## 🦜🔗 LangChain

[LangChain](https://www.langchain.com/) is an open-source framework for building applications powered by large language models (LLMs). Instead of calling a model API directly, LangChain gives you reusable building blocks to connect LLMs with your own data, tools, and logic.

### Why use it?
LLMs on their own don't know your private data, can't take actions, and forget past context. LangChain helps solve this by providing:

- **Model integrations:** a common interface for many providers (OpenAI, Anthropic, Google, open-source models via Hugging Face or Ollama), so you can swap models easily.
- **Prompt templates:** reusable, parameterized prompts instead of hardcoded strings.
- **Chains (LCEL):** compose steps such as prompt → model → output parser into one pipeline.
- **Retrieval (RAG):** load documents, split them into chunks, embed them, store them in a vector database (FAISS, Chroma, Pinecone), and retrieve relevant context for the model.
- **Agents and tools:** let the LLM decide which tools to call (search, calculators, APIs, databases).
- **Memory:** keep conversation history across turns.

### Related tools
- **LangGraph:** build stateful, multi-step agent workflows as graphs.
- **LangSmith:** trace, debug, and evaluate LLM applications.

### Installation
```bash
pip install langchain langchain-openai
```

### Quick example
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words.")
model = ChatOpenAI(model="gpt-4o-mini")  # needs OPENAI_API_KEY set
chain = prompt | model | StrOutputParser()

print(chain.invoke({"topic": "retrieval-augmented generation"}))
```

### How it's used in this project
<!-- Replace with your own details, for example: -->
- Loaded and chunked documents using LangChain document loaders and text splitters
- Stored embeddings in a FAISS / Chroma vector store
- Built a RAG pipeline to answer questions grounded in the documents

### Resources
- [LangChain documentation](https://python.langchain.com/)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
