# Vinyl Videos

Add fading subtitles to a music video file to sync with the music played on vinyl.

1. Use GarageBand to record the vinyl and export to an audio file.
    - Circles_SideD.m4a
2. Gather the lyrics for the side of the record.
    - Circles_SideD.txt
3. Use lyrics, audio file and http://www.lrcgenerator.com/ to generate .lrc file.
    - Circles_SideD.lrc
4. Use lrc.py to generate .ass file for fading subtitles effect.
    - Circles_SideD.ass
5. Use ffmpeg to add fading subtitles to video file.
    - ffmpeg.sh
