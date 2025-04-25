import json
import typer
from rich import print
from rich.table import Table
from typing_extensions import Annotated

app = typer.Typer()

table = Table("Name", "Item")

@app.command()
def main(
        name: Annotated[str, typer.Option("--name", "-n", help="Your name", show_default=False)],
        gun: Annotated[str, typer.Argument(help="Your Gun", rich_help_panel="Weapons")] =  "", 
        formal: Annotated[bool, typer.Option(help="Formal or Informal greeting")]= False,
        lastname: Annotated[str, typer.Option(help="Last Name", prompt=True, show_default=False)]="Barbosa"):
    """
    Showed only in Help.
    """
    if formal:
        print(f"[red]Good day Ms.[/red] [bold green]{name} {lastname} {gun}[/bold green]")
    else:
        print(f"Testing {name} {lastname} {gun}")
        add(name, gun)
    


def add(name: str, gun: str):
    table.add_row(name, gun)
    print(table)

if __name__ == "__main__":
    app()