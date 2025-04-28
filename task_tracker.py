import json
import typer
from rich import print
from rich.table import Table
from typing_extensions import Annotated

app = typer.Typer()

table = Table("Name", "Item")

class Player:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def to_dict(self):
        return {"name": self.name, "gun": self.gun}



@app.command("init")
def main(
        name: Annotated[str, typer.Argument(help="Your name", rich_help_panel="Player name", show_default=False)],
        gun: Annotated[str, typer.Argument(help="Your Gun", rich_help_panel="Weapons")] =  "", 
        formal: Annotated[bool, typer.Option(help="Formal or Informal greeting")]= False,
        lastname: Annotated[str, typer.Option(help="Last Name", prompt=True, show_default=False)]="Barbosa"):

    if formal:
        print(f"[red]Good day Ms.[/red] [bold green]{name} {lastname} {gun}[/bold green]")
    else:
        print(f"Testing {name} {lastname} {gun}")

@app.command()
def add(name: str, gun: str):
    new = Player(name, gun)
    new = new.to_dict()
    with open('tasks.json', 'w') as json_file:
        json.dump(new, json_file)


@app.command("print")
def print_table():
    with open('tasks.json') as json_file:
        data = json.load(json_file)
        print(data['name'])


if __name__ == "__main__":
    app()