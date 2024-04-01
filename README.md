# ASK A PDF

This Streamlit-based application question-answering on texts extracted from PDF documents by integrating the [langchain](https://python.langchain.com/docs/get_started/introduction) framework with various language models and utilizing the FAISS library for efficient similarity searches in large vector spaces.A key feature of this application is its support for local model execution using [Ollama](https://ollama.com/), enabling users to process data without relying on external API calls, thus ensuring privacy.

# Features

- PDF text extraction and processing
- Text chunking for efficient processing
- Choice of OpenAI models or local Mistral 7B for inference and LLaMA2 for embeddings via Ollama.
- Saved vector embeddings and search with FAISS

### Running Models Locally with Ollama

To run models locally using Ollama, installation is required. The most straightforward method to install and start Ollama is via its official Docker image. For comprehensive installation instructions, refer to:

- [Ollama's official site](https://ollama.com/) for general installation guidelines.
- [Ollama Docker Image Guide](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image) for specific steps to use the Docker image.

If you have an NVIDIA GPU on your machine, it's highly recommended to leverage it when running Ollama.

> If you opt to use OpenAI models, you _must_ obtain an `OPENAI_API_KEY`. Please visit [OpenAI API Keys](https://platform.openai.com/api-keys) to get your key. Once obtained, ensure to save it in your `.env` file as follows:
>
> ```plaintext
> OPENAI_API_KEY=your_openai_api_key_here
> ```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/rabee05/ask-a-pdf.git
cd ask-a-pdf.git
```

To run the project, first, create a virtual environment. I recommend using Pipenv for its simplicity and effectiveness in managing project dependencies.

> check if Pipenv is installed by running `pipenv --version`. If not found, install Pipenv with:
>
> ```bash
> pip install pipenv --user
> ```

To ensure the virtual environment is created within the project folder, set the following environment variable:

```bash
export PIPENV_VENV_IN_PROJECT=1
```

Now, create a virtual environment and install dependencies by running:

```bash
pipenv install
```

If you prefer to use `venv` for virtual environment management and a `requirements.txt` file for dependencies, follow these steps:

```bash
python3 -m venv .venv
```

On macOS and Linux:

```bash
source .venv/bin/activate
```

Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

To delete the virtual environment, either manually remove the environment directory or run :

```bash
pipenv --rm
```

## Environment Configuration

if you want to run OpenAI models, copy and rename `.env.example` to `.env`:

```
cp .env.example .env
```

Open the `.env` file and include the following information:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### Configuration File Updates

After setting up your project, ensure to review and update the `config/config.py` file to suit your environment, particularly the `OLLAMA_SERVER` settings:

After installing Ollama, check it's running by navigating to http://localhost:11434/ or use the IP address with default port 11434. You should see "Ollama is running".

## Running the Application

To run the application, execute the following command from the project root:

```bash
streamlit run app.py
```

Navigate to the URL provided by Streamlit in your browser to interact with the application.

![App Main Page](https://github.com/rabee05/ask-a-pdf/blob/main/docs/app-main-page.png)
