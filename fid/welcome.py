from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

def welcome():
    ascii=pyfiglet.figlet_format("fid-ffmpeg",font="slant")
    logo = Text(ascii)
    logo.stylize("bold gradient(blue, magenta)")
    console.print(logo, justify="center")
    content =(
        "[bold]fid-ffmpeg Helper[/bold]\n\n"
        "[green]Commands:[/green]\n"
        " • info     Show video info\n"
        " • audio    Extract audio\n"
        " • frames   Extract frames\n"
        " • gif      Create gif\n"
        " • mute     Remove audio\n"
        " • compress Compress video\n\n"
        "[dim]Run : fid <command> <video path>[/dim]")
    console.print(Panel(content,title="fid-ffmpeg",border_style="cyan",expand=True))