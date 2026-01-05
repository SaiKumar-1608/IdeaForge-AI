import React, { useState } from "react";

function ConceptCard({ concept, isSelected, onSelect }) {
  const [copied, setCopied] = useState(false);

  const copyConcept = async () => {
    const text = `${concept.concept_title}

${concept.description}

${concept.tagline}`;

    await navigator.clipboard.writeText(text);

    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <div
      className={`concept-card ${isSelected ? "selected" : ""}`}
      onClick={onSelect}
      style={{
        cursor: "pointer",
        padding: "16px",
        borderRadius: "8px",
        border: "1px solid #e5e7eb",
        marginBottom: "16px",
        position: "relative",
      }}
    >
      <h3 style={{ marginBottom: "8px" }}>{concept.concept_title}</h3>
      <p style={{ marginBottom: "8px", color: "#555" }}>
        {concept.description}
      </p>
      <strong>{concept.tagline}</strong>

      {/* 📋 COPY BUTTON */}
      {isSelected && (
        <button
          onClick={(e) => {
            e.stopPropagation(); // prevent reselect
            copyConcept();
          }}
          style={{
            position: "absolute",
            top: "12px",
            right: "12px",
            fontSize: "13px",
            padding: "6px 10px",
            borderRadius: "6px",
            background: copied ? "#16a34a" : "#6366f1",
            color: "#fff",
            border: "none",
            cursor: "pointer",
          }}
        >
          {copied ? "✅ Copied" : "📋 Copy"}
        </button>
      )}
    </div>
  );
}

export default ConceptCard;
