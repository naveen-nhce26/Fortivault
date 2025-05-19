import { useState } from "react";
import axios from "axios";

function RegisterForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    await axios.post("http://localhost:8000/register", {
      username,
      password,
    });
    alert("Registered! Please login.");
    window.location.href = "/";
  };

  return (
    <div className="p-4">
      <h2 className="text-xl">Register</h2>
      <input className="block border p-2 my-2" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input type="password" className="block border p-2 my-2" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button className="bg-green-500 text-white p-2" onClick={handleRegister}>Register</button>
    </div>
  );
}

export default RegisterForm;
