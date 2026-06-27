import { useState } from "react";

import Navbar from "./components/Navbar";
import UploadCard from "./components/UploadCard";
import Loader from "./components/Loader";
import ResultCard from "./components/ResultCard";

import api from "./services/api";

export default function App() {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [image, setImage] = useState(null);

    async function predict() {

        if (!file) {
            alert("Please select a .npy thermal image");
            return;
        }

        setLoading(true);

        const formData = new FormData();
        formData.append("file", file);

        try {

            const response = await api.post(
                "/predict",
                formData,
                {
                    responseType: "blob",
                }
            );

            const url = URL.createObjectURL(response.data);
            setImage(url);

        } catch (err) {

            console.error(err);
            alert("Prediction failed.");

        }

        setLoading(false);
    }

    return (

        <div className="min-h-screen bg-slate-900">

            <Navbar />

            <div className="max-w-4xl mx-auto py-12 px-6">

                <UploadCard
                    setFile={setFile}
                    predict={predict}
                />

                {loading && <Loader />}

                <ResultCard image={image} />

            </div>

        </div>

    );
}