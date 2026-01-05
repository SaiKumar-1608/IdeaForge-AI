import React from "react";

/**
 * Optional application footer
 */
function Footer() {
  return (
    <footer
      style={{
        marginTop: "40px",
        padding: "12px 24px",
        textAlign: "center",
        fontSize: "13px",
        color: "#6b7280",
        borderTop: "1px solid #e5e7eb",
      }}
    >
      © {new Date().getFullYear()} IdeaForge AI. All rights reserved.
    </footer>
  );
}

export default Footer;
