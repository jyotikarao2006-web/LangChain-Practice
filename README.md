#  LangChain Practice

A collection of hands-on mini-projects for learning and experimenting with the LangChain framework. Each folder in this repository is a self-contained example exploring a different LangChain concept, from agent tools to prompt-based content generation.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![LangChain](https://img.shields.io/badge/Framework-LangChain-1C3C3C)
![LLM](https://img.shields.io/badge/Powered%20by-LLMs-orange)

---

## Overview

This repository is a practice space for building applications with LangChain. Rather than one single app, it's organized as a set of small, focused projects, each demonstrating a specific capability of the framework, such as using tools with agents, generating structured content, and summarizing text.

---

## Project Structure

```
LangChain-Practice/
├── Agent_Tools/                   # Examples of building and using tools with LangChain agents
├── restaurent_menue_generator/    # LLM-powered restaurant menu generator
└── sumarrize_article/             # Article summarization using LangChain
```

---

## Modules

### Agent_Tools
Explores how LangChain agents can be equipped with tools to extend their capabilities beyond plain text generation, allowing them to take actions, look up information, or call functions as part of reasoning through a task.

### restaurent_menue_generator
A project that uses an LLM through LangChain to generate restaurant menu ideas, likely combining prompt templates with structured output generation.

### sumarrize_article
A LangChain-based example that takes an article as input and produces a condensed summary using an LLM chain.

---

## Tech Stack

| Component     | Technology         |
|---------------|---------------------|
| Language      | Python              |
| Framework     | LangChain           |
| LLM Provider  | OpenAI / other LangChain-supported models |

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- An API key for your chosen LLM provider (e.g. OpenAI)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jyotikarao2006-web/LangChain-Practice.git
   cd LangChain-Practice
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install langchain openai python-dotenv
   ```

4. **Set your API key**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run a specific module**
   Navigate into the folder you want to try and run its script or notebook, for example:
   ```bash
   cd sumarrize_article
   python main.py
   ```

---

## Learning Outcomes

Working through this repository covers:

- Core LangChain concepts: chains, prompts, and models
- Building and integrating tools with LangChain agents
- Using LLMs for structured content generation
- Text summarization pipelines with LangChain

---

## Future Improvements

- [ ] Add a top-level requirements.txt covering all modules
- [ ] Add usage instructions and sample output for each sub-project
- [ ] Add a unified CLI or notebook index to run any module easily
- [ ] Expand with more LangChain concepts (memory, retrieval-augmented generation, chat history)

---

## Contributing

Contributions are welcome. Feel free to fork this repo, open an issue, or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project currently has no license specified. Consider adding one (e.g. MIT) if you plan to share or accept contributions.

---

## Author

Built by [jyotikarao2006-web](https://github.com/jyotikarao2006-web) while learning to build LLM-powered applications with LangChain.
