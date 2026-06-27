export default function Loader() {
    return (
        <div className="flex flex-col items-center mt-10">

            <div className="w-16 h-16 border-4 border-cyan-400 border-t-transparent rounded-full animate-spin"></div>

            <p className="mt-5 text-white text-lg">
                Running AI inference...
            </p>

        </div>
    );
}