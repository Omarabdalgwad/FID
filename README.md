# fid-ffmpeg
simple ffmpeg based cli for video operations

## installation 

- you need to install python >=3.9 : [Download Python](https://www.python.org/downloads/)
- install ffmpeg : [Download FFmpeg](https://www.ffmpeg.org/download.html)
- then install fid-cli with pip :
```bash
pip install fid-ffmpeg
```
## installation demo
https://github.com/user-attachments/assets/5c1bb2ac-1793-44b8-8240-bc71a1919d5a

## Commands
| Command | Description |
|---------|------------|
| `fid --help` | show help for fid cli |
| `fid info "videoPath"` | `to know all info about the video` |
| `fid audio "videoPath"` | `extract audio from the video` |
| `fid mute "videoPath"` | `mute the video` |
| `fid gif "videoPath"` | `make a gif from the video` |
| `fid frames "videoPath"` | `extract all video frames and add them in a folder`|
| `fid frames "videoPath"` | `extract all video frames and add them in a folder`|
| `fid compress "videoPath"` | `Compress the video to reduce its file size`|