# agents
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv
# create a llm

# load all environment variables
load_dotenv()

# create a llm
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.6)

# setup agents
tools = load_tools(["wikipedia","llm-math"],llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("How much films did irrfan khan acted, add 6 to it")