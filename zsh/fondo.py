import os, random
select = str ( random.randrange ( 28 ) )
# select = str ( 99 )
os.popen ( "wal -n -i Imagenes/" + select + '.jpg -q') 
os.popen ( "nitrogen --set-zoom-fill Imagenes/" + select + ".jpg" )
