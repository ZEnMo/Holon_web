import React from "react";
import s from "./RawHtml.module.css";

const RawHtml = ({ html }: { html: string }) => (
  <div className={s.Container} dangerouslySetInnerHTML={{ __html: html }} />
);

export default RawHtml;
