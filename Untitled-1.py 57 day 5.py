import tkinter as tk #mengimport module tkinter
from tkinter import ttk #import ttk () widget 
from tkinter.messagebox import showinfo
# Init 
Window = tk . tk () # membuat object window berisi window tk() 
Window.configure (bg ="white") # mengubah background window menjadi putih 
Window. geometry ("300 x 200") # mengubah  size window dalam satuan pixel 
Window . resuzble  (False,False ) # window x,y  tidak bisa diresize 
Window.title ("sapa") # mengubah title window 
#variabeL
NAMA_DEPAN = tk stringVar () # membuat cosntant 