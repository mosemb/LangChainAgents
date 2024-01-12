"""""
Created on Fri Jan 12 16:26:15 2024

@author: Mose
"""

import os


#C:\Users\Mose\Documents\Env\EnvFile.env
# Load environment variables
from dotenv import load_dotenv,find_dotenv
import os
#from serpapi.google_search_results import GoogleSearchResults


key = load_dotenv(r'C:\Users\Mose\Documents\Env\EnvFile.env')
print(key)




api_key=os.getenv('OPEN_API_KEY')
environment=os.getenv('SERPAPI_API_KEY')

print(api_key)
print(environment)



#Creating an Agent, first load the tools the agent will use
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["google-serper", "llm-math"], llm=llm)

print(tools[0].name, tools[0].description)
print()
print(tools[1].name, tools[1].description)
print()


#Then Initialize the agent with the tools

#In this case we have 2 agents google-serper and llm-math 
#google-serper - Which is a search engine
#llm-math - is a calculator

#When we look into the tool there are lots of things in the tool 
#For example, 
print(tools[1]) #Those are some of the things we can do with the tool


#Now lets initialize the agent, this will take in the tools, llm and agent type
agent = initialize_agent(tools, llm, agent="zero-shot-react-description",verbose=True)

#With the prompt below we have to decide what the agent is going to do
print()
print (agent.agent.llm_chain.prompt.template) 


#So lets run the agent, it will use either the search or calculator
agent.run("How are you doing now?")

agent.run("Who is the current president of United States? Get his age now and divide by 2")

agent.run("Who is the current president of Rwanda? What is the difference between his age and the country's life expectancy")

#Now lets build an agent with more tools
tools2 = load_tools(["google-serper", "llm-math", "wikipedia"], llm=llm)

agent = initialize_agent(tools2, llm, agent="zero-shot-react-description",verbose=True)

print(agent.agent.llm_chain.prompt.template) #This now is our prompt

#we can now ask the agent some questions
agent.run("Who is the head of Google?")

agent.run("Who is the head of Google and for how long has been the head in years todate?")

agent.run("When was Microsoft opened? Add 50 years to that, will we have AGI then?")



