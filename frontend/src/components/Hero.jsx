function Hero() {
  const scrollToUpload = () => {
    document
      .getElementById("upload")
      .scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="hero">

      <h1 className="hero-title">

        <span className="line1">
          Everything You Upload,
        </span>

        <br />

        <span className="line2">
          Ready to Answer.
        </span>

      </h1>

      <p className="hero-subtitle">

        Upload your PDFs, DOCX, PPTs, websites, and YouTube videos
        and get intelligent answers instantly with AI.

      </p>

      <button
        className="hero-btn"
        onClick={scrollToUpload}
      >
        Get Started
      </button>

    </section>
  );
}

export default Hero;