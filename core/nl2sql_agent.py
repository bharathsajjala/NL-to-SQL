from langchain.agents import create_agent
from .sql_tools import SQL_TOOL_DB

sql_tool= SQL_TOOL_DB()
model = sql_tool.get_model()
tools = sql_tool.get_tooldb()
system_prompt = sql_tool.get_system_prompt()

agent = create_agent(
    model,
    tools,
    system_prompt=system_prompt,
)

question = "Which genre on average has the longest tracks?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()

# response = agent.invoke({"messages": [{"role": "user", "content": question}]})

# response["messages"][-1].pretty_print()