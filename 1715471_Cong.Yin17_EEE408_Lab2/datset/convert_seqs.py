#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv


def save_img(dname, fn, i, frame):
    cv.imwrite('{}/{}_{}_{}.jpeg'.format(
        out_dir, os.path.basename(dname),
        os.path.basename(fn).split('.')[0], i), frame)

out_dir = '/home/deeplearning_2/congyin.2017/lab2/py-faster-rcnn/data/caltechimage'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for dname in sorted(glob.glob('/home/deeplearning_2/Data/set*')):
    for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
        cap = cv.VideoCapture(fn)
        i = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            save_img(dname, fn, i, frame)
            i += 1
        print(fn)
