from rich import print as rprint
from rich.console import Console

rich_console : Console = Console()
rprint("[bold green]Welcome to the band name generator![/bold green]")
city_name : str = rich_console.input("[bold blue]Please insert the name of your town/city[/bold blue]\n")
pet_name : str = rich_console.input("[bold red]Please insert the name of your pet[/bold red]\n")
rprint(f"[bold yellow]Your generated band name is: [/bold yellow][bold blue]{city_name} {pet_name}[/bold blue]")