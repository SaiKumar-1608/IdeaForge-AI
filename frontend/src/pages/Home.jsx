import React, { useEffect } from "react";
import GenerateConcept from "./GenerateConcept";

/**
 * Home page – redirects to GenerateConcept
 */
function Home() {
  useEffect(() => {
    // Future routing can be added here if needed
  }, []);

  return <GenerateConcept />;
}

export default Home;
