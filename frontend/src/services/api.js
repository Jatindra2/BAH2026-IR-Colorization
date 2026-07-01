import axios from "axios";

const API = axios.create({
  baseURL: "https://bah2026-ir-colorization.onrender.com",
  timeout: 60000,
});

export async function uploadImage(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await API.post("/predict", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
}

export default API;
