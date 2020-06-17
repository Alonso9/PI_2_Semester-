#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Example of button that open another window and minimize the father window
'''


from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

#-----------------------Path files-----------------------------------------#
currentPath = os.path.dirname(__file__) #path where is main.py
imagePath = os.path.join(currentPath, 'assets') #path where the images are

#---------------------------------------------------------------------------#
words = [
    'Language',
    'Accept',
    'Welcome to the App',
    'Choose a game',
    'Game 1',
    'Game 2',
    'Game 3',
    'Game 4',
    'Game 5',
    "Do you like to exit from app?",
    "Warning"
]

palabras = [
    'Idioma',
    'Aceptar',
    'bienvenido al la App',
    'Escoge un juego',
    'Juego 1',
    'Juego 2',
    'Juego 3',
    'Juego 4',
    'Juego 5'
]

textApp = words

#------------------------------Class APP-------------------------------#
class MainWindow:
    
    def __init__(self, root):
        
        self.root = root
        root.title(textApp[2])
        root.geometry("450x350")
        root.resizable(0,0)
        
    def background_Image(self, root, path_image):
        self.image = path_image #PhotoImage(file=path_image)
        
        self.background_label = Label(root, image=self.image).place(x=0, y=0)
                    
    def gameButton(self, root, text, posx, posy, command, image):
        
        self.image = image
        #button = Button(root, text=text, width=70, height=40, bd=3, image=image, command=command).grid(row=row, column=column, padx=12, pady=12, sticky="S")
        button = Button(root, text=text, width=70, height=40, bd=3, image=image, command=command).place(x=posx, y=posy)

#-------------------------------game functions------------------------------#

def launcher01():
    try:
        p = subprocess.run(["python", "GuardiandelAire/GuardiandelAire/main.py"])
    except:
        messagebox.showwarning(words[10], "Hubo un eror, porfavor cierre y abra la App de nuevo")

def launcher02():
    try:
        p = subprocess.run(["python", "GuardiandelAire/GuardiandelAire/main.py"])
    except:
        messagebox.showwarning(words[10], "Hubo un eror, porfavor cierre y abra la App de nuevo")


#-----------------------------------------------------------------#
def main():
    
    app = Tk()
    window01 = MainWindow(app)
    im = Image.open('assest/goku.png')
    ph = ImageTk.PhotoImage(im)
    
    ph2 = PhotoImage(file='assest/iconplay01.png')
    ph3 = PhotoImage(file='assest/buttonExit.png')
    
    
    def function_buttonExit():
    
        valor = messagebox.askquestion(words[10], words[9])
    
        if(valor=="yes"):
            app.destroy()

    window01.background_Image(app, ph)
    
    button01 = window01.gameButton(app, words[4], 20, 20, launcher01, ph2)
    button02 = window01.gameButton(app, words[4], 20, 90, launcher02, ph2)

    button_exit = window01.gameButton(app, 'Exit', 180, 300, function_buttonExit, ph3)
    
    app.mainloop()
main()
