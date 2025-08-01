CulturaX: A Generative AI Chatbot for Personalized Consumer Insights

🚀 Live Demo
[View the live application here!](https://culturax-mpq4vqtzks9kfs6866m7ah.streamlit.app/)

✨ Inspiration

We saw a critical gap in a market filled with generic information. Existing tools offer one-size-fits-all data, failing to provide the personalized insights users truly need. CulturaX was created to fill this void, combining consumer insights with generative AI to help people make smarter decisions. 

NLP at its Core: This project is a sophisticated application of Natural Language Processing (NLP), with the Gemini Large Language Model (LLM) at its core, to create a specialized and intelligent chatbot.

Project Overview: A Streamlit web application that acts as an expert analyst in the domains of finance, travelling, and culture. It combines the advanced reasoning of the Gemini large language model with consumer trend insights from a mock Qloo API to provide data-driven and culturally relevant responses. Streamlit allows rapid development of an interactive chatbot that leverages machine learning, enabling seamless integration of AI models and real-time user interactions in an open-source environment.

💡 Features

    Insight-Driven Responses: The Gemini model generates responses that are enriched with consumer insights from the Qloo API.

    Secure API Integration: Uses st.secrets to securely manage API keys.

    Conversational Interface: A modern and responsive chat interface built with Streamlit.

    GDPR-Compliant by Design: The application does not store any personal user data or chat history.

NLP at its Core: This project is a sophisticated application of Natural Language Processing (NLP), with the Gemini Large Language Model (LLM) at its core, to create a specialized and intelligent chatbot.

How It Works

    A user query is received.

    The application calls a mock Qloo API to retrieve pre-defined consumer insights.

    The query and insights are packaged into a single, comprehensive prompt.

    The enhanced prompt is sent to the Gemini large language model.

    Gemini uses the provided insights to generate a detailed, context-aware response.

    The final response is displayed in the chat interface.

💻 Tech Stack

Technologies Used

    Streamlit

    Python

    Gemini API

    Qloo API

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

QLOO_API_KEY =
"YOUR_QLOO_API_KEY_HERE" 

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

    Multi-user Chat History:  Each user would have their own persistent chat history. This would allow a user to come back later and see their past conversations.

    Multi-Model Integration: Explore integrating other models or APIs to expand the chatbot's domain expertise

🔒 Privacy Considerations

    User Data Protection: CulturaX is designed to prioritize user privacy by minimizing data collection. Personal information is not stored unless explicitly required for functionality, and users are informed about any data usage.

    Data Encryption: All sensitive data transmitted between the client and server is encrypted using industry-standard protocols to prevent unauthorized access.

    Anonymization: Any data collected for analytics or improvement purposes is anonymized to ensure that individual users cannot be identified.

    Compliance: CulturaX adheres to relevant data protection regulations, such as GDPR and CCPA, ensuring that user rights are respected and upheld.

    User Control: Users have the option to manage their data preferences, including the ability to delete their data or opt out of data collection features.

    Transparency: Clear communication regarding data usage policies is provided to users, ensuring they understand how their information is handle

    
    🤝 Contribution
"This project is a solo submission by for the Qloo LLM Hackathon." While I am the sole contributor, I welcome new features, bug fixes, and improvements. To contribute, please fork the repository, create a new branch, and submit a pull request with your changes.

📄 License

This project was created for the Qloo LLM Hackathon. This project is licensed under the MIT License.
