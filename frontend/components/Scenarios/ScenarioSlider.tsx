import Tooltip from "./Tooltip";

interface Props {
  locked?: boolean;
  neighbourhoodID: string;
  inputId: string;
  value: number;
  updateValue: (id: string, value: string) => void;
  label: string;
  scenarioId: string;
  message: string;
}

export default function ScenarioSlider({
  neighbourhoodID,
  locked,
  inputId,
  value,
  updateValue,
  label,
  message,
  scenarioId,
}: Props) {
  const sliderid = `scenarioslider${inputId}${neighbourhoodID}${scenarioId}`;
  return (
    <div className="mb-2 flex flex-row items-center justify-between gap-2">
      <label htmlFor={sliderid} className="flex">
        {label}
      </label>
      <div className="flex flex-row items-center justify-between gap-2">
        <input
          data-testid={sliderid}
          id={sliderid}
          type="range"
          onChange={(e) => updateValue(inputId, e.target.value)}
          value={value}
          disabled={locked}
          className={`h-1 w-3/5 ${
            locked ? "cursor-not-allowed" : ""
          } slider appearance-none disabled:bg-holon-grey-300`}
          min="0"
          max="100"
        />
        <input
          data-testid="scenariosliderinput"
          aria-label={`${label} input`}
          disabled={locked}
          id={`${sliderid}number`}
          type="number"
          onChange={(e) => updateValue(inputId, e.target.value)}
          value={value}
          className={`w-16 ${
            locked ? "cursor-not-allowed" : ""
          } rounded-sm border-2 border-holon-blue-900 bg-white p-1 text-right text-holon-blue-900 shadow-holon-blue placeholder:font-light placeholder:italic placeholder:text-holon-slated-blue-300 disabled:border-gray-500 disabled:text-slate-500 disabled:shadow-gray-500`}
          min="0"
          max="100"
        />
        <span>%</span>
        <Tooltip tooltipMessage={message}></Tooltip>
      </div>
    </div>
  );
}
