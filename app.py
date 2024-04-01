import os
import sys
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain_openai.llms import OpenAI
from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings
import streamlit as st
from langchain_community.embeddings.ollama import OllamaEmbeddings
from libs.ui_components import text_from_pdf, load_local_css, setup_sidebar
from libs.text_processor import text_chunker
from config.config import OLLAMA_SERVER, UI, SPLITTER_OPS, DATA_DIR

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'config'))
sys.path.append(os.path.join(project_root, 'libs'))

load_local_css(os.path.join(project_root, UI.get('css_file')))
model_type = setup_sidebar()
load_dotenv()

for dir in DATA_DIR:
    if not (os.path.exists(os.path.join(project_root, DATA_DIR[dir]))):
        os.makedirs(os.path.join(project_root, DATA_DIR[dir]), exist_ok=True)


def main():

    vector_db = None
    embeddings = None
    llm = None
    file_name, input_text = text_from_pdf()
    if input_text and file_name is not None:
        chunks = text_chunker(input_text=input_text, ops=SPLITTER_OPS)

        try:
            store_dir = os.path.join(
                project_root, DATA_DIR.get('vector_stores'))
            store_path = os.path.join(
                store_dir, f"{file_name}_{model_type}.faiss")
            store_name = file_name+'_' + model_type

            if model_type == 'open_ai':
                embeddings = OpenAIEmbeddings()
                llm = OpenAI(temperature=0)
            elif model_type == 'local':
                embeddings = OllamaEmbeddings(
                    base_url=OLLAMA_SERVER.get('base_url')+':' + OLLAMA_SERVER.get('port'), model=OLLAMA_SERVER.get('embedding_model'))
                llm = Ollama(base_url=OLLAMA_SERVER.get(
                    'base_url')+':' + OLLAMA_SERVER.get('port'), model=OLLAMA_SERVER.get('llm_model'),)

            if os.path.exists(store_path):
                local_db = FAISS.load_local(folder_path=store_dir, index_name=store_name,
                                            embeddings=embeddings, allow_dangerous_deserialization=True)
                vector_db = local_db

            else:
                vector_db = FAISS.from_texts(
                    chunks, embedding=embeddings)
                vector_db.save_local(folder_path=store_dir,
                                     index_name=store_name)
            query = st.text_input(
                f"Ask a question to ({file_name}) using {'Open AI' if model_type == 'open_ai' else 'Local model'} "
            )

            if query:
                docs = vector_db.similarity_search(query=query, k=3)
                chain = load_qa_chain(llm=llm, chain_type='stuff')
                res = chain.invoke(
                    {"input_documents": docs, "question": query})
                st.write(res["output_text"])

        except Exception as e:
            error_message = f"{str(e)}"
            st.write(error_message)


if __name__ == '__main__':
    main()
