from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
import os
os.environ['GOOGLE_API_KEY']="AQ.Ab8RN6JPFVJCDl-596Yha-krhSHlwnlyrLF4Ij28OVfQR5Pbzw"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

def summarize_article(path):
    # Load article
    loader = PyPDFLoader(path)
    docs = loader.load()

    # Split article
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = splitter.split_documents(docs)

    # Combine all chunks
    article = ""

    for doc in split_docs:
        article += doc.page_content + "\n"

    # Create prompt
    prompt = f"""
    Summarize the following article in simple language.
    Article:
    {article}
    """

    # Generate summary
    response = llm.invoke(prompt)

    return response.content