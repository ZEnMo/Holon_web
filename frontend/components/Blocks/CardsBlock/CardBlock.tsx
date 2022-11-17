import React from "react";
import Card from "./Card";
import ButtonBlock from "@/components/Button/ButtonBlock";

type Props = {
  data: {
    type: string;
    value: {
      cards: Array<CardItem>;
      buttonBlock: React.ComponentProps<typeof ButtonBlock["buttons"]>;
    };
    id: string;
  };
};

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

export default function CardBlock({
  data: {
    value: { cards, buttonBlock },
  },
}: Props) {
  return (
    <div>
      <div
        className={`grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 py-12 px-10 lg:px-16 lg:pt-16 gap-8`}>
        {cards.map((cardItem, index) => {
          return (
            <React.Fragment key={index}>
              <Card cardItem={cardItem}></Card>
            </React.Fragment>
          );
        })}
      </div>
      {buttonBlock.length > 0 && (
        <ButtonBlock
          buttons={buttonBlock[0].value.buttons}
          align={buttonBlock[0].value.buttonsAlign}></ButtonBlock>
      )}
    </div>
  );
}
