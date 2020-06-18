#!/usr/bin/python3
# -*- coding: utf-8 -*-


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
    "Warning",
    "Exit"
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
    'Juego 5',
    'Deseas Salir del juego?'
    'Advertencia',
    'Salir'
]

textApp = words

#------------------------------Class APP-------------------------------#
class MainWindow:
    
    def __init__(self, root, command, text):
        
        self.root = root
        self.command = command
        self.textApp = text
        root.title(textApp[2])
        root.geometry("450x350")
        root.resizable(0,0)

        #menu barr 
        barraMenu = Menu(self.root)
        self.root.config(menu=barraMenu)

        option01 = Menu(barraMenu, tearoff=0)
        option01.add_command(label="Information", command=self.showInfo)
        option01.add_command(label="Exit", command=command)
        barraMenu.add_cascade(label='Help', menu=option01)

        option02 = Menu(barraMenu, tearoff=0)
        option02.add_command(label="Spanish", command=self.languageEs)
        option02.add_command(label="English", command=self.languageEn)
        barraMenu.add_cascade(label=self.textApp[0], menu=option02)

        option03 = Menu(barraMenu, tearoff=0)
        option03.add_command(label="Guardianes del aire", command=self.info_game01)
        option03.add_command(label="Guardian del agua", command=self.info_game02)
        barraMenu.add_cascade(label='About Game', menu=option03)

        option04 = Menu(barraMenu, tearoff=0)
        option04.add_command(label="About of:", command=self.buttonLicence)
        option04.add_command(label="Help:", command=self.info_game02)
        barraMenu.add_cascade(label='Licence', menu=option04)

    def buttonLicence(self):
        messagebox.showwarning("License", "GNU licensed product")

    def languageEn(self):
        self.textApp = words
    
    def languageEs(self):
        self.textApp = palabras

    def info_game01(self):
         messagebox.showinfo("Information", """This game is about the safe of Trees....""")

    def info_game02(self):
         messagebox.showinfo("Information", """This game is about the safe of water....""")

    def showInfo(self):
         messagebox.showinfo("Information", """This app was developed with the purpose, to manage different game with  the same App, make it easier""")
   
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
    global textApp
    app = Tk()

    def function_buttonExit():
    
        valor = messagebox.askquestion(words[10], words[9])
    
        if(valor=="yes"):
            app.destroy()


    window01 = MainWindow(app, function_buttonExit, textApp)

    im = Image.open('assest/goku.png')
    ph = ImageTk.PhotoImage(im)
    
    ph2 = PhotoImage(file='assest/iconplay01.png')
    ph4 = PhotoImage(file='assest/iconplay02.png')
    ph3 = PhotoImage(file='assest/buttonExit.png')

    window01.background_Image(app, ph)
    
    button01 = window01.gameButton(app, words[4], 20, 20, launcher01, ph2)
    button02 = window01.gameButton(app, words[4], 190, 20, launcher02, ph4)
    button_exit = window01.gameButton(app, 'Exit', 180, 300, function_buttonExit, ph3)
    
    app.mainloop()
main()
