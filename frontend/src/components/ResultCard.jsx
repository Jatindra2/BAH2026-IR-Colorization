export default function ResultCard({ image }) {

    if (!image) return null;

    return (

        <div className="mt-10 bg-slate-800 rounded-xl p-6 shadow-xl">

            <h2 className="text-2xl font-semibold text-white mb-5">
                Prediction
            </h2>

            <img
                src={image}
                alt="Prediction"
                className="rounded-lg shadow-lg w-full"
            />

            <a

                href={image}
                download="prediction.png"

                className="mt-5 inline-block bg-cyan-500 hover:bg-cyan-600 text-white px-5 py-3 rounded-lg"

            >
                Download Image
            </a>

        </div>

    );
}