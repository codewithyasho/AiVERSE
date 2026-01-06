'''
USING PYTHON 3.11.9
'''

from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from dotenv import load_dotenv
load_dotenv()


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
        )

    @agent
    def openai_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["openai_agent"],
        )

    @agent
    def llama_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["llama_agent"],
        )

    @agent
    def qwen_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["qwen_agent"],
        )

    @agent
    def kimik2_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["kimik2_agent"],
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
