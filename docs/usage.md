# Usage

## CLI

Basic usage:

```bash
python -m multi_agent_generator "I need a research assistant that summarizes papers and answers questions" --framework crewai
```

Using WatsonX instead:

```bash
python -m multi_agent_generator "I need a research assistant that summarizes papers and answers questions" --framework crewai --provider watsonx
```

Using Ollama locally:

```bash
python -m multi_agent_generator "Build me a ReAct assistant for customer support" --framework react-lcel --provider ollama
```

Save output to a file:

```bash
python -m multi_agent_generator "I need a team to create viral social media content" --framework langgraph --output social_team.py
```

Get JSON configuration only:

```bash
python -m multi_agent_generator "I need a team to analyze customer data" --framework react --format json
```