# multi_agent_generator/__main__.py
import argparse
from .multi_agent_generator.generator import AgentGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate multi-agent AI code")
    parser.add_argument("prompt", help="Plain English description")
    parser.add_argument("--framework", choices=["crewai", "crewai-flow", "langgraph", "react"], default="crewai")
    args = parser.parse_args()

    generator = AgentGenerator()
    config = generator.analyze_prompt(args.prompt, args.framework)
    print(config)

if __name__ == "__main__":
    main()
