import React from "react";
import CardItem from "./Card";
import Card from "./Card";
import ButtonBlock from "@/components/Button/ButtonBlock";

type Props = {
  data: {
    type: string;
    value: {
      cards: Array<typeof CardItem>;
      buttonBlock: React.ComponentProps<typeof ButtonBlock["buttons"]>;
    };
    id: string;
  };
};

export default function CardBlock({
  data: {
    value: { cards, buttonBlock },
  },
}: Props) {
  return (
    <div>
      <div
        className={`grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 defaultBlockPadding gap-8`}
        data-testid="cardblock">
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
