import os

import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


def initialize_session_state():
    """
    Initialize the session state variables if they don't exist.
    """
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'model' not in st.session_state:
        st.session_state.model = 'llama3-70b-8192'
    if 'programming_language' not in st.session_state:
        st.session_state.programming_language = 'Python'
    if 'style_guide' not in st.session_state:
        st.session_state.style_guide = 'PEP 8'


def display_customization_options():
    """
    Add customization options to the sidebar for model selection, memory length, programming language, and style guide.
    """
    st.sidebar.title('Customization')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant','gemma2-9b-it', 'llama3-70b-8192'],
        key='model_selectbox'
    )
    programming_language = st.sidebar.selectbox(
        'Programming Language',
        ['Python', 'R', 'Java', 'JavaScript']
    )

    style_guide_options = {
        'Python': ['PEP 8', 'Google Python Style Guide'],
        'R': ['Google R Style Guide', 'Tidyverse Style Guide'],
        'Java': ['Google Java Style Guide', 'Oracle Java Code Conventions'],
        'JavaScript': ['Airbnb JavaScript Style Guide', 'Google JavaScript Style Guide']
    }
    style_guide = st.sidebar.selectbox(
        'Style Guide',
        style_guide_options[programming_language]
    )

    return model, programming_language, style_guide


def initialize_groq_chat(groq_api_key, model):
    """
    Initialize the Groq Langchain chat object.
    """
    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )


def initialize_conversation(groq_chat, memory):
    """
    Initialize the conversation chain with the Groq chat object and memory.
    """
    return ConversationChain(
        llm=groq_chat,
        memory=memory
    )


def process_user_code(user_code, conversation, programming_language, style_guide):
    """
    Process the user's code and generate a response using the conversation chain.
    """
    prompt = f"Please rewrite the provided {programming_language} code to adhere strictly to the {style_guide} standards. Ensure the output consists solely of the revised code, enclosed within triple backticks for easy copy-paste, without specifying the programming language on the first line:\n\n{user_code}. Please ensure that the output only consists of the revised code within triple backticks, as this is very important!"
    response = conversation(prompt)
    message = {'human': prompt, 'AI': response['response']}
    st.session_state.chat_history.append(message)


def main():
    """
    The main entry point of the application.
    """
    groq_api_key = os.environ['GROQ_API_KEY']
    initialize_session_state()
    st.title("Lightning ⚡️ Code Style Guide Assistant & Code Translator")
    st.markdown("Get your code rewritten according to popular style guides by Lightning, an ultra-fast AI chatbot powered by Groq LPUs!!")

    model, programming_language, style_guide = display_customization_options()

    if st.session_state.model != model or st.session_state.programming_language != programming_language or st.session_state.style_guide != style_guide:
        # Reset chat history and session state when the model, programming language, or style guide is switched
        st.session_state.chat_history = []
        st.session_state.model = model
        st.session_state.programming_language = programming_language
        st.session_state.style_guide = style_guide
        st.rerun()

    memory = ConversationBufferWindowMemory(k=1)

    st.divider()

    user_code = st.text_area("Enter your code:")
    if user_code:
        st.session_state.chat_history.append({"human": user_code, "AI": ""})

        with st.expander("Original Code"):
            st.code(user_code, language=programming_language.lower())

        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

        groq_chat = initialize_groq_chat(groq_api_key, model)
        conversation = initialize_conversation(groq_chat, memory)
        process_user_code(user_code, conversation, programming_language, style_guide)

        with st.expander("Rewritten Code"):
            response = conversation(user_code)
            ai_response = response['response']

            # Extract the code within triple backticks
            code_start = ai_response.find('```') + 3
            code_end = ai_response.find('```', code_start)
            code = ai_response[code_start:code_end]

            # Extract the text before and after the code
            text_before_code = ai_response[:code_start-3].strip()
            text_after_code = ai_response[code_end+3:].strip()

            # Display the text and code separately
            st.write(text_before_code)
            st.code(code, language=programming_language.lower())
            st.write(text_after_code)

            st.session_state.chat_history[-1]["AI"] = response['response']


if __name__ == "__main__":
    main()