# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:10:32 2023

@author: Anay Bhandari
"""

from tkinter import *
import random

root = Tk()
root.title("PASSWORD GENERATOR") 
root.geometry("500x400")

user_input = Entry(root)
user_input.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_guessed_password = Label(root, bg = "yellow")
label_guessed_password.place(relx = 0.5, rely = 0.5, anchor = CENTER)

array_3d = [[["!", "@", "#", "$","%","^","&","*","()"], ["CLOUD", "WINTER", "SNOW", "SLUSHIE"], ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]]

def new_Password():
    random_number_1 = random.randint(0,8)
    random_number_2 = random.randint(0,3)
    random_number_3 = random.randint(0,25)
    
    letter_1 = str(array_3d[0][0][random_number_1])
    letter_2 = str(array_3d[0][1][random_number_2])
    letter_3 = str(array_3d[0][2][random_number_3])
    
    label_guessed_password["text"] = user_input.get() + letter_1 + letter_2 + letter_3 + letter_1

btn_generate = Button(root, text = "GENERATE PASSWORD", command = new_Password)
btn_generate.place(relx = 0.5, rely = 0.65, anchor = CENTER)
root.mainloop()