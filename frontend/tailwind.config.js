/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "holon-gold-200": "#F3E7C5",
        "holon-gold-600": "#C89D28",
        "holon-blue-200": "#C6D8F2",
        "holon-blue-500": "#23549F",
        "holon-blue-900": "#051E3F",
        "holon-grey-300": "#BFBFBF",
        "holon-slated-blue-300": "#AEC2E6",
      },
      backgroundImage: {
        "split-white-blue": "linear-gradient(-18deg, #051E3F 40% , white 30%)",
        "split-blue-white": "linear-gradient(-18deg, white 45%, #051E3F 40%)",
      },
      borderWidth: {
        8: "24px",
      },
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
      },
      translate: {
        "holon-bh-x": "0.2rem", // holon-bh :: holon-button-hover
        "holon-bh-y": "0.1rem",
      },
      boxShadow: {
        "holon-white": "0.3rem 0.15rem white",
        "holon-white-hover": "0.1rem 0.05rem white",
        "holon-blue": "0.3rem 0.15rem #051E3F",
        "holon-blue-hover": "0.1rem 0.05rem #051E3F",
        golden: "inset 0 -25px 0px 0px #F3E7C5",
        blue: "inset 0 -25px 0px 0px #AEC2E6",
      },
      keyframes: {
        appear: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        fallDown: {
          "0%": { transform: "translateY(-5rem)", opacity: "0" },
          "100%": { transform: "translateY(0)", opacity: "1" },
        },
        riseUp: {
          "0%": { transform: "translateY(0rem)", opacity: "1" },
          "100%": { transform: "translateY(-5rem)", opacity: "0" },
        },
        spinWindmill: {
          "0%": { transform: "rotate(0deg)", "transform-origin": "42.5% 61.266%" },
          "100%": { transform: "rotate(360deg)", "transform-origin": "42.5% 61.266%" },
        },
      },
      animation: {
        "appear-quick": "appear 1s ease-in",
        fallDown: "fallDown 1s ease-in",
        riseUp: "riseUp 1s ease-in",
        spinWindmill: "spinWindmill 4s linear infinite",
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
