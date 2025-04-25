# agents
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv
# create a llm

# load all environment variables
load_dotenv()

# create a llm
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.6)
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
# setup agents
tools = [wiki]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

response = agent.invoke("when was irrfan khan born") 
print("Loading")
print(response["output"])