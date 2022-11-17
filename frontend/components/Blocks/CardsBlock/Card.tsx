import RawHtml from "../../RawHtml/RawHtml";

type CardItem = {
  title: string;
  imageSelector: {
    id: number;
    title: string;
    img: {
      src: string;
      width: number;
      height: number;
      alt: string;
    };
  };
  text: string;
  cardBackground: string;
};

type Props = {
  cardItem: CardItem;
};

export default function Card({ cardItem }: Props) {
  const colorStyle: string = cardItem.cardBackground;

  return (
    <div className={` min-h-[400px] ${colorStyle} border-solid border-2 rounded-lg flex flex-col`}>
      <div className="overflow-hidden relative m-4 mb-0 flex-1 border">
        {/* eslint-disable @next/next/no-img-element */}
        <img
          src={cardItem.imageSelector.img.src}
          alt={cardItem.imageSelector.img.alt}
          width="725"
          height="380"
          className="object-cover object-center h-full w-full max-w-none max-h-none"
        />
      </div>

      <span className="flex-col flex m-4 flex-1 max-h:1/2 overflow-hidden">
        <strong className="mb-3 block">{cardItem.title}</strong>
        <span className="">
          <RawHtml html={cardItem.text} />
        </span>
      </span>
    </div>
  );
}
