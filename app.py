import streamlit as st
import google.generativeai as genai
import json

# --- Setup and Configuration ---

def setup_ui():
    """
    Configures the Streamlit page and sidebar.
    """
    st.set_page_config(page_title="CulturaX", page_icon="✨")
    st.title("CulturaX")
    
    with st.sidebar:
        st.header("API Configuration")
        st.write("API keys are securely loaded from `st.secrets`.")
        
        # Check if keys are available and display a status
        if "gemini_api_key" in st.secrets and "qloo_api_key" in st.secrets:
            st.success("API keys loaded successfully!")
        else:
            st.warning("API keys not found in `st.secrets`. Please set them up.")
            st.info("To use this app, you need to add your API keys to a `secrets.toml` file or through the Streamlit Cloud UI.")


def initialize_gemini(gemini_api_key):
    """
    Initializes the Gemini model using the provided API key.
    """
    if not gemini_api_key:
        st.warning("Gemini API key is not set. Please add it to your secrets.")
        return None
    try:
        genai.configure(api_key=gemini_api_key)
        # Use a model that is suitable for general text generation
        return genai.GenerativeModel('gemini-2.5-flash')
    except Exception as e:
        st.error(f"Failed to configure Gemini API: {e}")
        return None

# --- API Interaction Functions ---

def get_qloo_insights(qloo_api_key, user_query):
    """
    Makes a hypothetical call to the Qloo API to get taste insights.
    
    NOTE: This is a simplified mock-up. A real Qloo API call would be more complex.
    
    Args:
        qloo_api_key (str): The user's Qloo API key.
        user_query (str): The user's input.
        
    Returns:
        dict: A dictionary of mock insights or an error message.
    """
    if not qloo_api_key:
        return {"error": "Qloo API key is missing. The Gemini model will provide a general response."}

    # Simulating a response based on keywords.
    if "coffee" in user_query.lower():
        return {
            "insights": "Consumers who like coffee also show high affinity for jazz music, independent bookstores, and minimalist design.",
            "affinity_score": 85,
            "trends": "The trend for artisanal, single-origin coffee is on the rise, especially among the 25-34 age demographic."
        }
    elif "travel" in user_query.lower():
        return {
            "insights": "Consumers interested in travel often have high affinities for outdoor activities, photography, and documentary films.",
            "affinity_score": 92,
            "trends": "Sustainable and eco-friendly travel options are gaining significant popularity across all age groups."
        }
    else:
        return {
            "insights": "No specific Qloo insights found for this query. The Gemini model will provide a general response.",
            "affinity_score": 0,
            "trends": "General trends are not available for this query."
        }
        
def get_gemini_response(model, combined_prompt):
    """Generates a response from the Gemini model."""
    if not model:
        return "Gemini model not initialized. Please check your API key."
    
    try:
        # The prompt is a single string that combines user input and Qloo insights
        response = model.generate_content(combined_prompt)
        return response.text
    except Exception as e:
        st.error(f"Gemini API call failed: {e}")
        return None

# --- Main Application Logic ---

def main():
    """Runs the Streamlit chatbot application."""
    
    setup_ui()
    
    # Retrieve API keys from st.secrets and store them in session state
    st.session_state.gemini_api_key = st.secrets.get("gemini_api_key")
    st.session_state.qloo_api_key = st.secrets.get("qloo_api_key")
    
    # Ensure chat history is initialized in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Add a welcome message if the session is new
    if not st.session_state.messages:
        welcome_message = {
            "role": "assistant",
            "content": "Hello! I'm a chatbot powered by Gemini and Qloo. Tell me what's on your mind and I can give you a response with consumer insights."
        }
        st.session_state.messages.append(welcome_message)
    
    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Initialize the Gemini model
    model = initialize_gemini(st.session_state.gemini_api_key)
    
    # Handle new user input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to the chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Get Qloo insights based on the user's prompt
        qloo_insights = get_qloo_insights(st.session_state.qloo_api_key, prompt)

        # Construct a combined prompt for Gemini
        combined_prompt = f"""
        User Query: "{prompt}"
        
        Qloo Consumer Insights:
        {json.dumps(qloo_insights, indent=2)}
        
        Please act as an expert marketing analyst. Use the provided Qloo insights to inform your response.
        Address the user's query and explain the insights in a clear, easy-to-understand way.
        """
        
        # Get response from Gemini
        response = get_gemini_response(model, combined_prompt)
        
        # Display the response
        if response:
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()