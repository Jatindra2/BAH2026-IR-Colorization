export default function UploadCard({ setFile, predict }) {

    return (

        <div className="bg-slate-800 rounded-xl shadow-xl p-10">

            <h2 className="text-2xl text-white font-semibold mb-6">

                Upload Thermal Image

            </h2>

            <input

                type="file"

                accept=".npy"

                onChange={(e) => setFile(e.target.files[0])}

                className="block w-full text-white"

            />

            <button

                onClick={predict}

                className="mt-8 bg-cyan-500 hover:bg-cyan-600 px-8 py-3 rounded-lg text-white font-semibold"

            >

                Predict

            </button>

        </div>

    );

}