import { useState } from "react";
import axios from "axios";

function AddUser() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleAdd = async () => {
    await axios.post("http://localhost:8000/admin/add-user", {
      username,
      password,
      is_admin: false,
    });
    alert("User added.");
  };

  return (
    <div className="p-4">
      <h3 className="text-lg">Add User</h3>
      <input className="block border p-2 my-2" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input className="block border p-2 my-2" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button className="bg-green-600 text-white p-2" onClick={handleAdd}>Add User</button>
    </div>
  );
}

export default AddUser;
