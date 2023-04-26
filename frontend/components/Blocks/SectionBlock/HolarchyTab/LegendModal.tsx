import Image from "next/image";

export type LegendItem = {
  label: string;
  imageSelector: {
    img: {
      src: string;
    };
  };
};

type LegendModal = {
  data: {
    color: LegendItem[];
    line: LegendItem[];
  };
};

function LegendModalItems({ legendItems }: LegendItem) {
  return legendItems.map(legendItem => (
    <li key={legendItem.label} className="flex flex-row items-center" title={legendItem.label}>
      <Image
        width="16"
        height="16"
        alt=""
        className="object-cover"
        src={legendItem.imageSelector.img.src}
      />
      <span className="ml-1 truncate">{legendItem.label}</span>
    </li>
  ));
}

export default function LegendModal({ data }: LegendModal) {
  return (
    <div className="flex flex-row justify-center ">
      <div
        role="figure"
        aria-label="Legend for colors and lines within image"
        className="gap-1 px-4 animate-fallDown py-2 min-w-[350px] h-auto bg-white flex flex-row justify-between z-50">
        <div className="w-1/2">
          <p>Type kleur</p>

          {data["color"] && (
            <ul>
              <LegendModalItems legendItems={data["color"]} />
            </ul>
          )}
        </div>
        <div className="w-1/2">
          <p>Type lijn</p>

          {data["line"] && (
            <ul>
              <LegendModalItems legendItems={data["line"]} />
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
