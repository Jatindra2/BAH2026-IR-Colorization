export default function LoadingOverlay({

    loading,
    currentStep,

}) {

    if (!loading) return null;

    const steps = [

        "Uploading Image",
        "Pre-processing",
        "Super Resolution",
        "AI Colorization",
        "Post Processing",
        "Generating RGB Image",

    ];

    return (

        <div className="loading-overlay">

            <div className="loading-card">

                <div className="loader"></div>

                <h2>Processing Satellite Image</h2>

                <p>Please wait while our AI enhances your thermal image.</p>

                <div className="progress-bar">

                    <div
                        className="progress-fill"
                        style={{
                            width: `${(currentStep / 6) * 100}%`,
                        }}
                    />

                </div>

                <ul>

                    {steps.map((step, index) => (

                        <li
                            key={index}
                            className={
                                currentStep > index
                                    ? "done"
                                    : currentStep === index
                                    ? "active"
                                    : ""
                            }
                        >

                            {step}

                        </li>

                    ))}

                </ul>

            </div>

        </div>

    );

}