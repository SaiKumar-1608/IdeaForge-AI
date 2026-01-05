import React from "react";

/**
 * Skeleton loader for concept cards
 * Displays placeholder UI while concepts are loading
 */
function ConceptSkeleton({ count = 3 }) {
  return (
    <div style={{ display: "grid", gap: "20px" }}>
      {Array.from({ length: count }).map((_, index) => (
        <div
          key={index}
          style={{
            backgroundColor: "#ffffff",
            borderRadius: "8px",
            padding: "20px",
            boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
            animation: "pulse 1.5s ease-in-out infinite",
          }}
        >
          {/* Title */}
          <div
            style={{
              height: "20px",
              width: "60%",
              backgroundColor: "#e5e7eb",
              borderRadius: "4px",
              marginBottom: "12px",
            }}
          />

          {/* Description lines */}
          <div
            style={{
              height: "14px",
              width: "100%",
              backgroundColor: "#e5e7eb",
              borderRadius: "4px",
              marginBottom: "8px",
            }}
          />
          <div
            style={{
              height: "14px",
              width: "90%",
              backgroundColor: "#e5e7eb",
              borderRadius: "4px",
              marginBottom: "8px",
            }}
          />
          <div
            style={{
              height: "14px",
              width: "80%",
              backgroundColor: "#e5e7eb",
              borderRadius: "4px",
              marginBottom: "16px",
            }}
          />

          {/* Tagline */}
          <div
            style={{
              height: "16px",
              width: "40%",
              backgroundColor: "#e5e7eb",
              borderRadius: "4px",
            }}
          />
        </div>
      ))}

      {/* Keyframes */}
      <style>
        {`
          @keyframes pulse {
            0% {
              opacity: 1;
            }
            50% {
              opacity: 0.4;
            }
            100% {
              opacity: 1;
            }
          }
        `}
      </style>
    </div>
  );
}

export default ConceptSkeleton;
