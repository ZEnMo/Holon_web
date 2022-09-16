import { MDXProvider } from "@mdx-js/react";
import PropTypes from "prop-types";
import React, { Fragment } from "react";

interface IMDXItemProps {
  children: string;
}

const articleComponents = {
  h1: (props: IMDXItemProps) => <h1 id={"h1-" + encodeURIComponent(props.children)} {...props} />,
  h2: (props: IMDXItemProps) => <h2 id={"h2-" + encodeURIComponent(props.children)} {...props} />,
  h3: (props: IMDXItemProps) => <h2 id={"h3-" + encodeURIComponent(props.children)} {...props} />,
  h4: (props: IMDXItemProps) => <h2 id={"h4-" + encodeURIComponent(props.children)} {...props} />,
  h5: (props: IMDXItemProps) => <h2 id={"h5-" + encodeURIComponent(props.children)} {...props} />,
  h6: (props: IMDXItemProps) => <h2 id={"h6-" + encodeURIComponent(props.children)} {...props} />,
};

const sidecomponents = {
  h1: (props: IMDXItemProps) =>
    typeof typeof props.children !== "object" && (
      <a
        className="wiki-context-menu-link px-4 pt-1 pb-3"
        href={"#h1-" + encodeURIComponent(props.children)}
        {...props}
      />
    ),
  h2: (props: IMDXItemProps) =>
    typeof props.children !== "object" && (
      <a
        className="wiki-context-menu-link px-4 pt-1 pb-3"
        href={"#h2-" + encodeURIComponent(props.children)}
        {...props}
      />
    ),
  h3: (props: IMDXItemProps) =>
    typeof props.children !== "object" && (
      <a
        className="wiki-context-menu-link px-4 pt-1 pb-3"
        href={"#h3-" + encodeURIComponent(props.children)}
        {...props}
      />
    ),
  h4: (props: IMDXItemProps) =>
    typeof props.children !== "object" && (
      <a
        className="wiki-context-menu-link px-4 pt-1 pb-3"
        href={"#h4-" + encodeURIComponent(props.children)}
        {...props}
      />
    ),
  h5: (props: IMDXItemProps) =>
    typeof props.children !== "object" && (
      <a
        className="wiki-context-menu-link px-4 pt-1 pb-3"
        href={"#h5-" + encodeURIComponent(props.children)}
        {...props}
      />
    ),
  h6: (props: IMDXItemProps) =>
    typeof props.children !== "object" && (
      <a
        className="wiki-context-menu-link px-4 pt-1 pb-3"
        href={"#h6-" + encodeURIComponent(props.children)}
        {...props}
      />
    ),

  //ignore all other tags
  p: () => null,
  code: () => null,
  span: () => null,
  ul: () => null,
  ol: () => null,
  hr: () => null,
  div: () => null,
  table: () => null,
  blockquote: () => null,
  section: () => null,
};

interface ArticleProps {
  article?: React.ReactNode;
}

export default function Article({ article }: ArticleProps) {
  return (
    <Fragment>
      <MDXProvider components={articleComponents}>
        <article className="prose mt-5 ml-10 mb-16 w-3/4">{article}</article>
      </MDXProvider>
      <nav className=" mx-3 w-1/4 border-l-2 border-gray-200">
        <div className="sticky top-0 mx-3 pt-5 ">
          <h3 className="px-4 pt-1 pb-3">
            <strong>Inhoudsopgave</strong>
          </h3>
          <div className="wiki-context-menu">
            <MDXProvider components={sidecomponents}>{article}</MDXProvider>
          </div>
        </div>
      </nav>
    </Fragment>
  );
}

Article.propTypes = {
  article: PropTypes.shape({}),
};
