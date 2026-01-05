# 🤖 AIVerse

<div align="center">

**One Window. 6 Perspectives.**

A multi-AI agent platform that provides answers from 6 different AI models simultaneously, giving you diverse perspectives on any question.

[![Python Version](https://img.shields.io/badge/python-3.11.9-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/crewai-latest-orange.svg)](https://www.crewai.com/)

</div>

---

## 🌟 Overview

AIVerse is an innovative multi-agent AI platform that leverages the power of 6 different state-of-the-art language models to answer your queries. Each AI agent processes your question independently, providing unique insights and perspectives.

### Why AIVerse?

- **🔍 Multiple Perspectives**: Get 6 different viewpoints on any question
- **🤖 Diverse AI Models**: Compare responses from DeepSeek, OpenAI, Gemini, Llama, Qwen, and Kimi K2
- **⚡ Simultaneous Processing**: All agents work in sequence to provide comprehensive answers
- **📊 Easy Comparison**: View all responses in organized tabs
- **💾 Export Results**: Download individual responses as markdown files

---

## 🎯 Supported AI Models

| AI Model | Provider | Version |
|----------|----------|---------|
| 🔷 **DeepSeek** | Ollama | V3.1 671B Cloud |
| 🟢 **OpenAI GPT** | Ollama | OSS 120B Cloud |
| 🔵 **Google Gemini** | Google AI | 2.5 Flash |
| 🦙 **Meta Llama** | Groq | 3.3 70B Versatile |
| 🟣 **Alibaba Qwen** | Groq | Qwen 3 32B |
| 🌙 **Moonshot Kimi K2** | Groq | K2 Instruct |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11.9** or higher
- **Ollama** (for local models like DeepSeek and OpenAI GPT)
- **API Keys** for:
  - Google Gemini (via Google AI Studio)
  - Groq (for Llama, Qwen, and Kimi K2)

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AIVerse.git
cd AIVerse
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.\.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
# Google Gemini API Key
GOOGLE_API_KEY=your_google_api_key_here

# Groq API Key
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Install Ollama Models

Make sure Ollama is running, then pull the required models:

```bash
ollama pull deepseek-v3.1:671b-cloud
ollama pull gpt-oss:120b-cloud
```

---

## Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Run via Python Script

```bash
python main.py
```

This will execute the crew with the predefined query in `main.py`.

---

## 📁 Project Structure

```
AIVerse/
│
├── app.py                      # Streamlit web interface
├── main.py                     # Command-line execution script
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
│
├── src/
│   ├── __init__.py
│   ├── crew.py                # AIVerse crew definition
│   └── config/
│       ├── agents.yaml        # Agent configurations
│       └── tasks.yaml         # Task definitions
│
└── outputs/                   # AI responses saved here
    ├── deepseek-task.md
    ├── openai-gpt-task.md
    ├── google-gemini-task.md
    ├── meta-llama3-task.md
    ├── alibaba-qwen-task.md
    └── kimi-k2-task.md
```

---

## ⚙️ Configuration

### Modifying Agents

Edit `src/config/agents.yaml` to customize agent behavior, roles, and models.

### Modifying Tasks

Edit `src/config/tasks.yaml` to change task descriptions and expected outputs.

### Changing the Query

**For Web App**: Simply enter your question in the text area.

**For CLI**: Edit the `inputs` dictionary in `main.py`:

```python
inputs = {
    "query": "Your question here",
}
```

---

## Customization

### Add More Agents

1. Add agent configuration in `src/config/agents.yaml`
2. Add task configuration in `src/config/tasks.yaml`
3. Create agent and task methods in `src/crew.py`
4. Update `app.py` to include the new agent tab

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) - Multi-agent orchestration framework
- [Streamlit](https://streamlit.io/) - Web interface framework
- [Ollama](https://ollama.ai/) - Local LLM hosting
- [Groq](https://groq.com/) - Fast AI inference
- [Google AI](https://ai.google.dev/) - Gemini API

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

<div align="center">

**Made with ❤️ by AIVerse Team**

⭐ Star this repo if you find it helpful!

</div>
