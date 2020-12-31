#!/usr/bin/env python3

import sys

LRC_LINE_START = 7

def init_ass(filename):
    contents = ("[Script Info]\n"
    "ScriptType: v4.00+\n\n" 
    "[V4+ Styles]\n" 
    "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, "  
    "OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, " 
    "ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
    "MarginR, MarginV, Encoding\n"
    "Style: Default,Arial,16,&Hffffff,&Hffffff,&H0,&H0,0,0,0,0,100,100,0,0,1,1,0,2,10,10,10,0\n\n"
    "[Events]\n"
    "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    
    f = open(filename, 'w')
    f.write(contents)
    return f

def make_ass_line(lyric, start, end):
    #Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
    line = ("Dialogue: 0,0:"+start+",0:"+end+",Default,,0,0,0,,{\\fad(500,500)}"+lyric+"\n")
    return line

# Return secs as 'mm:ss.ms'
def format_time(secs):
    mm = int(secs//60)
    mm = '0'+str(mm) if mm < 10 else str(mm)
    ss = int(secs%60)
    ss = '0'+str(ss) if ss < 10 else str(ss)
    ss = ss[:2]
    ms = str(secs%60)[3:5]
    
    return mm+":"+ss+"."+ms

def main(lrc_file):
    # Initialize .ass file
    ass_name = lrc_file[0:lrc_file.index('.lrc')] + '.ass'
    ass_file = init_ass(ass_name)

    # Read lrc file
    f = open(lrc_file, "r")
    lrc = f.read().splitlines()
    f.close()
    
    line_num = LRC_LINE_START
    end_line = len(lrc) - 2
    
    # Convert each .lrc line to .ass line and write to file
    while (line_num < end_line):
        lyric = lrc[line_num][10:len(lrc[line_num])]
        lyric_start = lrc[line_num][1:9] #mm:ss.ms
        lyric_end = lrc[line_num+1][1:9]
        start_secs = int(lyric_start[:2])*60 + int(lyric_start[3:5]) + int(lyric_start[6:])/100
        end_secs = None
        
        if (lyric_end):
            end_secs = int(lyric_end[:2])*60 + int(lyric_end[3:5]) + int(lyric_end[6:])/100

        # lyric_start = current line start
        # lyric_end = min(next line start, current line start + 5 sec)
        if (not end_secs or end_secs - start_secs > 5):
            end_secs = start_secs + 5
            lyric_end = format_time(end_secs)

        ass_line = make_ass_line(lyric, lyric_start, lyric_end)
        ass_file.write(ass_line)
        
        line_num += 1

    ass_file.close()
    
# ./lrc.py <file.lrc>
if __name__ == "__main__":
    main(sys.argv[1])