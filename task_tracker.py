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
    def __init__(self, description: str, deadline: datetime, status: str = "default"):
        self.description: str = description
        self.deadline: datetime = deadline
        self.status: str = self.check_status()

    def to_dict(self) -> dict:
        return {"description": self.description, "deadline": str(self.deadline), "status" : self.status }
    
    def check_status(self) -> str:
        today = datetime.today()
        if self.deadline >= today:
            return 'To do'
        elif self.deadline < today:
            return 'Delayed'
        else:
            return 'Waiting definition'


@app.command("init", help="Init the database")
def main():
    if os.path.exists(FILE_PATH):
        print("File exists")
    else:
        tasks = {}
        with open(FILE_PATH, 'w') as write_file:
            json.dump(tasks, write_file)

@app.command('add', help="Add a new task, insert the task description and the deadline will be prompt")
def add(task: Annotated[str, typer.Argument(help="Enter the task description")], deadline: Annotated[datetime, typer.Option(help="Enter the deadline for this task", prompt="Enter the deadline")]):
    new = Task(task, deadline).to_dict()
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


@app.command("print", help="Print task table")
def print_table():
    with open(FILE_PATH) as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            table.add_row(data[i]['description'], data[i]['deadline'][:10], data[i]['status'])

    print(table)

@app.command("done", help="Set the task status as done")
def done(task: Annotated[str, typer.Argument(help="Enter task description")]):
    temp_data = {}

    with open(FILE_PATH, 'r') as read_file:
        temp_data = json.load(read_file)
        
    with open(FILE_PATH, 'w') as json_file:
        for i in range(len(temp_data)):
            if temp_data[i]['description'] == task:
                temp_data[i]['status'] = 'Done'
        json.dump(temp_data, json_file, indent=4)

@app.command("delete", help="Delete a specific task")
def delete(task: Annotated[str, typer.Argument(help="Enter task description")]):
    temp_data = []
    removed_value = {}
    try:
        with open(FILE_PATH, 'r') as read_file:
            temp_data = json.load(read_file)
    except:
        print('file inexist')

    try:
        with open(FILE_PATH, 'w') as json_file:
            for i in range(len(temp_data)):
                if temp_data[i]['description'] == task:
                    removed_value = temp_data.pop(i)

            json.dump(temp_data, json_file, indent=4)
    except:
        print(removed_value)

    print(f'{removed_value['description']} was sucessfull removed')

if __name__ == "__main__":
    app()