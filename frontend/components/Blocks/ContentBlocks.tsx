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
import { Content, SavedElements } from "./SectionBlock/types";
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
  const [savedValues, setSavedValues] = useState({});
  const [checkedSavedValues, setCheckedSavedValues] = useState(false);
  const [openingSection, setOpeningSection] = useState<string>("");
  
  const { asPath } = useRouter();
  let scenarioDiffElements = {}; 
  let sectionCount = 0; 

  useEffect(() => {
    checkIfSavedScenario();
    if (Object.keys(savedValues).length !== 0) {
      const elem = document.getElementById(openingSection);
      elem?.scrollIntoView({ behavior: "smooth" });
    }
  }, []);

  /*Adds target values of previous sections to interactive elements in the section */
  function addTargetValues(values, content: Content[]) {
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
  function updateTargetValues(content: Content[]) {
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
  function saveScenario(title: string, description: string, sectionId: string) {
    //get baseUrl
    const origin =
      typeof window !== "undefined" && window.location.origin ? window.location.origin : "";

    const pathWithoutParams = asPath.split('?')[0]; 
    const baseURL = `${origin}${pathWithoutParams}`;
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
    params.append("title", encodeURIComponent(title));
    params.append("currentSection", encodeURIComponent(sectionId));
    description && params.append("description", encodeURIComponent(description));
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

        if (decodedKey === "title") {
          data[decodedKey] = decodedValue;
        } else if (decodedKey === "description") {
          data[decodedKey] = decodedValue;
        } else if (decodedKey === "currentSection") {
          data[decodedKey] = decodedValue;
          setOpeningSection(decodedValue);
        } else {
          const [section, key] = decodedKey.split(".");
          if (!(section in data)) {
            data[section] = {};
          }
          data[section][key] = decodedValue;
        }
      }
    }

    setSavedValues(data);
    setCheckedSavedValues(true);
  }

  function addSavedValues(values: SavedElements, content: Content) {
    //add saved values to content or scenarioDiffElements
    const updatedContent = { ...content }; 
    for (const key in values) {
      if (key === "title") {
        updatedContent.value.scenarioTitle = values[key];
      } else if (key === "description") {
        updatedContent.value.scenarioDescription = values[key];
      } else if (key === "currentSection" && values[key] === content.id) {
        updatedContent.value.openingSection = true;
      } else if (key === content.id) {
        const value = values[key];
        
        for (const subKey in value) {

          const foundElement = updatedContent.value.content.find(element => {
            return element.type === "interactive_input" && element.value.id === Number(subKey);
          });
         if (foundElement) {
            const subValue = value[subKey];
            foundElement.value.savedValue = subValue;
          }
          else {
            scenarioDiffElements[content.id] = {
              ...(scenarioDiffElements[content.id] || {}),
      
                [subKey]: {
                  value: value[subKey],
                  difference: "missing",
                }
              
            }
          }
        }
      }
    }

     // Check for elements in content that are not in values
     let valuesIds: string[]; 
    values[content.id] ? valuesIds = Object.keys(values[content.id]) : valuesIds = [];
    console.log(valuesIds); 
  
    for (const element of updatedContent.value.content) {
    if (
      element.type === "interactive_input" &&
      element.value.visible === true &&
      !valuesIds.includes(element.value.id.toString())
    ) {
      const subKey = element.value.id.toString();
   
      scenarioDiffElements[content.id] = {
        ...(scenarioDiffElements[content.id] || {}),
        [subKey]: {
          value: element.value,
          difference: "added",
        },
      };
    }
  }
 
    return updatedContent;
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
            sectionCount++; 
            const newContent = addTargetValues(targetValuesPreviousSections, contentItem);
            //if there are any savedValues in the parameters, these are added to the section
            const savedValuesContent =
              Object.keys(savedValues).length !== 0
                ? addSavedValues(savedValues, newContent)
                : newContent;
            updateTargetValues(contentItem.value.content);
            return (
              checkedSavedValues && (
                <SectionBlock
                  key={`section ${contentItem.id}`}
                  pageSectionCount={sectionCount}
                  data={savedValuesContent}
                  pagetype={pagetype}
                  feedbackmodals={feedbackmodals}
                  graphcolors={graphcolors ?? []}
                  savePageValues={saveSectionValues}
                  saveScenario={saveScenario}
                  scenarioDiffElements={scenarioDiffElements}
                />
              )
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
