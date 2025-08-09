# import packages
from dotenv import load_dotenv
from google import genai
import streamlit as st

@st.cache_data
def get_response(user_prompt, temperature):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt,
        config=genai.types.GenerateContentConfig(
            temperature=temperature
        )
    )
    return response

# load environment variables from .env file
load_dotenv()

client = genai.Client()

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# Add a text input box for the user prompt
user_prompt = st.text_input("Enter your prompt", "Explain generative AI in one sentence.")

# Add a slider for temperature
temperature = st.slider(
    "Model temperature:",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.01,
    help="Controls randomness: 0 = deterministic, 1 = very creative"
    )

with st.spinner("Calling Gemini.."):
    response = get_response(user_prompt=user_prompt, temperature=temperature)
    st.write(response.text)