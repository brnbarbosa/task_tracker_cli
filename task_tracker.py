import json
import typer
import os
from rich import print
from rich.table import Table
from rich.console import Console
from typing_extensions import Annotated
from datetime import datetime

def callback():
    print("Thinking...")

app = typer.Typer(callback=callback)

FILE_PATH = 'tasks.json'

table = Table("Description", "DeadLine", "Status")
console = Console()

class Task:
    def __init__(self, description: str, date: datetime):
        self.description: str = description
        self.date: datetime = date

    def to_dict(self) -> dict:
        return {"description": self.description, "date": str(self.date)}


@app.command("init")
def main():
    if os.path.exists(FILE_PATH):
        print("File exists")
    else:
        tasks = {}
        with open(FILE_PATH, 'w') as write_file:
            json.dump(tasks, write_file)

@app.command('add')
def add(task: Annotated[str, typer.Argument(help="Enter the task description")], date: Annotated[datetime, typer.Option(help="Enter the deadline for this task", prompt="Enter the deadline: ")]):
    new = Task(task, date).to_dict()
    task_list = []

    try:
        with open(FILE_PATH) as json_file:
            task_list = json.load(json_file)

            if not isinstance(task_list, list):
                task_list = []
    except FileNotFoundError:
        print(f"{FILE_PATH} not found.")
    except json.JSONDecodeError:
        print("Could not decode JSON file.")
        task_list = []

    task_list.append(new)

    with open(FILE_PATH, 'w') as json_file:
        json.dump(task_list, json_file, indent=4)


@app.command("print")
def print_table():
    with open(FILE_PATH) as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            table.add_row(data[i]['description'], data[i]['date'][:10])

    print(table)

if __name__ == "__main__":
    app()