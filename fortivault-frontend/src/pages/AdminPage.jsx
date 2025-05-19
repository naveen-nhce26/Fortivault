import AddUser from "../components/AdminPanel/AddUser";
import ManageUsers from "../components/AdminPanel/ManageUsers";

function AdminPage() {
  return (
    <div className="p-6">
      <h1 className="text-2xl">Admin Panel</h1>
      <AddUser />
      <ManageUsers />
    </div>
  );
}

export default AdminPage;
