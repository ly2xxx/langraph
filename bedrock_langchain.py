
# from langchain_community.llms import Bedrock
from langchain_aws import BedrockLLM
import dotenv

#load environment variables from .env file
dotenv.load_dotenv()

# llm = Bedrock(model_id="anthropic.claude-v2")
llm = BedrockLLM(model_id="anthropic.claude-v2")

prompt = "What is the largest city in Scotland?"

response_text = llm.invoke(prompt) #return a response to the prompt

print(response_text)
