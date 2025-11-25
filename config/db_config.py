import requests, pathlib
from langchain_community.utilities import SQLDatabase


class DBConfig:
    def __init__(self):

        url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"
        local_path = pathlib.Path("Chinook.db")

        if local_path.exists():
            print(f"{local_path} already exists, skipping download.")
        else:
            response = requests.get(url)
            if response.status_code == 200:
                local_path.write_bytes(response.content)
                print(f"File downloaded and saved as {local_path}")
            else:
                print(f"Failed to download the file. Status code: {response.status_code}")
        


    def get_db_conn(self) -> str:

        db = SQLDatabase.from_uri("sqlite:///Chinook.db")

        print(f"Dialect: {db.dialect}")
        print(f"Available tables: {db.get_usable_table_names()}")
        print(f'Sample output: {db.run("SELECT * FROM Artist LIMIT 5;")}')
        return db