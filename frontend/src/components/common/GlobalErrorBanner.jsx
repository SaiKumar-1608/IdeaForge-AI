import React from "react";
import { useAppState } from "../../context/AppStateContext";

const styles = {
  container: {
    padding: "12px 16px",
    marginBottom: "16px",
    borderRadius: "4px",
    backgroundColor: "#fdecea",
    color: "#611a15",
    border: "1px solid #f5c6cb",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center"
  },
  message: {
    fontSize: "14px"
  },
  closeButton: {
    background: "transparent",
    border: "none",
    fontSize: "16px",
    cursor: "pointer",
    color: "#611a15"
  }
};

export default function GlobalErrorBanner() {
  const { state, dispatch } = useAppState();
  const { error } = state;

  if (!error) return null;

  const handleClose = () => {
    dispatch({
      type: "GENERATE_CONCEPTS_ERROR",
      payload: null
    });
  };

  return (
    <div style={styles.container} role="alert">
      <span style={styles.message}>{error}</span>
      <button
        onClick={handleClose}
        style={styles.closeButton}
        aria-label="Dismiss error"
      >
        ×
      </button>
    </div>
  );
}
