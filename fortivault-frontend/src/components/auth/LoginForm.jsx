import { useState } from "react";
import axios from "axios";

function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const res = await axios.post("http://localhost:8000/login", {
      username,
      password,
    });
    localStorage.setItem("token", res.data.access_token);
    window.location.href = "/dashboard";
  };

  return (
    <div className="p-4">
      <h2 className="text-xl">Login</h2>
      <input className="block border p-2 my-2" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input type="password" className="block border p-2 my-2" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button className="bg-blue-500 text-white p-2" onClick={handleLogin}>Login</button>
    </div>
  );
}

export default LoginForm;
