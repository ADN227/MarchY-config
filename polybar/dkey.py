import os

read = str ( os.popen( "xkb-switch" ).readlines( ) )
dist = ""

i = 0
for C in read:
    if i < len ( read ) -4 and i > 1: 
        if C != '[' and C != ']' and C != "'":
            dist += C
    i+=1
if dist == "dvorak":
    print ( "EN > dvrk" )
elif dist == "latam(dvorak)":
    print ( "MX > dvrk" )
else:
    print ( "EN > qwrt" )
