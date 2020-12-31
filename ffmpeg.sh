# Add fading subtitles from .ass file to a mp4 file
ffmpeg -i input.mp4 -vf subtitles=input.ass -c:a copy output.mp4
