#pil and pyscreenshot module need to be installed
import pyscreenshot
import time
#grab whole page
img=pyscreenshot.grab()
img.show()
img.save('s1.png')
#grab a part of a page
img=pyscreenshot.grab(bbox=(10,10,500,500))
img.show()
img.save('s2.png')
print('Oops just Grabbed few Screenshots from your page')
print('wanna check it, go to documents-->python_projects-->u found me')
input()
