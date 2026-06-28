import "../styles/processing.css";

export default function Processing({ status }) {

    if (status === "idle") return null;

    if (status === "completed") return null;

    if (status === "error") return null;

    return (

        <section className="section">

            <div className="container">

                <div className="processing-card">

                    <div className="loader"></div>

                    <h2>

                        {status === "uploading"
                            ? "Uploading Thermal Image..."
                            : "Running AI Model..."}

                    </h2>

                    <p>

                        Please wait while IRVision processes
                        your satellite image.

                    </p>

                </div>

            </div>

        </section>

    );

}