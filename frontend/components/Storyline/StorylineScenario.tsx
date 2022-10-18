import { useState, useEffect } from "react";
import ImgFlatSolar from "../InteractiveImage/ImageElements/ImgFlatSolar";
import ImageSlider from "../InteractiveImage/ImageSlider";

export type Storyline = {
  title: string;
  description: string;
  body: Array<StorylineScenario>;
};

export type StorylineScenarioWrapper = {
  id: string;
  type: string;
  value: StorylineScenario;
};

export type StorylineScenario = {
  name: string;
  description?: string;
  tag: string;
  sliderValueDefault: number;
  sliderValueMin: number;
  sliderValueMax: number;
  sliderLocked: boolean;
};

type Props = {
  storylineScenario: StorylineScenario[] | [];
};

export default function StorylineScenario({ storylineScenario: scenario }: Props) {
  const [solarpanels, setSolarpanels] = useState(0);
  const [solarpanelsProperties, setSolarpanelsProperties] = useState({});
  const [windmills, setWindmills] = useState(0);
  const [windmillsProperties, setWindmillsProperties] = useState({});

  useEffect(() => {
    setScenarioData(scenario);
  }, [scenario]);

  const setScenarioData = (scenarios: StorylineScenarioWrapper[]) => {
    scenarios.map((scenario: StorylineScenarioWrapper) => {
      switch (scenario.value.tag) {
        case "solar":
          setSolarpanelsProperties(scenario);
          setSolarpanels(
            scenario?.value.sliderValueMin && scenario?.value.sliderValueDefault
              ? scenario?.value.sliderValueDefault
              : 0
          );
          break;
        case "windmills":
          setWindmillsProperties(scenario);
          setWindmills(
            scenario?.value.sliderValueMin && scenario?.value.sliderValueDefault
              ? scenario?.value.sliderValueDefault
              : 0
          );
          break;
        default:
          return null;
      }
    });
  };

  function updateLayers(value: string, setValue: (newValue: number) => void) {
    const newValue: number = parseInt(value);
    setValue(newValue);
  }

  return (
    <div className="storyline__row flex flex-col lg:flex-row">
      <div className="flex flex-col p-8 lg:w-1/3">
        <ImageSlider
          inputId="zonnepanelen_flat"
          datatestid="zonnepanelen_flat"
          value={solarpanels}
          setValue={setSolarpanels}
          min={solarpanelsProperties.value?.sliderValueMin}
          max={solarpanelsProperties.value?.sliderValueMax}
          step={1}
          label="Aantal zonnepanelen"
          updateLayers={updateLayers}
          type="range"
          locked={solarpanelsProperties.value?.sliderLocked}></ImageSlider>

        {!isNaN(windmillsProperties.value?.sliderValueDefault) ? (
          <ImageSlider
            inputId="windmills_flat"
            datatestid="windmills_flat"
            value={windmills}
            setValue={setWindmills}
            min={windmillsProperties.value?.sliderValueMin}
            max={windmillsProperties.value?.sliderValueMax}
            step={1}
            label="Aantal windmolens"
            updateLayers={updateLayers}
            type="range"
            locked={windmillsProperties.value?.sliderLocked}></ImageSlider>
        ) : null}
        {/* <div>{windmills?.value.description}</div> */}
      </div>
      <div
        className="flex flex-col lg:w-2/3"
        data-solarpanels={solarpanels}
        data-windmills={windmills}
        data-windforce={3}>
        <div className="storyline__row__image lg:sticky top-0 p-8">
          <ImgFlatSolar></ImgFlatSolar>
        </div>
      </div>
    </div>
  );
}
