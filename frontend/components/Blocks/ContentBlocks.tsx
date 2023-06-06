import { useRouter } from "next/router";
import React, { useEffect, useState } from "react";
import {
  CardBlockVariant,
  Graphcolor,
  HeroBlockVariant,
  PageProps,
  TextAndMediaVariant,
  TitleBlockVariant,
} from "../../containers/types";
import ButtonsAndMediaBlock from "./ButtonsAndMediaBlock/ButtonsAndMediaBlock";
import CardBlock from "./CardsBlock/CardBlock";
import { FeedbackModal } from "./ChallengeFeedbackModal/types";
import HeaderFullImageBlock from "./HeaderFullImageBlock/HeaderFullImageBlock";
import HeroBlock from "./HeroBlock/HeroBlock";
import ParagraphBlock from "./ParagraphBlock";
import SectionBlock from "./SectionBlock/SectionBlock";
import { SavedElements } from "./SectionBlock/types";
import TableBlock from "./TableBlock/TableBlock";
import TextAndMediaBlock from "./TextAndMediaBlock/TextAndMediaBlock";
import TitleBlock from "./TitleBlock/TitleBlock";

export type Feedbackmodals = [FeedbackModal];

type ContentBlockProps = PageProps<
  TextAndMediaVariant | HeroBlockVariant | TitleBlockVariant | CardBlockVariant
>;

const ContentBlocks = ({
  content,
  pagetype,
  feedbackmodals,
  graphcolors,
}: {
  content: ContentBlockProps[];
  feedbackmodals?: Feedbackmodals[];
  pagetype?: string;
  graphcolors?: Graphcolor[];
}) => {
  let targetValuesPreviousSections = new Map();
  const [currentPageValues, setCurrentPageValues] = useState({});
  const { asPath } = useRouter();
  const [savedValues, setSavedValues] = useState({});

  useEffect(() => {
    checkIfSavedScenario();
  }, []);

  useEffect(() => {
    console.log(savedValues);
  }, [savedValues]);

  /*Adds target values of previous sections to interactive elements in the section */
  function addTargetValues(values, content) {
    const updatedContent = { ...content };
    const uniqueTargetValues = [];

    values.forEach((value, key) => {
      const foundElement = updatedContent.value.content.find(element => {
        return element.type === "interactive_input" && element.value.id === key;
      });

      if (foundElement) {
        foundElement.value.targetValuePreviousSection = value.targetValue;
      } else {
        //if the element does not exist yet it is added to an array (the element is invisible and with no other defaultValues besides the target value(s))
        uniqueTargetValues.unshift({
          type: "interactive_input",
          value: {
            ...value,
            visible: false,
            defaultValueOverride: "",
            targetValuePreviousSection: value.targetValue,
            options: value.options.map(option => ({
              ...option,
              default: false,
            })),
          },
        });
      }
    });
    //the array target values is placed in front of the list with interactive input elements, keeping the order in which they were placed on the page
    uniqueTargetValues.map(item => {
      updatedContent.value.content.unshift(item);
    });

    return updatedContent;
  }

  /*loops through current section and if there is an interactive element with a target value it creates a clone of the map, either updating an existing interactive input or adding one and then setting that clone to the variable targetValue*/
  function updateTargetValues(content) {
    content.map(element => {
      if (element.type === "interactive_input" && element.value.targetValue) {
        const newTargetValues = new Map(targetValuesPreviousSections);
        newTargetValues.set(element.value.id, element.value);
        targetValuesPreviousSections = newTargetValues;
      }
    });
    return null;
  }

  /*Saves all current values of visible interactive elements in a section */
  function saveSectionValues(sectionValue: SavedElements) {
    const newCurrentPageValues = Object.assign(currentPageValues, sectionValue);
    setCurrentPageValues(newCurrentPageValues);
  }

  /*Save scenario functionality. Creates a link of the page with the current values of visible interactive elements of the different sections in the params*/
  function saveScenario() {
    console.log(currentPageValues);
    //get baseUrl
    const origin =
      typeof window !== "undefined" && window.location.origin ? window.location.origin : "";
    const baseURL = `${origin}${asPath}`;
    //get params
    const params = new URLSearchParams();
    const data = currentPageValues;
    //so far so good, data klopt
    for (const section in data) {
      for (const key in data[section]) {
        for (const key in data[section]) {
          const encodedKey = encodeURIComponent(`${section}.${key}`); // modify key format
          const encodedValue = encodeURIComponent(data[section][key]);
          params.append(encodedKey, encodedValue);
        }
      }
    }
    //create link
    const savedScenarioUrl = `${baseURL}?${params.toString()}`;
    return savedScenarioUrl;
  }

  function checkIfSavedScenario() {
    const urlParams =
      typeof window !== "undefined" && window.location.origin
        ? new URLSearchParams(window.location.search)
        : null;

    const data = {};

    if (urlParams) {
      for (const [encodedKey, encodedValue] of urlParams) {
        const decodedKey = decodeURIComponent(encodedKey);
        const decodedValue = decodeURIComponent(encodedValue);

        const [section, key] = decodedKey.split(".");
        if (!(section in data)) {
          data[section] = {};
        }
        data[section][key] = decodedValue;
      }
    }
    setSavedValues(data);
  }

  function addSavedValues(values, content) {
    values.keys(item => {
      if (item === content.id) {
      }
    });
  }

  return (
    <React.Fragment>
      {content?.map(contentItem => {
        switch (contentItem.type) {
          case "header_full_image_block":
            return <HeaderFullImageBlock key={`headerfull ${contentItem.id}`} data={contentItem} />;
          case "paragraph_block":
            return <ParagraphBlock key={`paragraphBlock ${contentItem.id}`} data={contentItem} />;
          case "table_block":
            return (
              <div className="holonContentContainer defaultBlockPadding">
                <TableBlock key={`tableBlock ${contentItem.id}`} data={contentItem} />;
              </div>
            );
          case "text_image_block":
            return <TextAndMediaBlock key={`txtmedia ${contentItem.id}`} data={contentItem} />;
          case "hero_block":
            return <HeroBlock key={`heroblock ${contentItem.id}`} data={contentItem} />;
          case "title_block":
            return <TitleBlock key={`titleblock ${contentItem.id}`} data={contentItem} />;
          case "card_block":
            return <CardBlock key={`cardsblock ${contentItem.id}`} data={contentItem} />;
          case "section":
            const newContent = addTargetValues(targetValuesPreviousSections, contentItem);
            //const savedValuesContent = addSavedValues(savedValues, contentItem);
            //console.log(savedValuesContent);
            updateTargetValues(contentItem.value.content);
            return (
              <SectionBlock
                key={`section ${contentItem.id}`}
                data={newContent}
                pagetype={pagetype}
                feedbackmodals={feedbackmodals}
                graphcolors={graphcolors ?? []}
                savePageValues={saveSectionValues}
                saveScenario={saveScenario}
              />
            );
          case "buttons_and_media_block":
            return (
              <ButtonsAndMediaBlock key={`buttonsmedia ${contentItem.id}`} data={contentItem} />
            );
          default:
            null;
        }
      })}
    </React.Fragment>
  );
};

export default ContentBlocks;
