import { useState } from "react";
import axios from "axios";

function FileUpload() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const form = new FormData();
    form.append("file", file);
    const res = await axios.post("http://localhost:8000/upload", form);
    alert(`File uploaded. Risk: ${res.data.risk}`);
  };

  return (
    <div className="my-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button className="bg-purple-500 text-white p-2 ml-2" onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default FileUpload;
