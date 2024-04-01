from langchain.text_splitter import RecursiveCharacterTextSplitter


def text_chunker(input_text: str, ops: dict) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=ops.get('size'),
        chunk_overlap=ops.get('overlap'),
        length_function=len
    )

    chunks = text_splitter.split_text(text=input_text)

    return chunks
