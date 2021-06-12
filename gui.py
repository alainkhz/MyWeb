from os import name
from tkinter import font
from tkinter import*
import tkinter
from typing import Collection
from tkinter.font import*
from main import goods

#開檔案
main  = open("main.py",mode="a",encoding='utf-8')  


#視窗
gui = Tk()
gui.title("goods data")
gui.geometry("800x500+550+200")
gui.config(bg='#323232')


#lable name
Lname = Label(text="商品名稱:",font="微軟正黑體 20",bg="#323232",fg="white")
Lname.place(x=55,y=100)

#lable price
Lprice = Label(text="價格:",font="微軟正黑體 20",bg="#323232",fg="white")
Lprice.place(x=100,y=200)

#lable pic
Lpic = Label(text="圖片:",font="微軟正黑體 20",bg="#323232",fg="white")
Lpic.place(x=100,y=300)


#entry name
Ename = Entry(bg="skyblue")
Ename.place(x=200,y=100,height=40)

#entry price
Eprice = Entry(bg="skyblue")
Eprice.place(x=200,y=200,height=40)

#entry pic
Epic = Entry(bg="skyblue")
Epic.place(x=200,y=300,height=40)

#按鈕邏輯
def data ():
    name = Ename.get() 
    price = Eprice.get()
    pic = Epic.get()
    main.write("\n" + name + " = goods(" + "'" + name + "'" + "," + price + "," + "'" + pic + "'" + ")")

#button
but = Button(text="完成",font="500",command=data)
but.place(x=480,y=175,width=140,height=80)


gui.mainloop()

