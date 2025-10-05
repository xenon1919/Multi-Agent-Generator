# 🤖 Multi-Agent Generator

<div align="center">

[![PyPI version](https://badge.fury.io/py/multi-agent-generator.svg)](https://pypi.org/project/multi-agent-generator/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Transform plain English into fully configured multi-agent AI systems**

*No coding required • Multiple frameworks • Enterprise-ready*

</div>

---

## ✨ What is Multi-Agent Generator?

Multi-Agent Generator is a powerful tool that converts natural language descriptions into production-ready multi-agent AI systems. Simply describe what you need in plain English, and get fully functional code for popular AI frameworks.

### 🎯 Key Benefits
- **Zero Coding Required**: Describe your needs in natural language
- **Multiple AI Frameworks**: Support for CrewAI, LangGraph, ReAct, and more
- **Enterprise Ready**: Works with OpenAI, IBM WatsonX, Google Gemini, and other providers
- **Modern UI**: Beautiful Streamlit interface with real-time preview
- **Production Ready**: Generate clean, documented, runnable code

---

## 🚀 Features

### 🔧 Supported Frameworks
- **CrewAI**: Role-playing autonomous agents with specialized tasks
- **CrewAI Flow**: Event-driven workflows with state management
- **LangGraph**: Stateful multi-actor applications with graph-based execution
- **ReAct**: Reasoning + Acting agents with tool integration

### 🌐 LLM Provider Support
- **OpenAI**: GPT-4, GPT-3.5 models
- **Google Gemini**: Gemini 2.5 Flash with multimodal capabilities
- **IBM WatsonX**: Enterprise-grade Llama and Granite models
- **Anthropic**: Claude models (via LiteLLM)
- **Ollama**: Local model execution
- **And more**: Any provider supported by LiteLLM

### 💻 Multiple Interfaces
- **Streamlit Web UI**: Interactive, visual interface
- **Command Line**: Scriptable automation
- **Python API**: Programmatic integration

---

## 📦 Installation

```bash
pip install multi-agent-generator
```

### 🔧 Quick Setup

1. **Install the package**:
   ```bash
   pip install multi-agent-generator
   ```

2. **Set up your API key** (choose one):
   ```bash
   # For OpenAI
   export OPENAI_API_KEY="your-openai-key"
   
   # For Google Gemini
   export GEMINI_API_KEY="your-gemini-key"
   
   # For IBM WatsonX
   export WATSONX_API_KEY="your-watsonx-key"
   export WATSONX_PROJECT_ID="your-project-id"
   ```

3. **Start the web interface**:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🎮 Usage

### 🌐 Web Interface (Recommended)

Launch the beautiful Streamlit interface:

```bash
streamlit run streamlit_app.py
```

Then:
1. Select your LLM provider (OpenAI, Gemini, WatsonX)
2. Choose a framework (CrewAI, LangGraph, ReAct)
3. Describe your needs in plain English
4. Generate and download your agent system!

### 💻 Command Line Interface

**Basic Usage:**
```bash
multi-agent-generator "I need a research assistant" --framework crewai
```

**With Gemini:**
```bash
multi-agent-generator "Build a customer support team" --framework crewai --provider gemini
```

**Save to file:**
```bash
multi-agent-generator "Data analysis team" --framework langgraph --output my_agents.py
```

**JSON configuration only:**
```bash
multi-agent-generator "Content creation team" --framework react --format json
```

---

## 💡 Examples

### 🔬 Research Assistant
```
"I need a research assistant that summarizes papers and answers questions"
```
**Generates**: Multi-agent system with research specialist, data collector, and report writer.

### 📱 Social Media Team
```
"I need a team to create viral social media content and manage our brand presence"
```
**Generates**: Content creators, social media managers, and brand strategists working together.

### 📊 Data Analysis Pipeline
```
"Build me a team to analyze customer data and create visualizations"
```
**Generates**: Data analysts, visualization specialists, and insight generators.

### 🎯 Customer Support System
```
"Create a customer support workflow that handles inquiries and escalates complex issues"
```
**Generates**: Support agents, escalation managers, and knowledge base specialists.

---

## 🛠️ Framework Details

| Framework | Best For | Key Features |
|-----------|----------|--------------|
| **CrewAI** | Role-based teams | Specialized agents with clear roles and responsibilities |
| **CrewAI Flow** | Complex workflows | Event-driven processes with state management |
| **LangGraph** | Stateful applications | Graph-based execution with conditional routing |
| **ReAct** | Tool-using agents | Reasoning + Acting with external tool integration |

---

## 🌐 Supported LLM Providers

| Provider | Models | Best For | Setup |
|----------|--------|----------|-------|
| **OpenAI** | GPT-4, GPT-3.5 | General purpose, high quality | `OPENAI_API_KEY` |
| **Google Gemini** | Gemini 2.5 Flash | Multimodal, fast responses | `GEMINI_API_KEY` |
| **IBM WatsonX** | Llama-3, Granite | Enterprise, compliance | `WATSONX_API_KEY` + `WATSONX_PROJECT_ID` |
| **Anthropic** | Claude | Safety-focused | Via LiteLLM |
| **Ollama** | Local models | Privacy, offline | Local installation |

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.



---

## ⭐ Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs or requesting features
- 🔄 Sharing with the AI community

**Made with ❤️ for the AI community**
