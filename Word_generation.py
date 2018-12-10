import os
import cv2
import numpy as np
from collections import deque

path = 'C:/Images'
num_words = 1517
id = 100
space_bet_words = 7

for fileName in os.listdir(path):

    img = cv2.imread('C:/Images/%s' % fileName, 0)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # ret, mask = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    ret, mask = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # mask = cv2.fastNlMeansDenoising(mask,None,10,10,7,21)

    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    bit_val = 255
    count = 1517

    shape = mask.shape

    '''
    crop_img=mask[20:20+50,20:20+50] #co
    cv2.imshow('crop_img', crop_img)#co
    cv2.waitKey(0)#co
    '''

    print(shape)
    val = 0
    curx = 4
    cury = 4
    count = 0
    flag = 0
    mn = 12
    maximum = shape[1] / 5

    cnt = list()
    line_id = deque()

    for i in range(shape[0]):
        count = 0
        for j in range(shape[1]):
            if mask[i, j] == 0:
                count += 1

        cnt.append(count)
        # print(count)

    flag = 0
    prev = 0
    line_id.append(0)
    for i in range(1, len(cnt) - 1):
        proCur = cnt[i]
        if (proCur + cnt[i - 1] + cnt[i + 1]) <= maximum and flag == 1:
            line_id.append(i)
            flag = 0

            '''
            crop_img = mask[prev:i, 4:shape[1] - 1] 
            cv2.imshow('crop_img', crop_img)
            cv2.waitKey(0)
            '''
            prev = i

        if proCur >= maximum:
            flag = 1

    '''
    line_id.append(0)
    for i in range(0,shape[0]-0):
        count=0
        for j in range(0,shape[1]-0):
            if mask[i, j] == 0:
                count+=1

        if count<=mn and flag==0:

            continue
        if count>=mn and flag==1:

            continue
        if count<=mn and flag==1:
            line_id.append(i)

            id=line_id.popleft()
            crop_img = mask[id:i, 4:shape[1]-4]
            cv2.imshow('crop_img', crop_img)
            cv2.waitKey(0)
            val=1

            flag=0

        if count>=mn and flag==0:
            flag=1

    '''

    words = list()
    # print(len(line_id))
    prev = line_id.popleft()
    while len(line_id) > 0:
        cur = line_id.popleft()

        flag = 0

        word_id = list()

        for i in range(0, shape[1] - 2):
            count = 0
            for j in range(prev, cur + 1):
                if mask[j, i] == 0:
                    count += 1

            word_id.append(count)

        #  print(len(word_id))
        pro = 0
        flag = 0
        for i in range(2, len(word_id) - 2):
            proCur = word_id[i]
            if proCur <= 3 and word_id[i - 1] <= 3 and word_id[i + 1] <= 3 and word_id[i - 2] <= 3 and word_id[
                i + 2] <= 3 and flag == 1:
                words.append(((prev, cur), (pro, i)))
                flag = 0

                '''
                crop_img = mask[prev:cur, pro:i] #co
                cv2.imshow('crop_img', crop_img) #co
                cv2.waitKey(0) #co
                '''
                pro = i

            if proCur > 3:
                flag = 1

        # print(len(words))

        prev = cur

    for i in range(len(words)):
        crop_img = mask[words[i][0][0]:words[i][0][1], words[i][1][0]:words[i][1][1]]
        cv2.imshow('crop_img', crop_img)
        #cv2.waitKey(0)
        cv2.imwrite('detected_words/%d.jpg' % num_words, crop_img)
        num_words += 1

print(count)
