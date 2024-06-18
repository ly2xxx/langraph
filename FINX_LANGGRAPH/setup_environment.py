import os

from decouple import config


def set_environment_variables() -> None:
    os.environ["OPENAI_API_KEY"] = str(config("OPENAI_API_KEY"))