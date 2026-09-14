import os
from datetime import date

from decouple import config


def set_environment_variables(project_name: str = "") -> None:
    if not project_name:
        project_name = f"Test_{date.today()}"

    os.environ["OPENAI_API_KEY"] = str(config("OPENAI_API_KEY", default="sk-admin"))
    os.environ["OPENAI_BASE_URL"] = str(config("OPENAI_BASE_URL", default="http://localhost:8081/v1"))

    langchain_key = str(config("LANGCHAIN_API_KEY", default=""))
    os.environ["LANGCHAIN_API_KEY"] = langchain_key
    if langchain_key:
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = project_name
    else:
        os.environ["LANGCHAIN_TRACING_V2"] = "false"

    os.environ["TAVILY_API_KEY"] = str(config("TAVILY_API_KEY", default=""))
    os.environ.setdefault("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    print("API Keys loaded and tracing set with project name: ", project_name)