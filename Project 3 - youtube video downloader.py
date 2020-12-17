from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('500x400')
root.title('Youtube Video Downloader')

Label_1=Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=65,y=20)

mylink=StringVar()

pastelink=Entry(root, width=65, textvariable=mylink)
pastelink.place(x=50, y=80)

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('C:/Users/Yash/Desktop'):
        os.makedirs('C:/Users/Yash/Desktop')
    ytvideo.download('C:/Users/Yash/Desktop') 

Button(root,text="Download Video", width=20, bg='red',fg="white", command=downloadVideo).place(x=170, y=130)

root.mainloop()