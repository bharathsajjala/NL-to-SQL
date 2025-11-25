from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import init_chat_model
from config.db_config import DBConfig
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import getpass

 
model = None
db = None
class SQL_TOOL_DB:
    def __init__(self):
        global model
        load_dotenv()  
        if not os.getenv("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

        model = init_chat_model("gpt-4.1")
    def get_model(self):
        global model
        if model is None:
            SQL_TOOL_DB()
        return model

    def get_tooldb(self):
        global db 
        db_config = DBConfig()
        db = db_config.get_db_conn()
        toolkit = SQLDatabaseToolkit(db=db, llm=model)

        tools = toolkit.get_tools()
        
        for tool in tools:
            print(f"{tool.name}: {tool.description}\n")
        return tools

    def get_system_prompt(self):
        system_prompt = """
            You are an agent designed to interact with a SQL database.
            Given an input question, create a syntactically correct {dialect} query to run,
            then look at the results of the query and return the answer. Unless the user
            specifies a specific number of examples they wish to obtain, always limit your
            query to at most {top_k} results.

            You can order the results by a relevant column to return the most interesting
            examples in the database. Never query for all the columns from a specific table,
            only ask for the relevant columns given the question.

            You MUST double check your query before executing it. If you get an error while
            executing a query, rewrite the query and try again.

            DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
            database.

            To start you should ALWAYS look at the tables in the database to see what you
            can query. Do NOT skip this step.

            Then you should query the schema of the most relevant tables.
            """.format(
                dialect=db.dialect,
                top_k=5,
            )
        return system_prompt