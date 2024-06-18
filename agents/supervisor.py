from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import ToolDescription

class SupervisorAgent:
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.tools = [
            ToolDescription(name="Search", description="Search for relevant information"),
            ToolDescription(name="Web Scraper", description="Extract data from websites"),
        ]

    def supervise(self, article: dict):
        system_prompt = "You are a supervisor tasked with managing a conversation between the following workers: Search, Web Scraper. Given the following user request, respond with the worker to act next. Each worker will perform a task and respond with their results and status. When finished, respond with FINISH."
        agent = initialize_agent(
            self.tools,
            self.llm,
            agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            agent_kwargs={"system_message": system_prompt},
        )

        result = agent.run(article)
        return result

    def run(self, article: dict):
        article.update(self.supervise(article))
        return article
