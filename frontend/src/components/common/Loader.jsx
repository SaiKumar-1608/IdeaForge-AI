import React from "react";

/**
 * Simple loading indicator
 */
function Loader() {
  return (
    <div
      style={{
        marginTop: "24px",
        textAlign: "center",
        fontSize: "14px",
        color: "#555",
      }}
    >
      Generating creative concepts...
    </div>
  );
}

export default Loader;
