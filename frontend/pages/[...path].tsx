import querystring from "querystring";
import { getPage, getRedirect, getAllPages, WagtailApiResponseError } from "../api/wagtail";
import LazyContainers from "../containers/LazyContainers";

const isProd = process.env.NODE_ENV === "production";

export default function CatchAllPage({ componentName, componentProps }) {
  const Component = LazyContainers[componentName];
  if (!Component) {
    return <h1>Component {componentName} not found</h1>;
  }
  return <Component {...componentProps} />;
}

// For SSR
export async function getServerSideProps({ req, params, res, resolvedUrl }) {
  let path = params?.path || [];
  path = path.join("/");

  const { host } = req.headers;
  let queryParams = new URL(req.url, `https://${host}`).search;
  if (queryParams.indexOf("?") === 0) {
    queryParams = queryParams.substr(1);
  }
  queryParams = querystring.parse(queryParams);

  const nonWagtailPages = [
    { path: "/inloggen/", container: "CustomNonWagtailPage", type: "login" },
    { path: "/registratie/", container: "CustomNonWagtailPage", type: "registratie" },
    { path: "/profiel/", container: "CustomNonWagtailPage", type: "profiel" },
    { path: "/tiles-demo/", container: "CustomNonWagtailPage", type: "tiles-demo" },
    { path: "/animation-demo/", container: "CustomNonWagtailPage", type: "animation-demo" },
    {
      path: "/wachtwoord-aanmaken/",
      container: "CustomNonWagtailPage",
      type: "wachtwoord-aanmaken",
    },
    {
      path: "/wachtwoord-aanvragen/",
      container: "CustomNonWagtailPage",
      type: "wachtwoord-aanvragen",
    },
  ];

  const {
    json: { componentProps },
  } = await getPage("/", queryParams, {
    headers: {
      cookie: req.headers.cookie,
      host,
    },
  });

  try {
    for await (const page of nonWagtailPages) {
      if (resolvedUrl == page.path) {
        const componentName = page.container;
        componentProps.type = page.type;
        return { props: { componentName, componentProps } };
      }
    }
  } catch (err) {
    return err;
  }

  // Try to serve page
  try {
    const {
      json: { componentName, componentProps, redirect, customResponse },
      headers,
    } = await getPage(path, queryParams, {
      headers: {
        cookie: req.headers.cookie,
        host,
      },
    });

    // Forward any cookie we encounter
    const cookies = headers.get("set-cookie");
    if (cookies) {
      res.setHeader("Set-Cookie", cookies);
    }

    if (customResponse) {
      const { body, body64, contentType } = customResponse;
      res.setHeader("Content-Type", contentType);
      res.statusCode = 200;
      res.write(body64 ? Buffer.from(body64, "base64") : body);
      res.end();

      return { props: {} };
    }

    if (redirect) {
      const { destination, isPermanent } = redirect;
      return {
        redirect: {
          destination: destination,
          permanent: isPermanent,
        },
      };
    }

    if (componentName === "WikiPage") {
      const { json: wikiMenu } = await getAllPages({ type: "main.WikiPage" });
      componentProps.wikiMenu = wikiMenu;
    }

    return { props: { componentName, componentProps } };
  } catch (err) {
    if (!(err instanceof WagtailApiResponseError)) {
      throw err;
    }

    // When in development, show django error page on error
    if (!isProd && err.response.status >= 500) {
      const html = await err.response.text();
      return {
        props: {
          componentName: "PureHtmlPage",
          componentProps: { html },
        },
      };
    }

    if (err.response.status >= 500) {
      throw err;
    }
  }

  // Try to serve redirect
  try {
    const { json: redirect } = await getRedirect(path, queryParams, {
      headers: {
        cookie: req.headers.cookie,
        host,
      },
    });
    const { destination, isPermanent } = redirect;
    return {
      redirect: {
        destination: destination,
        permanent: isPermanent,
      },
    };
  } catch (err) {
    if (!(err instanceof WagtailApiResponseError)) {
      throw err;
    }

    if (err.response.status >= 500) {
      throw err;
    }
  }

  // Serve 404 page
  return { notFound: true };
}

// For SSG
/*
export async function getStaticProps({ params, preview, previewData }) {
    params = params || {};
    let path = params.path || [];
    path = path.join("/");

    const { json: pageData } = await getPage(path);
    return { props: pageData }
}

export async function getStaticPaths() {
    const { json: data } = await getAllPages();

    let htmlUrls = data.items.map(x => x.relativeUrl);
    htmlUrls = htmlUrls.filter(x => x);
    htmlUrls = htmlUrls.map(x => x.split("/"));
    htmlUrls = htmlUrls.map(x => x.filter(y => y))
    htmlUrls = htmlUrls.filter(x => x.length)

    const paths = htmlUrls.map(x => (
        { params: { path: x } }
    ));

    return {
        paths: paths,
        fallback: false,
    };
}
*/
