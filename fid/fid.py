import typer
import subprocess
from pathlib import Path

app = typer.Typer()

formats = [".mp4",".mov",".avi",".webm"]


@app.command()
def info(vid: str):
    if vid.lower().endswith(tuple(formats)):
        subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", vid], check=True)
    else:
        print("plz enter a proper video format")

@app.command()
def audio(vid: Path):
    if vid.suffix.lower() in formats:
        Vdir= vid.parent
        audio= Vdir / "Audio"
        audio.mkdir(exist_ok=True)
        subprocess.run(["ffmpeg", "-i", vid, "-vn", "-acodec", "mp3", "-y", str(audio / "audio.mp3")], check=True)
    else:
        print("plz enter a proper video format")

@app.command()
def frames(vid: Path):
    if vid.suffix.lower() in formats:
        Fdir= vid.parent
        frames= Fdir / "Frames"
        frames.mkdir(exist_ok=True)
        subprocess.run(["ffmpeg", "-i", str(vid),str(frames/ "frame_%01d.png")],check=True )
    else:
        print("plz enter a proper video format")

if __name__=="__main__":
  app()
