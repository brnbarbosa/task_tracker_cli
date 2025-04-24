import json
import typer
from rich import print
from rich.table import Table

table = Table("Name", "Item")

def main(name: str, gun : str =  "", formal : bool = False):
    if formal:
        print(f"[red]Good day Ms.[/red] [bold green]{name} {gun}[/bold green]")
    else:
        print(f"Testing {name} {gun}")

    add(name, gun)


def add(name: str, gun: str):
    table.add_row(name, gun)
    print(table)

if __name__ == "__main__":
    typer.run(main)