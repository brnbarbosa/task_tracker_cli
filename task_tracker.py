import json
import typer
from rich import print
from rich.table import Table
from rich.console import Console
from typing_extensions import Annotated
from datetime import datetime

app = typer.Typer()

FILE_PATH = 'tasks.json'

table = Table("Description", "Date")
console = Console()

class Task:
    def __init__(self, description: str, date: datetime):
        self.description: str = description
        self.date: datetime = date

    def to_dict(self) -> dict:
        return {"description": self.description, "date": str(self.date)}


@app.command("init")
def main(
        name: Annotated[str, typer.Argument(help="Your name", rich_help_panel="Task name", show_default=False)],
        gun: Annotated[str, typer.Argument(help="Your Gun", rich_help_panel="Weapons")] =  "", 
        formal: Annotated[bool, typer.Option(help="Formal or Informal greeting")]= False,
        lastname: Annotated[str, typer.Option(help="Last Name", prompt=True, show_default=False)]="Barbosa"):

    if formal:
        print(f"[red]Good day Ms.[/red] [bold green]{name} {lastname} {gun}[/bold green]")
    else:
        print(f"Testing {name} {lastname} {gun}")

@app.command('add')
def add(task: str, date: datetime):
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
    table.add_column("Description")
    table.add_column("Date")
    with open(FILE_PATH) as json_file:
        data = json.load(json_file)
        #for i in range(len(data)):
            #Table.add_row(data[i]['description'], data[i]['date'][:10])

    Console.print(table)

if __name__ == "__main__":
    app()