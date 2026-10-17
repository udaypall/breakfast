
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from .env file
load_dotenv()

# Initialize LangChain model
llm = ChatOpenAI(model="gpt-4o-mini")

prompt = """
Suggest exactly 5 healthy breakfast ideas.
Use balanced meals with vegetables or fruit, whole grains,
and protein where practical.
Return only a numbered list, one idea per line.
Do not include a heading, preamble, or extra explanation.
"""

reply = llm.invoke(prompt)

# Print only the response text
print(reply.content)
