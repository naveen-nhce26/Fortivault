import React from "react";
import Sidebar from "./Sidebar";
import MainContent from "./MainContent";

export default function Dashboard({ user, onLogout }) {
  return (
    <div style={{ display: "flex" }}>
      <Sidebar onLogout={onLogout} />
      <MainContent user={user} />
    </div>
  );
}
