# Multi-Agent Generator
<img width="807" height="264" alt="Screenshot 2025-08-18 at 12 59 52 PM" src="https://github.com/user-attachments/assets/90665135-80a3-43e2-82cc-ae7fa1dcc6a3" />

**[Multi-Agent Generator](https://pypi.org/project/multi-agent-generator/)** is a powerful Python package that transforms plain English instructions into fully configured multi-agent AI workflows. It supports popular frameworks like **CrewAI**, **CrewAI Flow**, **LangGraph**, and **ReAct**, and integrates with LLM providers such as **OpenAI** and **IBM WatsonX**. With a user-friendly command-line interface and an optional **Streamlit-based UI**, it simplifies the creation of complex AI agent teams for tasks like research, content creation, and data analysis.

## Key Features

- **Natural Language Input**: Describe your requirements in plain English, and the generator creates a tailored multi-agent workflow.
- **Supported Frameworks**:
  - **CrewAI**: Orchestrates role-playing AI agents with defined roles and goals.
  - **CrewAI Flow**: Extends CrewAI with event-driven workflows and state management.
  - **LangGraph**: LangChain’s framework for stateful, multi-actor applications using directed graphs.
  - **ReAct**: Combines reasoning and action for adaptive AI agents.
- **LLM Providers**:
  - **OpenAI** (default model: GPT-4o-mini).
  - **IBM WatsonX** (default model: Llama-3-70B-Instruct).
- **New Enhancements**:
  - **Command-Line Process Selection**: Choose between `--process hierarchical` or `--process sequential` to define how agents interact.
  - **Intelligent Defaults**: The LLM automatically recommends the optimal process type (hierarchical or sequential) based on your requirements.
  - **Backward Compatibility**: Existing functionality remains unchanged, with `sequential` as the default process type.
- **Streamlit UI**: A web-based interface for selecting frameworks, providers, process types, and visualizing/downloading generated workflows.
- **Output Options**: Generate Python scripts or JSON configurations for your workflows.
- **Visualizations**: View agent relationships and workflow structures directly in the Streamlit UI.

## Installation

### Prerequisites
- Python 3.9 or higher.
- API keys for your chosen LLM provider:
  - **OpenAI**: Set `OPENAI_API_KEY` as an environment variable.
  - **IBM WatsonX**: Set `WATSONX_API_KEY`, `WATSONX_PROJECT_ID`, and `WATSONX_URL` as environment variables.

### Install via pip
- **Basic Installation** (uses OpenAI by default):
  ```bash
  pip install multi-agent-generator
  ```
- **With IBM WatsonX Support**:
  ```bash
  pip install multi-agent-generator[watsonx]
  ```
- **For Developers** (includes development tools):
  ```bash
  pip install multi-agent-generator[dev]
  ```

## Usage

### Command-Line Interface
Run the `multi-agent-generator` directly from the command line to generate AI agent workflows.

#### Basic Usage
```bash
python -m multi_agent_generator "Create a research team to summarize papers" --framework crewai
```
This generates a CrewAI-based workflow with a sequential process (default).

#### Specify Process Type
- **Hierarchical Process** (agents organized in a hierarchy with a lead agent coordinating tasks):
  ```bash
  python -m multi_agent_generator "Create a research team" --framework crewai --process hierarchical
  ```
- **Sequential Process** (agents execute tasks in a linear sequence):
  ```bash
  python -m multi_agent_generator "Create a research team" --framework crewai --process sequential
  ```

#### Intelligent Process Selection
Let the LLM decide the best process type based on your requirements:
```bash
python -m multi_agent_generator "Create a complex project management system" --framework crewai
```
The LLM analyzes the complexity and nature of the task to recommend either a hierarchical or sequential process.

#### Save Output to a File
```bash
python -m multi_agent_generator "Create a team for viral social media content" --framework langgraph --output social_team.py
```

#### Use with IBM WatsonX
```bash
python -m multi_agent_generator "Analyze customer data and create visualizations" --framework crewai --provider watsonx --process hierarchical
```

### Streamlit UI
Launch the Streamlit-based web interface to interactively design and visualize workflows:
```bash
streamlit run -m multi_agent_generator.streamlit_app.app
```
- Select a framework, provider, and process type (hierarchical or sequential).
- Input your requirements in plain English.
- Visualize agent relationships and download the generated code or JSON configuration.

### Example Use Cases
- **Research Assistant**: "Create a research team to summarize papers and answer questions."
- **Content Creation**: "Build a team to create viral social media content and manage brand presence."
- **Data Analysis**: "Develop a team to analyze customer data and generate visualizations."
- **Project Management**: "Create a complex project management system with task delegation and progress tracking."

## Process Types Explained
- **Sequential**: Agents perform tasks in a linear order, suitable for straightforward workflows where tasks follow a clear sequence.
- **Hierarchical**: Agents are organized in a hierarchy, with a lead agent coordinating sub-agents, ideal for complex tasks requiring delegation and oversight.

The intelligent defaults feature ensures that the LLM selects the most appropriate process type based on the task's complexity and requirements, while still allowing manual overrides via `--process`.

## Backward Compatibility
The new `--process` flag and intelligent defaults are fully backward compatible. If no process type is specified, the default remains `sequential`, ensuring existing scripts and workflows function as before.

## Connect with Us
- Connect with the maintainer, Aakriti Aggarwal, on [LinkedIn](https://www.linkedin.com/in/aakritiaggarwal13/).
- Check out our [GitHub Issues page](https://github.com/aakriti1318/multi-agent-generator/issues) for ongoing ideas and improvements we are working on.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please check out the [GitHub repository](https://github.com/aakriti1318/multi-agent-generator) for guidelines on how to contribute.

## Support
For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/aakriti1318/multi-agent-generator) or contact the maintainers.

## Footer
© 2025 GitHub, Inc.
