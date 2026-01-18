import typer
import subprocess
from pathlib import Path
import shutil
from .welcome import welcome
app = typer.Typer()

formats = [".mp4",".mov",".avi",".webm"]

@app.callback(invoke_without_command=True)
def start(ctx : typer.Context):
    if ctx.invoked_subcommand is None:
        welcome()

def ffmpeg():
    if shutil.which("ffmpeg")is None:
        print("ffmpeg isn't installed\n download from: https://ffmpeg.org/download.html")
        raise typer.Exit()

def ckvideo(vid:Path):
    if not vid.exists():
        print("file doesn't exist")
        raise typer.Exit()
    

@app.command()
def info(vid: Path):
    ffmpeg()
    ckvideo(vid)
    subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", str(vid)], check=True)

@app.command()
def audio(vid: Path):
    ffmpeg()
    ckvideo(vid)
    audio=vid.with_suffix(".mp3")
    subprocess.run(["ffmpeg", "-i", str(vid), "-vn", "-acodec", "mp3", "-y", str(audio)], check=True)
    

@app.command()
def frames(vid: Path):
    ffmpeg()
    ckvideo(vid)
    Fdir= vid.parent
    frames= Fdir / "Frames" / vid.stem
    frames.mkdir(parents=True,exist_ok=True)
    subprocess.run(["ffmpeg", "-i", str(vid),str(frames/ "frame_%02d.png")],check=True )
   
@app.command()
def gif(vid: Path):
    ffmpeg()
    ckvideo(vid)
    gif=vid.with_suffix(".gif")
    subprocess.run(["ffmpeg", "-i", str(vid), "-t", "3", "-vf", "scale=320:-1", "-y", str(gif)], check=True)


@app.command()
def mute(vid: Path):
    ffmpeg()
    ckvideo(vid)
    mute=vid.with_stem(f"{vid.stem}_muted").with_suffix(vid.suffix)
    subprocess.run(["ffmpeg", "-i", str(vid), "-c", "copy", "-an", "-y", str(mute)], check=True)

@app.command()
def compress(vid: Path, crf: int=28):
    ffmpeg()
    ckvideo(vid)
    compress= vid.with_stem(f"{vid.stem}_compressed").with_suffix(".mkv")
    subprocess.run(["ffmpeg", "-i", str(vid),"-c:v", "libx264", "-crf", str(crf), "-preset","medium","-c:a","aac","-b:a","96k","-y",str(compress),], check=True)

if __name__=="__main__":
        app()