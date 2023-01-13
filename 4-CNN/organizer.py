import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shutil

path = "data//"
for CLASS in os.listdir(path):
    if not CLASS.startswith('.'):
        IMG_NUM = len(os.listdir(path + CLASS))
        for (n, FILE_NAME) in enumerate(os.listdir(path + CLASS)):
            img = path + CLASS + '/' + FILE_NAME
            if n < 5:
                shutil.copy(img, 'TEST/' + CLASS.upper() + '/' + FILE_NAME)
            elif n < 0.8*IMG_NUM:
                shutil.copy(img, 'TRAIN/'+ CLASS.upper() + '/' + FILE_NAME)
            else:
                shutil.copy(img, 'VAL/'+ CLASS.upper() + '/' + FILE_NAME)