import os
import pygame

def getPath(*args): 
    #return os.path.join(os.getcwd().split()[0], os.path.join(*args))
    return os.path.join(os.path.join(*args))
# print("-----------------------------------")
# print(getPath("UNO", "images", "logo.png"))

# playBtPath = getPath("images","Buttons","blue","medium.jpg")
# bg_img_path=getPath("images","BGs","bg_start2.jpg")
# print(playBtPath)
# print(bg_img_path)