from rich.console import Console
from rich.prompt import Confirm

console = Console()

def request_approval(action_type: str, command: str) -> bool:
    """
    Safety Gate: Requests human-in-the-loop approval before executing sensitive commands.
    """
    console.print(f"\n[bold red]⚠️  SAFETY GATE TRIGGERED[/bold red]")
    console.print(f"[yellow]Action Type:[/yellow] {action_type}")
    console.print(f"[yellow]Command/Action:[/yellow] [bold white]{command}[/bold white]")
    
    # Prompt the user for approval
    is_approved = Confirm.ask(f"[bold red]Do you approve this action?[/bold red]")
    
    if is_approved:
        console.print("[bold green]✅ Action Approved.[/bold green]")
        return True
    else:
        console.print("[bold red]❌ Action Denied by User.[/bold red]")
        return False
