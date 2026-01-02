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
        audio=vid.with_suffix(".mp3")
        subprocess.run(["ffmpeg", "-i", vid, "-vn", "-acodec", "mp3", "-y", str(audio)], check=True)
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

@app.command()
def gif(vid: Path):
    if vid.suffix.lower() in formats:
        gif=vid.with_suffix(".gif")
        subprocess.run(["ffmpeg", "-i", vid, "-t", "3", "-vf", "scale=320:-1", "-y", str(gif)], check=True)
    else:
        print("plz enter a proper video format")

@app.command()
def mute(vid: Path):
    if vid.suffix.lower() in formats:
        mute=vid.with_stem(f"{vid.stem}_muted").with_suffix(vid.suffix)
        subprocess.run(["ffmpeg", "-i", vid, "-c", "copy", "-an", "-y", str(mute)], check=True)
    else:
        print("plz enter a proper video format")

if __name__=="__main__":
  app()
