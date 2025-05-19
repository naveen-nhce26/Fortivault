import { useEffect, useState } from "react";
import axios from "axios";

function ManageUsers() {
  const [users, setUsers] = useState([]);

  const loadUsers = async () => {
    const res = await axios.get("http://localhost:8000/admin/users");
    setUsers(res.data);
  };

  const deleteUser = async (id) => {
    await axios.delete(`http://localhost:8000/admin/delete-user/${id}`);
    loadUsers();
  };

  useEffect(() => {
    loadUsers();
  }, []);

  return (
    <div className="p-4">
      <h3 className="text-lg">Manage Users</h3>
      {users.map((u) => (
        <div key={u.id} className="flex justify-between my-1 border p-2">
          <span>{u.username}</span>
          <button className="bg-red-500 text-white px-2" onClick={() => deleteUser(u.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}

export default ManageUsers;
