# 🤖 AIVerse - Multi-AI Agent Platform

<div align="center">

### _One Window. 6 Perspectives._

[![Python Version](https://img.shields.io/badge/python-3.11.9-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Get intelligent responses from 6 different AI models simultaneously! Compare perspectives from DeepSeek, OpenAI GPT, Google Gemini, Meta Llama, Alibaba Qwen, and Moonshot Kimi K2 - all in one unified interface.

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**AIVerse** is a cutting-edge multi-agent AI platform that leverages the power of 6 different state-of-the-art language models to provide diverse, comprehensive answers to your questions. By running all agents in parallel, you get instant access to multiple AI perspectives in seconds.

### Why AIVerse?

- **🔄 Multiple Perspectives**: Compare responses from 6 different AI models
- **⚡ Parallel Processing**: All agents run simultaneously using ThreadPoolExecutor
- **🛠️ Tool-Enabled Agents**: Each agent has access to weather, currency conversion, web search, and calculator tools
- **💻 Dual Interface**: Choose between beautiful Streamlit web UI or CLI
- **📥 Export Responses**: Download any agent's response in Markdown format
- **🎨 Modern UI**: Clean, gradient-styled interface with real-time progress tracking

---

### Agent Capabilities

Each AI agent has access to these tools:

- 🌤️ **Weather Information**: Get current weather for any location
- 💱 **Currency Conversion**: USD to INR conversion
- 🔍 **Web Search**: Real-time information retrieval via Google Serper API
- 🧮 **Calculator**: Mathematical calculations

---

## 🎬 Demo

### Web Interface (Streamlit)

```bash
streamlit run app.py
```

### CLI Interface

```bash
python main.py
```

### Sample Output

```
Enter your query: What's the weather in New York and convert 100 USD to INR?

DeepSeek Agent Response:
The current temperature in New York is 5°C with Partly cloudy.
100 USD is equal to 8,350 INR.

OpenAI Agent Response:
New York weather: 5°C, partly cloudy conditions.
Currency: $100 = ₹8,350

[... responses from other agents ...]
```

---

## 🛠️ Tech Stack

| Category          | Technology                                 |
| ----------------- | ------------------------------------------ |
| **Language**      | Python 3.11.9                              |
| **Web Framework** | Streamlit                                  |
| **AI Framework**  | LangChain                                  |
| **AI Models**     | Ollama, Groq, Google Gemini                |
| **Concurrency**   | ThreadPoolExecutor                         |
| **APIs**          | WeatherAPI, CurrencyAPI, Google Serper API |
| **Environment**   | python-dotenv                              |

---

## 📦 Installation

### Prerequisites

- Python 3.11.9 or higher
- pip package manager
- Active internet connection
- API keys (see Configuration section)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/aiverse.git
cd aiverse
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Ollama (for Local Models)

Download and install Ollama from [ollama.ai](https://ollama.ai)

```bash
# Pull required models
ollama pull deepseek-v3.1:671b-cloud
ollama pull gpt-oss:120b-cloud
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Weather API
WEATHER_API_KEY=your_weatherapi_key_here

# Currency API
CURRENCY_API_KEY=your_currencyapi_key_here

# Google Serper API (for web search)
SERPER_API_KEY=your_serper_api_key_here

# Groq API (for Llama, Qwen, Kimi models)
GROQ_API_KEY=your_groq_api_key_here

# Google AI API (for Gemini)
GOOGLE_API_KEY=your_google_api_key_here
```

### API Key Sources

| API           | Get Key From                                  | Free Tier  |
| ------------- | --------------------------------------------- | ---------- |
| WeatherAPI    | [weatherapi.com](https://www.weatherapi.com/) | ✅ Yes     |
| CurrencyAPI   | [currencyapi.com](https://currencyapi.com/)   | ✅ Yes     |
| Google Serper | [serper.dev](https://serper.dev/)             | ✅ Limited |
| Groq          | [console.groq.com](https://console.groq.com/) | ✅ Yes     |
| Google AI     | [ai.google.dev](https://ai.google.dev/)       | ✅ Yes     |

---

## 🚀 Usage

### Option 1: Streamlit Web Interface (Recommended)

```bash
streamlit run app.py
```

1. Open browser at `http://localhost:8501`
2. Enter your question in the input field
3. Click **SUBMIT**
4. Watch as all 6 agents process your query in parallel
5. View responses in individual tabs
6. Download any response using the download buttons

### Option 2: CLI - Parallel Execution

```bash
python main.py
```

All 6 agents run in parallel and display results as they complete.

### Option 3: CLI - Sequential Execution

```bash
python sequential_main.py
```

Agents run one after another (slower but more predictable).

---

## 📁 Project Structure

```
AiVERSE_2.0/
│
├── app.py                  # Streamlit web application
├── main.py                 # CLI with parallel execution
├── sequential_main.py      # CLI with sequential execution
├── agents.py               # Agent configuration and initialization
├── tools.py                # LangChain tool definitions
├── google_client.py        # Google Gemini client wrapper
│
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
└── __pycache__/           # Python cache files
```

---

## 🏗️ Architecture

### System Flow

```
User Query
    ↓
ThreadPoolExecutor (6 parallel threads)
    ├── DeepSeek Agent (Ollama) ──→ Tools (Weather, Currency, Search, Calculator)
    ├── OpenAI Agent (Ollama) ────→ Tools (Weather, Currency, Search, Calculator)
    ├── Qwen Agent (Groq) ────────→ Tools (Weather, Currency, Search, Calculator)
    ├── Llama Agent (Groq) ───────→ Tools (Weather, Currency, Search, Calculator)
    ├── Kimi Agent (Groq) ────────→ Tools (Weather, Currency, Search, Calculator)
    └── Gemini Agent (Google) ────→ Direct API call
    ↓
Aggregate Responses
    ↓
Display in UI/CLI
```

### Agent Architecture

Each LangChain agent follows this pattern:

```python
create_agent(
    model="provider:model_name",
    system_prompt="You are a helpful assistant...",
    tools=[weather, currency, web_search, calculator]
)
```

### Parallel Processing

Using `concurrent.futures.ThreadPoolExecutor`:

- All 6 agents execute simultaneously
- Responses collected as they complete
- Progress tracked in real-time
- Error handling per agent (failures don't block others)

---

## 🔌 API Integrations

### 1. Ollama (Local Models)

- **Models**: DeepSeek V3.1, OpenAI GPT-OSS
- **Setup**: Install Ollama desktop app
- **Endpoint**: `http://localhost:11434`

### 2. Groq Cloud

- **Models**: Llama 3.3, Qwen 3, Kimi K2
- **Speed**: Ultra-fast inference
- **Free Tier**: Generous limits

### 3. Google Gemini

- **Model**: Gemma 3 27B IT
- **Direct API**: Google AI Studio

### 4. Weather Data

- **Provider**: WeatherAPI.com
- **Endpoint**: `api.weatherapi.com/v1/current.json`

### 5. Currency Conversion

- **Provider**: CurrencyAPI.com
- **Endpoint**: Real-time USD to INR rates

### 6. Web Search

- **Provider**: Google Serper API
- **Feature**: Real-time search results

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "Module not found" error

```bash
pip install -r requirements.txt
```

#### 2. Ollama models not responding

```bash
# Check Ollama is running
ollama list

# Pull models if missing
ollama pull deepseek-v3.1:671b-cloud
ollama pull gpt-oss:120b-cloud
```

#### 3. API key errors

- Verify all keys in `.env` file
- Check API key validity on provider websites
- Ensure no trailing spaces in keys

#### 4. Streamlit not opening

```bash
# Specify port manually
streamlit run app.py --server.port 8501
```

#### 5. Import errors for LangChain

```bash
pip install --upgrade langchain langchain-community
```

---

## 🗺️ Roadmap

### Upcoming Features

- [ ] Response comparison and summary view
- [ ] Token usage and cost tracking
- [ ] Response caching for repeated queries
- [ ] User authentication and history
- [ ] More AI models (Anthropic Claude, Mistral, etc.)
- [ ] Custom tool creation interface
- [ ] API endpoint for programmatic access
- [ ] Docker containerization
- [ ] Response quality voting system
- [ ] Export all responses to PDF

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

<div align="center">

---

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ by Yashodeep**

[Back to Top](#-aiverse---multi-ai-agent-platform)

</div>
