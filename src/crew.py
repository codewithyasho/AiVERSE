'''
USING PYTHON 3.11.9
'''

from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.agents.agent_builder.base_agent import BaseAgent
load_dotenv()


# TOOLS for agents
serper_dev_tool = SerperDevTool()
scrape_website_tool = ScrapeWebsiteTool()

# Toolkit
toolkit = [serper_dev_tool, scrape_website_tool]

# Define the class for the crew


@CrewBase
class AIVerseCrew():

    # define for the crew method
    agents: list[BaseAgent]
    tasks: list[Task]

    # define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # =========== AGENTS ===========

    @agent
    def deepseek_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["deepseek_agent"],
            tools=toolkit,
        )

    @agent
    def openai_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["openai_agent"],
            tools=toolkit,
        )

    @agent
    def llama_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["llama_agent"],
            tools=toolkit,
        )

    @agent
    def qwen_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["qwen_agent"],
            tools=toolkit,
        )

    @agent
    def kimik2_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["kimik2_agent"],
            tools=toolkit,
        )

    # =========== TASKS ===========
    # order of tasks matters

    @task
    def deepseek_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["deepseek_agent_task"],
            output_file="outputs/deepseek-task.md",
        )

    @task
    def openai_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["openai_agent_task"],
            output_file="outputs/openai-gpt-task.md",
        )

    @task
    def llama_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["llama_agent_task"],
            output_file="outputs/meta-llama3-task.md",
        )

    @task
    def qwen_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["qwen_agent_task"],
            output_file="outputs/alibaba-qwen-task.md",
        )

    @task
    def kimik2_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["kimik2_agent_task"],
            output_file="outputs/kimi-k2-task.md",
        )

    # =========== CREW ===========

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
