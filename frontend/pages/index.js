import { Fragment } from "react";

import Head from "next/head";
import Link from "next/link";
import Image from "next/image";
import Scenarios from "../components/Scenarios";

function Card({ children, href }) {
  return (
    <a
      href={href}
      className="align-left m-3 max-w-xs rounded-md border p-5 text-black no-underline transition"
    >
      {children}
    </a>
  );
}

export default function Home() {
  return (
    <div className="px-2">
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="">
        <hr />

        <hr />
        <Scenarios
          solarpanels="8"
          heatpump="32"
          heatnetwork="true"
          legal="legal 3"

          />
        <hr />
        <h1 className="text-6xl">
          Welcome to <a href="https://nextjs.org">Next.js!</a>
        </h1>

        <p className="mt-6 text-lg">
          <Link href="tailwind-example">
            <a
              href="tailwind-example"
              className="group flex items-center gap-0.5 p-3 hover:no-underline"
            >
              <Fragment>
                <span className="group-hover:underline">See an example with Tailwind</span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 transition group-hover:translate-x-1"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fillRule="evenodd"
                    d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z"
                    clipRule="evenodd"
                  />
                </svg>
              </Fragment>
            </a>
          </Link>
        </p>

        <p className="my-6 text-center text-xl">
          Get started by editing{" "}
          <code className="rounded bg-gray-100 px-2 py-1">pages/index.js</code>
        </p>

        <div className="flex max-w-3xl flex-wrap items-center justify-center">
          <Card href="https://nextjs.org/docs">
            <h2 className="mb-3 text-2xl">Documentation &rarr;</h2>
            <p className="text-lg">Find in-depth information about Next.js features and API.</p>
          </Card>

          <Card href="https://nextjs.org/learn">
            <h2 className="mb-3 text-2xl">Learn &rarr;</h2>
            <p className="text-lg">Learn about Next.js in an interactive course with quizzes!</p>
          </Card>

          <Card href="https://github.com/vercel/next.js/tree/canary/examples">
            <h2 className="mb-3 text-2xl">Examples &rarr;</h2>
            <p className="text-lg">Discover and deploy boilerplate example Next.js projects.</p>
          </Card>

          <Card href="https://vercel.com/new?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app">
            <h2 className="mb-3 text-2xl">Deploy &rarr;</h2>
            <p className="text-lg">
              Instantly deploy your Next.js site to a public URL with Vercel.
            </p>
          </Card>
        </div>
      </main>

      <footer className="mb-3 text-lg">
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center justify-center hover:no-underline"
        >
          Powered by{" "}
          <span className="ml-1 mt-1 inline-block">
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  );
}
