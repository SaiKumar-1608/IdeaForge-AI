import React from "react";

/**
 * Displays error messages from backend or frontend
 */
function ErrorAlert({ message }) {
  if (!message) return null;

  return (
    <div
      style={{
        marginTop: "20px",
        padding: "12px 16px",
        borderRadius: "6px",
        backgroundColor: "#fee2e2",
        color: "#991b1b",
        border: "1px solid #fecaca",
      }}
    >
      {message}
    </div>
  );
}

export default ErrorAlert;
