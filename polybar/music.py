import os

player = str ( os.popen( "playerctl metadata -s title" ).readlines( ) )
played = str ( os.popen( "playerctl metadata -s artist" ).readlines( ) )
title = " > "
artist = ""

for y in range ( 2 ):
    i = 0
    xploit = ""
    if y == 0:
        xploit = player
    else:
        xploit = played
    for C in xploit:
        if i < len ( xploit ) -4 and i > 1: 
            if C != '[' and C != ']' and C != "'":
                if y == 0:
                    if i < 30:
                        title += C
                    elif i < 33:
                        title += '.'
                else:
                    if i < 30:
                        artist +=C
                    elif i < 33:
                        artist += '.'
            
        i+=1
if len ( artist ) > 0 or len ( title ) > 3:
    print ( artist + title )
else:
    print ( '---' )
