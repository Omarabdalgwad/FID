def audio(vid: Path):
    ffmpeg()
    ckvideo(vid)
    audio=vid.with_suffix(".mp3")
    subprocess.run(["ffmpeg", "-i", str(vid), "-vn", "-acodec", "mp3", "-y", str(audio)], check=True)