import React from "react";

export default function MainContent({ user }) {
  return (
    <div style={{ flex: 1, padding: "20px" }}>
      <h2>Welcome, {user.email}</h2>
      <p>This is the main content area.</p>
    </div>
  );
}
