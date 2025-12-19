import React from "react";
import ReactDOM from "react-dom/client";
import MyCarousel from "./MyCarousel";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
  <React.StrictMode>
    <MyCarousel />
  </React.StrictMode>
);
