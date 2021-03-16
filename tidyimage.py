import sys 
import os
#sourcefolder = sys.argv[1]
sourcefolder = '/home/student/Pythonsem1/PROJECT/test directory'
#The Exif give several information about a pucture. Many of them are not usefull for our programme. We neet just the date. The date is in  the biblio tags     
from PIL import Image
from PIL import ExifTags
path=sourcefolder
content = []
images = []
print("All the files ending by '.jpg' in the directory and they subdirectories : " '\n')
# r corresponds to root ; d to directory and f to folder
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            images.append(os.path.join( r,file)) #very helpfull in the folowing lines
for f in images:
    print(f)

import pprint
from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag,tag)
        ret[decoded] = value
    return ret
fn = '/home/student/Pythonsem1/PROJECT/Tidyimage/tidyImages/Sony_HDR-HC3.jpg'
print('\n')
#pprint.pprint(get_exif(fn)) #inutile 

import shutil 

print("We are moving theses files from",sourcefolder )
#targetfolder = sys.argv[2]
targetfolder = '/home/student/Pythonsem1/PROJECT/test moving'
print("to the new directory : ",targetfolder)
for f in images :
	shutil.move(f,targetfolder)
print('the files has been succesfuly moved ')
		



