import React from "react";
import GenerateConcept from "./pages/GenerateConcept";
import Header from "./components/layout/Header";
import GlobalErrorBanner from "./components/common/GlobalErrorBanner";

/**
 * Root application layout (Production-grade)
 */
function App() {
  return (
    <div style={{ minHeight: "100vh", backgroundColor: "#f9fafb" }}>
      {/* Header */}
      <Header />

      {/* Global Error Banner (single error surface for entire app) */}
      <div style={{ maxWidth: "1100px", margin: "0 auto", padding: "0 24px" }}>
        <GlobalErrorBanner />
      </div>

      {/* Main Content */}
      <main style={{ padding: "24px", maxWidth: "1100px", margin: "0 auto" }}>
        <GenerateConcept />
      </main>
    </div>
  );
}

export default App;
