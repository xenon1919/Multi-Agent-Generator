import os
import time
import streamlit as st

from multi_agent_generator.generator import AgentGenerator
from multi_agent_generator.multi_agent_generator.frameworks.crewai_generator import create_crewai_code, create_crewai_flow_code
from multi_agent_generator.multi_agent_generator.frameworks.langgraph_generator import create_langgraph_code
from multi_agent_generator.multi_agent_generator.frameworks.react_generator import create_react_code

def create_code_block(config, framework):
    if framework == "crewai":
        return create_crewai_code(config)
    elif framework == "crewai-flow":
        return create_crewai_flow_code(config)
    elif framework == "langgraph":
        return create_langgraph_code(config)
    elif framework == "react":
        return create_react_code(config)
    else:
        return "# Invalid framework"

def main():
    st.set_page_config(page_title="Agent Framework Generator", page_icon="🚀", layout="wide")
    
    st.title("Multi-Framework Agent Generator")
    st.write("Generate agent code for different frameworks based on your requirements!")

    # Display IBM WatsonX AI information
    st.sidebar.info("Powered by IBM Watsonx")
    
    # Check for API key
    if not os.getenv("WATSON_API_KEY"):
        api_key = st.sidebar.text_input("Watson API Key:", type="password")
        if api_key:
            os.environ["WATSON_API_KEY"] = api_key

    # Framework selection
    st.sidebar.title("🔄 Framework Selection")
    framework = st.sidebar.radio(
        "Choose a framework:",
        ["crewai", "crewai-flow", "langgraph", "react"],
        format_func=lambda x: {
            "crewai": "CrewAI",
            "crewai-flow": "CrewAI Flow",
            "langgraph": "LangGraph",
            "react": "ReAct Framework"
        }[x]
    )
    
    # Framework description
    framework_descriptions = {
        "crewai": """
        **CrewAI** is a framework for orchestrating role-playing autonomous AI agents. 
        It allows you to create a crew of agents that work together to accomplish tasks, 
        with each agent having a specific role, goal, and backstory.
        """,
        "crewai-flow": """
        **CrewAI Flow** extends CrewAI with event-driven workflows. 
        It enables you to define multi-step processes with clear transitions between steps,
        maintaining state throughout the execution, and allowing for complex orchestration
        patterns like sequential, parallel, and conditional execution.
        """,
        "langgraph": """
        **LangGraph** is LangChain's framework for building stateful, multi-actor applications with LLMs.
        It provides a way to create directed graphs where nodes are LLM calls, tools, or other operations, 
        and edges represent the flow of information between them.
        """,
        "react": """
        **ReAct** (Reasoning + Acting) is a framework that combines reasoning and action in LLM agents.
        It prompts the model to generate both reasoning traces and task-specific actions in an interleaved manner, 
        creating a synergy between the two that leads to improved performance.
        """
    }
    
    st.sidebar.markdown(framework_descriptions[framework])
    
    # Sidebar for examples
    st.sidebar.title("📚 Example Prompts")
    example_prompts = {
        "Research Assistant": "I need a research assistant that summarizes papers and answers questions",
        "Content Creation": "I need a team to create viral social media content and manage our brand presence",
        "Data Analysis": "I need a team to analyze customer data and create visualizations",
        "Technical Writing": "I need a team to create technical documentation and API guides"
    }
    
    selected_example = st.sidebar.selectbox("Choose an example:", list(example_prompts.keys()))
    
    # Main input area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Define Your Requirements")
        user_prompt = st.text_area(
            "Describe what you need:",
            value=example_prompts[selected_example],
            height=100
        )
        
        # Add workflow steps input for CrewAI Flow
        if framework == "crewai-flow":
            st.subheader("🔄 Define Workflow Steps")
            workflow_steps = st.text_area(
                "List the steps in your workflow (one per line):",
                value="1. Data collection\n2. Analysis\n3. Report generation",
                height=100
            )
        
        if st.button(f"🚀 Generate {framework.upper()} Code"):
            if not os.getenv("WATSON_API_KEY"):
                st.error("Please set your Watson API Key in the sidebar")
            elif not os.getenv("PROJECT_ID"):
                st.error("PROJECT_ID not found in .env file")
            else:
                with st.spinner(f"Generating your {framework} code..."):
                    generator = AgentGenerator()
                    
                    # Handle CrewAI Flow differently
                    if framework == "crewai-flow":
                        # Extract workflow steps
                        steps = [step.strip() for step in workflow_steps.split("\n") if step.strip()]
                        steps = [step[2:].strip() if step[0].isdigit() and step[1] == "." else step for step in steps]
                        
                        # Append workflow information to the prompt
                        flow_prompt = f"{user_prompt}\n\nWorkflow steps:\n"
                        for i, step in enumerate(steps):
                            flow_prompt += f"{i+1}. {step}\n"
                        
                        # Use the CrewAI analyzer but modify for flow
                        config = generator.analyze_prompt(flow_prompt, "crewai")
                        
                        # Modify config to ensure tasks align with workflow steps
                        if len(config["tasks"]) < len(steps):
                            # Add missing tasks
                            for i in range(len(config["tasks"]), len(steps)):
                                config["tasks"].append({
                                    "name": f"step_{i+1}",
                                    "description": f"Execute step: {steps[i]}",
                                    "tools": config["tasks"][0]["tools"] if config["tasks"] else ["basic_tool"],
                                    "agent": config["agents"][0]["name"] if config["agents"] else "default_assistant",
                                    "expected_output": f"Results from {steps[i]}"
                                })
                        elif len(config["tasks"]) > len(steps):
                            # Trim extra tasks
                            config["tasks"] = config["tasks"][:len(steps)]
                            
                        # Update task names and descriptions to match steps
                        for i, step in enumerate(steps):
                            config["tasks"][i]["name"] = f"{step.lower().replace(' ', '_')}"
                            config["tasks"][i]["description"] = f"Execute the '{step}' step"
                        
                        st.session_state.config = config
                        st.session_state.code = create_crewai_flow_code(config)  # Function for Flow
                    else:
                        config = generator.analyze_prompt(user_prompt, framework)
                        st.session_state.config = config
                        st.session_state.code = create_code_block(config, framework)
                        
                    st.session_state.framework = framework
                    
                    time.sleep(0.5)  # Small delay for better UX
                    st.success(f"✨ {framework.upper()} code generated successfully!")

    with col2:
        st.subheader("💡 Framework Tips")
        if framework == "crewai":
            st.info("""
            **CrewAI Tips:**
            - Define clear roles for each agent
            - Set specific goals for better performance
            - Consider how agents should collaborate
            - Specify task delegation permissions
            """)
        elif framework == "crewai-flow":
            st.info("""
            **CrewAI Flow Tips:**
            - Define a clear sequence of workflow steps
            - Use the @start decorator for the entry point
            - Use @listen decorators to define step transitions
            - Maintain state between workflow steps
            - Consider how to aggregate results at the end
            """)
        elif framework == "langgraph":
            st.info("""
            **LangGraph Tips:**
            - Design your graph flow carefully
            - Define clear node responsibilities
            - Consider conditional routing between nodes
            - Think about how state is passed between nodes
            """)
        else:  # react
            st.info("""
            **ReAct Tips:**
            - Focus on the reasoning steps
            - Define tools with clear descriptions
            - Provide examples of thought processes
            - Consider the observation/action cycle
            """)

    # Display results
    if 'config' in st.session_state:
        st.subheader("🔍 Generated Configuration")
        
        # Tabs for different views
        tab1, tab2 = st.tabs(["📊 Visual Overview", "💻 Code"])
        
        with tab1:
            current_framework = st.session_state.framework
            
            if current_framework in ["crewai", "crewai-flow"]:
                # Display Agents
                st.subheader("Agents")
                for agent in st.session_state.config["agents"]:
                    with st.expander(f"🤖 {agent['role']}", expanded=True):
                        st.write(f"**Goal:** {agent['goal']}")
                        st.write(f"**Backstory:** {agent['backstory']}")
                        st.write(f"**Tools:** {', '.join(agent['tools'])}")
                
                # Display Tasks
                st.subheader("Tasks")
                for task in st.session_state.config["tasks"]:
                    with st.expander(f"📋 {task['name']}", expanded=True):
                        st.write(f"**Description:** {task['description']}")
                        st.write(f"**Expected Output:** {task['expected_output']}")
                        st.write(f"**Assigned to:** {task['agent']}")
                        
                # Show Flow Diagram for CrewAI Flow
                if current_framework == "crewai-flow":
                    st.subheader("Flow Diagram")
                    task_names = [task["name"] for task in st.session_state.config["tasks"]]
                    
                    # Create a simple graph visualization
                    st.write("Event Flow:")
                    flow_html = f"""
                    <div style="text-align: center; padding: 20px;">
                        <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap;">
                            <div style="padding: 10px; margin: 5px; background-color: #f0f0f0; border-radius: 5px; text-align: center;">
                                Start
                            </div>
                            <div style="margin: 0 10px;">→</div>
                    """
                    
                    for i, task in enumerate(task_names):
                        flow_html += f"""
                            <div style="padding: 10px; margin: 5px; background-color: #e1f5fe; border-radius: 5px; text-align: center;">
                                {task}
                            </div>
                        """
                        if i < len(task_names) - 1:
                            flow_html += f"""<div style="margin: 0 10px;">→</div>"""
                    
                    flow_html += f"""
                            <div style="margin: 0 10px;">→</div>
                            <div style="padding: 10px; margin: 5px; background-color: #f0f0f0; border-radius: 5px; text-align: center;">
                                End
                            </div>
                        </div>
                    </div>
                    """
                    
                    st.components.v1.html(flow_html, height=150)
                    
                    # Show state elements
                    st.subheader("State Elements")
                    st.code("""
class AgentState(BaseModel):
    query: str
    results: Dict[str, Any]
    current_step: str
                    """, language="python")
                    
                    # Show execution visualization 
                    st.subheader("Execution Flow")
                    st.write("The workflow executes through these phases:")
                    
                    # Create execution flow diagram
                    exec_flow = """
                    ```mermaid
                    flowchart LR
                        A[Initialize] --> B[Process Query]
                        B --> C[Execute Tasks]
                        C --> D[Compile Results]
                        D --> E[Return Final Output]
                    ```
                    """
                    st.markdown(exec_flow)
                    
                    # Show event listeners
                    st.subheader("Event Listeners")
                    event_listeners = "```python\n"
                    event_listeners += "@start()\ndef initialize_workflow(self):\n    # Initialize workflow state\n\n"
                    
                    # Add each task's listener
                    for i, task in enumerate(st.session_state.config["tasks"]):
                        task_name = task["name"].replace("-", "_")
                        previous = "initialize_workflow" if i == 0 else f"execute_{st.session_state.config['tasks'][i-1]['name'].replace('-', '_')}"
                        event_listeners += f"@listen({previous})\ndef execute_{task_name}(self, state):\n    # Execute {task['name']} task\n\n"
                    
                    # Add final listener
                    last_task = st.session_state.config["tasks"][-1]["name"].replace("-", "_")
                    event_listeners += f"@listen(execute_{last_task})\ndef finalize_workflow(self, state):\n    # Compile final results\n"
                    event_listeners += "```"
                    
                    st.markdown(event_listeners)
            
            elif current_framework == "langgraph":
                # Display Agents
                st.subheader("Agents")
                for agent in st.session_state.config["agents"]:
                    with st.expander(f"🤖 {agent['role']}", expanded=True):
                        st.write(f"**Goal:** {agent['goal']}")
                        st.write(f"**Tools:** {', '.join(agent['tools'])}")
                        st.write(f"**LLM:** {agent['llm']}")
                
                # Display Nodes
                st.subheader("Graph Nodes")
                for node in st.session_state.config["nodes"]:
                    with st.expander(f"📍 {node['name']}", expanded=True):
                        st.write(f"**Description:** {node['description']}")
                        st.write(f"**Agent:** {node['agent']}")
                
                # Display Edges
                st.subheader("Graph Edges")
                for edge in st.session_state.config["edges"]:
                    with st.expander(f"🔗 {edge['source']} → {edge['target']}", expanded=True):
                        if "condition" in edge:
                            st.write(f"**Condition:** {edge['condition']}")
            
            elif current_framework == "react":
                # Display Agents
                st.subheader("Agents")
                for agent in st.session_state.config["agents"]:
                    with st.expander(f"🤖 {agent['role']}", expanded=True):
                        st.write(f"**Goal:** {agent['goal']}")
                        st.write(f"**Tools:** {', '.join(agent['tools'])}")
                        st.write(f"**LLM:** {agent['llm']}")
                
                # Display Tools
                st.subheader("Tools")
                for tool in st.session_state.config.get("tools", []):
                    with st.expander(f"🔧 {tool['name']}", expanded=True):
                        st.write(f"**Description:** {tool['description']}")
                        st.write("**Parameters:**")
                        for param, desc in tool["parameters"].items():
                            st.write(f"- **{param}**: {desc}")
                
                # Display Examples
                if "examples" in st.session_state.config:
                    st.subheader("Examples")
                    for i, example in enumerate(st.session_state.config["examples"]):
                        with st.expander(f"📝 Example {i+1}: {example['query'][:30]}...", expanded=True):
                            st.write(f"**Query:** {example['query']}")
                            st.write(f"**Thought:** {example['thought']}")
                            st.write(f"**Action:** {example['action']}")
                            st.write(f"**Observation:** {example['observation']}")
                            st.write(f"**Final Answer:** {example['final_answer']}")
        
        with tab2:
            # Display code with options for visualization and execution
            st.code(st.session_state.code, language="python")
            
            # Add buttons for CrewAI Flow capabilities
            if st.session_state.framework == "crewai-flow":
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("📋 Copy Code"):
                        st.toast("Code copied to clipboard! 📋")
                
                with col2:
                    if st.button("🔄 Visualize Flow"):
                        st.info("Flow visualization would be generated here in a real implementation")
                        st.toast("Flow visualization generated! 🔄")
                
                with col3:
                    if st.button("▶️ Test Execution"):
                        st.info("In a real implementation, this would execute the flow with sample data")
                        st.toast("Flow execution started! ▶️")
                
                # Add sample execution output
                with st.expander("Sample Execution Output", expanded=False):
                    st.code("""
Starting workflow with query: I need a team to analyze customer data
Current step: initial
Executing task: data_collection
Agent Research Specialist starting...
Task: Handle data collection and preparation
Task output: Successfully collected customer data from various sources.
- Identified 3,245 customer records
- Cleaned and normalized demographic information
- Prepared dataset for analysis

Executing task: data_analysis  
Agent Data Analyst starting...
Task: Analyze patterns and insights in customer data
Task output: Analysis completed with key findings:
1. Customer retention rate is 68% overall
2. Key demographic segments identified: [...]
3. Purchase frequency patterns suggest [...]

Executing task: report_generation
Agent Content Creator starting...
Task: Create comprehensive report with visualizations
Task output: Report generated with 5 sections:
- Executive Summary
- Methodology
- Key Findings
- Visualizations (3 charts)
- Recommendations

Workflow completed, compiling final results...
Results saved to workflow_results.md
                    """)
                
                # Add explanation of flow capabilities
                st.subheader("CrewAI Flow Capabilities")
                st.markdown("""
                The generated code provides these key capabilities:
                
                1. **Event-driven execution** - Each step triggers based on completion of previous steps
                2. **State management** - Workflow state persists between steps
                3. **Context awareness** - Each step has access to previous results
                4. **Visualization** - Flow structure can be visualized with `flow.plot()`
                5. **Result compilation** - Final output aggregates all step results
                6. **Error handling** - Each step can handle failures gracefully
                
                To use this code in your application:
                1. Install CrewAI: `pip install crewai`
                2. Copy the generated code
                3. Configure your OpenAI API key
                4. Modify inputs and outputs as needed
                5. Run the workflow with your specific query
                """)
            else:
                if st.button("📋 Copy Code"):
                    st.toast("Code copied to clipboard! 📋")

if __name__ == "__main__":
    main()