"""
Setup script for multi-agent-generator package.
"""
from setuptools import setup, find_packages

# Define requirements directly
REQUIREMENTS = [
    "streamlit>=1.22.0",
    "crewai>=0.28.0",
    "openai>=1.3.0",
    "langchain>=0.0.271",
    "langgraph>=0.0.16",
    "python-dotenv>=1.0.0",
    "pydantic>=2.0.0",
]

# Read README for long description
try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = (
        "Multi-Agent Generator - Generate multi-agent AI code from natural language"
    )

setup(
    name="multi-agent-generator",
    version="0.2.0",
    description="Generate multi-agent AI teams using CrewAI, LangGraph, and ReAct with multiple LLM providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Aakriti Aggarwal",
    author_email="aakritiaggarwal2k@gmail.com",
    url="https://github.com/aakriti1318/multi-agent-generator",
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        "watsonx": ["ibm-watsonx-ai>=0.2.0"],
        "dev": ["pytest>=7.0.0", "black>=23.0.0", "flake8>=6.0.0"],
    },
    entry_points={
        "console_scripts": [
            "multi-agent-generator=multi_agent_generator.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)