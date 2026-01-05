import React from "react";

/**
 * Reusable textarea component
 */
function TextArea({
  label,
  name,
  value,
  onChange,
  placeholder = "",
  required = false,
  rows = 4,
}) {
  return (
    <div style={{ marginBottom: "16px" }}>
      {label && (
        <label
          htmlFor={name}
          style={{
            display: "block",
            marginBottom: "6px",
            fontWeight: "500",
          }}
        >
          {label}
        </label>
      )}

      <textarea
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        required={required}
        rows={rows}
        style={{
          width: "100%",
          padding: "10px 12px",
          borderRadius: "6px",
          border: "1px solid #ccc",
          fontSize: "14px",
          resize: "vertical",
        }}
      />
    </div>
  );
}

export default TextArea;
