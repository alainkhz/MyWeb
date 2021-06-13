from os import name
import eel
import random
import os
import shutil

eel.init("web")

path="notyet"
@eel.expose
def py():
    for file_name in os.listdir(path):
        f = open("notyet\\"+file_name,mode="r",encoding="utf-8")
        f2 = open('C:\\game\\GitHub\\MyWeb\\檔案name.txt',"a",encoding="UTF-8")
        line = f.read()
        return line


    #移動檔案
    start = "C:\\game\\GitHub\\MyWeb\\notyet\\" + file_name
    to = "C:\\game\\GitHub\\MyWeb\\already\\" + file_name
    f.close()
    #shutil.move(start,to)
    
eel.start("alainWeb.html")