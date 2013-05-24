#!/usr/bin/python
import sys,os,zipfile
from PIL import Image

## A script that takes a picture. Creates a html page of which when the font size is reduced, forms the original image
# As a argument takes a file of image and the text that you want to show in the html image
filename=sys.argv[1]
text=sys.argv[2]
text=text.upper()
size=128,128


def compressor(filename):
   zf=zipfile.ZipFile(filename+'.zip',mode='w')
   zf.write(filename+'.html',compress_type=zipfile.ZIP_DEFLATED)
   zf.close()

def appendZero(x):
   return '0'+x if len(x)==1 else x

def getHex(x):
   return hex(x)[2:].upper()


def transform(filename,text):
   index=-1
   maxi=len(text)
   size=160,160
   new=os.path.splitext(filename)[0]
   f=open(new+'.html','w')
   f.write("""<html>
<title>MagicPicture</title>
<body>
<div style='line-height:70%;font-size:13px;font-family: "Courier New", Courier, monospace;'>
""")
   im=Image.open(filename)
   im.thumbnail(size,Image.ANTIALIAS)
   
#   im.save(new+'-thumb.jpg',"JPEG")
   pix=im.load()
   size=im.size
   last=pix[0,0]
   string=''
   for y in range(size[1]):
      for x in range(size[0]):
         color = pix[x,y]
         index = (index+1)%maxi
         if last==color:
            string = string+text[index]
            last=color
            continue
         else:
            colorCode = '#'+''.join(map(appendZero,map(getHex,last)))
            line='<font color=\"'+colorCode+'\">'+string+'</font>'
            f.write(line)
            string=text[index]
         last=color
      f.write('<br />')
   f.write('</div></body></html>')
   f.close()
 #  compressor(new)

if __name__=="__main__":
   transform(filename,text)   
