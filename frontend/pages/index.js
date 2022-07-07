import { Fragment } from "react";
import Head from "next/head";
import Link from "next/link";
import Image from "next/image";
import Scenarios from "../components/Scenarios";
import IntroductionVideo from "../components/IntroductionVideo";

import HolonStyle from "./holon-style";
import TextBlock from "../components/TextBlock";
import WelcomePage from "../components/WelcomePage";
import ContentBlock from "../components/ContentBlock";
import HolonButton from "../components/Buttons/HolonButton";

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
  const neighbourhood1 = {
    heatpump: { value: "0", label: "Warmtepompen" },
    evadoptation: { value: "70", label: "Elektrische auto's" },
    solarpanels: { value: "40", label: "Zonnepanelen" },
    heatnetwork: { value: false, label: "Warmtenet" },
  };
  const neighbourhood2 = {
    heatpump: { value: "0", label: "Warmtepompen" },
    evadoptation: { value: "70", label: "Elektrische auto's" },
    solarpanels: { value: "60", label: "Zonnepanelen" },
    heatnetwork: { value: true, label: "Warmtenet" },
  };
  return (
    <div>
      <Head>
        <title>HOLON en de kunst van het Loslaten</title>
        <meta name="description" content="HOLON en de kunst van het Loslaten" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="h-screen snap-y snap-mandatory overflow-y-auto">
        <ContentBlock>
          <WelcomePage></WelcomePage>
        </ContentBlock>
        <ContentBlock colorClass="bg-split-white-blue"></ContentBlock>
        <ContentBlock colorClass="bg-holon-blue-900" id="introVideo">
          <IntroductionVideo />
        </ContentBlock>
        <ContentBlock colorClass="bg-split-blue-white"></ContentBlock>
        <ContentBlock>
          <TextBlock value="hoeDoen" borderColor="border-holon-slated-blue-300"></TextBlock>
        </ContentBlock>
        <ContentBlock>
          <Scenarios
            locked
            scenarioTitle="Het moet anders"
            borderColor="border-holon-slated-blue-300"
            neighbourhood1={neighbourhood1}
            neighbourhood2={neighbourhood2}
            windholon={true}
          />
        </ContentBlock>
        <ContentBlock>
          <TextBlock
            value="slimmerSamenwerken"
            borderColor="border-holon-gold-200"
            right="true"
          ></TextBlock>
        </ContentBlock>
        <ContentBlock>
          <Scenarios
            locked
            scenarioTitle="De windcoöperatie"
            right="true"
            borderColor="border-holon-gold-200"
            neighbourhood1={neighbourhood1}
            neighbourhood2={neighbourhood2}
            windholon={true}
          />
        </ContentBlock>
        <ContentBlock>
          <TextBlock value="warmte" borderColor="border-holon-blue-900"></TextBlock>
        </ContentBlock>
        <ContentBlock>
          <Scenarios
            locked
            scenarioTitle="Ook warmte een rol"
            borderColor="border-holon-blue-900"
            neighbourhood1={neighbourhood1}
            neighbourhood2={neighbourhood2}
            windholon={true}
          />
        </ContentBlock>
        <ContentBlock>
          <TextBlock
            value="tweeKeerSlimmer"
            borderColor="border-holon-gold-600"
            right="true"
          ></TextBlock>
        </ContentBlock>
        <ContentBlock>
          <Scenarios
            locked
            scenarioTitle="Twee keer slimmer"
            borderColor="border-holon-gold-600"
            right="true"
            neighbourhood1={neighbourhood1}
            neighbourhood2={neighbourhood2}
            windholon={true}
          />
        </ContentBlock>
        <ContentBlock>
          <TextBlock
            value="afsluiter"
            underlineTitle="true"
            colorUnderline="decoration-holon-slated-blue-300"
          >
            <HolonButton variant="blue">Naar het open model</HolonButton>
            <HolonButton variant="blue">Op de hoogte blijven</HolonButton>
          </TextBlock>
        </ContentBlock>
        <ContentBlock>
          <Scenarios
            neighbourhood1={neighbourhood1}
            neighbourhood2={neighbourhood2}
            windholon={true}
          />
        </ContentBlock>
        <ContentBlock colorClass="bg-split-white-blue"></ContentBlock>
      </main>
    </div>
  );
}
