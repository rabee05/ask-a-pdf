import streamlit as st
from typing import Tuple
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader

# if pdf is None:
#     raise st.error("No file uploaded. Please upload a PDF file.")


def load_local_css(file_name: str) -> None:
    """
    Loads and applies a local CSS file to a Streamlit application.

    Parameters:
    - file_name (str): The path to the CSS file to be loaded.

    Returns:
    None

    Note:
    The function uses Streamlit's `markdown` method with `unsafe_allow_html=True` to allow HTML content, including CSS, to be rendered. This approach requires careful handling to avoid security risks associated with injecting HTML directly into the app.
    """

    with open(file_name) as f:
        st.markdown(f'<style> {f.read()} </style>', unsafe_allow_html=True)


def setup_sidebar():
    """
    Initializes the sidebar in a Streamlit application, presenting a welcoming message and the application's title.

    Parameters:
    None

    Returns:
    None
    """

    st.header("Welcome to ASK a PDF")
    with st.sidebar:
        st.title('Ask a PDF')
        model_type = st.radio("Choose the model type:",
                              ('OpenAI Models', 'Local Models'))
        st.markdown("""
- **OpenAI Models**: 
    - **Embedding**: `Text-embedding-ada-002-v2`.
    - **LLM**: `GPT-3.5-turbo-instruct`.
        
- **Local Models**: 
    - **Embedding**:`llama2`
    - **LLM**: `Mistral 7B`
""", unsafe_allow_html=True)

        add_vertical_space(1)
        st.write('---')
        st.markdown(
            """
            ## Tools and Frameworks Used
            - [streamlit](https://streamlit.io/)
            - [Ollama](https://ollama.com/), [Ollama Docker Image](https://github.com/ollama/ollama?tab=readme-ov-file)
            - [langchain](https://python.langchain.com/docs/get_started/introduction)
            - [Milvus](https://milvus.io/) to be added
            """
        )
        st.write('---')

        st.write(
            'Created by [Rabee Zyoud](https://www.linkedin.com/in/zyoud/)')

    if model_type == 'OpenAI Models':
        return 'open_ai'
    elif model_type == 'Local Models':
        return 'local'
    return None


def text_from_pdf() -> Tuple[str | None, str | None]:
    """
    Creates and returns a file uploader for PDF files.
    If a PDF is uploaded, extracts text and returns the file name (without extension) and text.
    """
    uploaded_file = st.file_uploader('Upload a PDF file', type='pdf')

    if uploaded_file is not None:
        file_name = uploaded_file.name[:-4]
        pdf_reader = PdfReader(uploaded_file)
        input_text = ""
        for page in pdf_reader.pages:
            input_text += page.extract_text() or ''

        return file_name, input_text
    else:
        return None, None
