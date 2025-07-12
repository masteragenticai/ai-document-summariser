"""
CrewAI Implementation for Document Summariser
Month 1 Mini Project - AI Solutions Course | MasterAgenticAI.Academy
OpenAI-only version using original working library versions
"""

import yaml
from crewai import Agent, Task, Crew, Process
from langchain.chat_models import ChatOpenAI
import streamlit as st

class DocumentSummariserCrew:
    """Document Summariser Crew for Business Analysis - OpenAI Only"""

    def __init__(self, api_key: str):
        """
        Initialise the crew with OpenAI configuration
        
        Args:
            api_key: The OpenAI API key
        """
        # Load configuration
        with open('config.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

        # Initialise the language model (OpenAI only)
        self.llm = ChatOpenAI(
            openai_api_key=api_key,
            model_name="gpt-4-turbo-preview",
            temperature=0.1
        )

        # Initialise agents
        self.document_analyst = self._create_agent('document_analyst')
        self.summary_writer = self._create_agent('summary_writer')

        # Initialise tasks
        self.analyse_task = self._create_task('analyse_document', self.document_analyst)
        self.summary_task = self._create_task('create_summary', self.summary_writer)

    def _create_agent(self, agent_name: str) -> Agent:
        """Create an agent from configuration"""
        agent_config = self.config['agents'][agent_name]
        return Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            max_iter=agent_config.get('max_iter', 3),
            verbose=agent_config.get('verbose', True),
            llm=self.llm,
            allow_delegation=False
        )

    def _create_task(self, task_name: str, agent: Agent) -> Task:
        """Create a task from configuration"""
        task_config = self.config['tasks'][task_name]
        return Task(
            description=task_config['description'],
            agent=agent,
            expected_output=task_config['expected_output']
        )

    def summarise_document(self, document_text: str) -> str:
        """
        Run the document summarisation crew
        
        Args:
            document_text: The text to summarise
            
        Returns:
            The executive summary
        """
        # Update the analyse task with the document text
        self.analyse_task.description = f"""
        {self.config['tasks']['analyse_document']['description']}

        DOCUMENT TO ANALYSE:
        {document_text}
        """

        # Create the crew
        crew = Crew(
            agents=[self.document_analyst, self.summary_writer],
            tasks=[self.analyse_task, self.summary_task],
            process=Process.sequential,
            verbose=True
        )

        # Execute the crew
        result = crew.kickoff()
        return result
