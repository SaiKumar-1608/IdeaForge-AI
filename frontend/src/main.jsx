import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Vite + React entry point
import { AppStateProvider } from "./context/AppStateContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <AppStateProvider>
    <App />
  </AppStateProvider>
);