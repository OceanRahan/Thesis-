import  os
import cv2
import numpy as np
from os.path import basename

path='detected_words'
count=0
done=0

for fileName in os.listdir('Word_Label'):
    done+=1

print(done)



for fileName in os.listdir(path):
    if count < done:
        count += 1
        #continue
    img = cv2.imread('detected_words/%s' % fileName, 0)
    if img is None:
        count += 1
        continue
    count += 1
    base=os.path.splitext(fileName)[0]
    print(base)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    f = open('Word_Label/%s.txt' % base, "w+")
    f.close()
    file = "notepad.exe Word_Label/%s.txt" % base
    os.system(file)



print(count)
