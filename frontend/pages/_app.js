import { useEffect } from "react";
import PropTypes from "prop-types";

import { getCookieConsentValue } from "react-cookie-consent";
import { initGA } from "../util/gtag";
import CookieBar from "../components/CookieBar";

import "../styles/globals.css";
import "@fontsource/inter/variable.css";

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    getCookieConsentValue() === "true" && initGA();
  }, []);

  return (
    <>
      <Component {...pageProps} />
      <CookieBar onAccept={initGA} />
    </>
  );
}

export default MyApp;

MyApp.propTypes = {
  Component: PropTypes.func,
  pageProps: PropTypes.object,
};
