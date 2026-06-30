import axios from "axios";

const API = axios.create({
    baseURL:
        import.meta.env.VITE_API_URL ||
        "http://127.0.0.1:8000",
    timeout: 60000,
});

export async function uploadImage(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await API.post(
    "/predict",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}

export default API;