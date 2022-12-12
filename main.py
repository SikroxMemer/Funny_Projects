from tkinter import *
from playsound import playsound
import os as OS


Path = "100.wav"
Image = "Troll.png"

main_root = Tk()
main_root.title('Troll ?')
icon = PhotoImage(file=Image)
main_root.iconphoto(True,icon)

def troll():
    global Path
    playsound(Path)
    OS.system("shutdown -l")
    main_root.destroy()

image = PhotoImage(file=Image)
button_1 = Button(main_root , text="Click Me !" , command=troll)
button_1.config(
                fg='black' , 
                bg='white' , 
                activebackground='#FA2E85' , 
                activeforeground='#82FA2E' , 
                font=('Arial',50),
                image=image,
                compound='left'
                )

button_1.pack()
main_root.mainloop()