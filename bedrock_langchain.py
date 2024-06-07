
from langchain_community.llms import Bedrock
import dotenv

#load environment variables from .env file
dotenv.load_dotenv()

llm = Bedrock(model_id="anthropic.claude-v2")

prompt = "What is the largest city in Vermont?"

response_text = llm.invoke(prompt) #return a response to the prompt

print(response_text)
