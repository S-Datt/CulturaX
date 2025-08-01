CulturaX: A Generative AI Chatbot for Personalized Consumer Insights
🚀 Live Demo
[View the live application here!](https://culturax-mpq4vqtzks9kfs6866m7ah.streamlit.app/)
✨ Inspiration

We saw a critical gap in a market filled with generic information. Existing tools offer one-size-fits-all data, failing to provide the personalized insights users truly need. CulturaX was created to fill this void, combining consumer insights with generative AI to help people make smarter decisions.
💡 Features

    Personalized Insights: Tailors consumer insights by analyzing user queries.

    Dynamic Response Generation: Leverages the Gemini API to generate context-aware, human-like responses.

    Intuitive Interface: Built on Streamlit for a simple and user-friendly chat experience.

    Secure API Handling: Integrates with st.secrets to ensure API keys are never exposed.

💻 Tech Stack

Technologies Used

    Streamlit

    Python

    Gemini API

    Libraries: google-generativeai, json

    Deployment: Streamlit Community Cloud

🔧 How to Run Locally

    Clone the repository:

    git clone https://github.com/your-username/culturaX.git
    cd culturaX



    Create a virtual environment:

    python -m venv venv



    Activate the virtual environment:

        macOS / Linux:

        source venv/bin/activate



        Windows:

        venv\Scripts\activate



    Install dependencies:

    pip install -r requirements.txt



    Set up your secrets:
    Create a folder named .streamlit and a file inside it named secrets.toml.

    # .streamlit/secrets.toml
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"



    Run the app:

    streamlit run app.py



🚧 Challenges and Learnings

    Challenge: Seamlessly integrating the Gemini API and ensuring that its responses were consistently relevant and informed by the mock consumer insights.

    Solution: We addressed this by carefully crafting the prompt to the Gemini model, explicitly instructing it to act as an expert marketing analyst and to use the provided insights as its primary source of truth.

    Learning: This project reinforced the critical importance of prompt engineering and structured data handling when building AI-powered applications.

🎯 Future Improvements

    Multi-user authentication: Implement a system to allow multiple users to have personalized, persistent experiences.

    Advanced data visualizations: Enhance the insights by adding charts and graphs to visually represent trends and affinities.

    UI/UX improvements: Continuously refine the user interface based on feedback to provide a more intuitive and engaging experience.

🔒 Privacy Considerations

    User Data Protection: CulturaX is designed to prioritize user privacy by minimizing data collection. Personal information is not stored unless explicitly required for functionality, and users are informed about any data usage.

    Data Encryption: All sensitive data transmitted between the client and server is encrypted using industry-standard protocols to prevent unauthorized access.

    Anonymization: Any data collected for analytics or improvement purposes is anonymized to ensure that individual users cannot be identified.

    Compliance: CulturaX adheres to relevant data protection regulations, such as GDPR and CCPA, ensuring that user rights are respected and upheld.

    User Control: Users have the option to manage their data preferences, including the ability to delete their data or opt out of data collection features.

    Transparency: Clear communication regarding data usage policies is provided to users, ensuring they understand how their information is handle
