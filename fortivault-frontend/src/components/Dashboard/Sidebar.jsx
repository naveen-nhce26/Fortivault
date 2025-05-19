import React from "react";

export default function Sidebar({ onLogout }) {
  return (
    <div style={{ width: "200px", backgroundColor: "#ddd", padding: "20px" }}>
      <h3>Sidebar</h3>
      <button onClick={onLogout}>Logout</button>
    </div>
  );
}
