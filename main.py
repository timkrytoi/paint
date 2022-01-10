from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image,ImageDraw
from random import *


def save():
    filename = f'image_{randint(0,10000)}.png'
    image1.save(filename)
    messagebox.showinfo('Сохранение',"Сохарненено под названием %s" %filename )


def activate_point(event):
    x1,y1 = (event.x-2),(event.y-2)
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_line(x1,y1,x2,y2,fill='black',width=5)
    draw.line((x1,y1,x2,y2),fill='black',width=5)

root = Tk()
root.title('рисовалка')
root.resizable(False,False)

cv = Canvas(root,width=1280,height=720)

image1 = PIL.Image.new('RGB',(1280,720),'white')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>',activate_point)
cv.pack(expand=1,fill=BOTH)

btn_save = Button(text='Сохранить',bg='black',fg='white',font=('Comic Sans MS',30),command=save)
btn_save.pack()

root.mainloop()