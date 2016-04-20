# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 07:40:13 2016

@author: Breno
"""

import tkinter as tk

class Tabuleiro:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        
        botao1= tk.Button(self.window)
        botao1.configure(width= 15, height= 10)
        botao1.grid(column= 0, row= 0)
        
        botao2= tk.Button(self.window)
        botao2.configure(width= 15, height= 10)
        botao2.grid(column= 1, row= 0)
        
        botao3= tk.Button(self.window)
        botao3.configure(width= 15, height= 10)
        botao3.grid(column= 2, row= 0)
        
        botao4= tk.Button(self.window)
        botao4.configure(width= 15, height= 10)
        botao4.grid(column= 0, row= 1)
        
        botao5= tk.Button(self.window)
        botao5.configure(width= 15, height= 10)
        botao5.grid(column= 1, row= 1)
        
        botao6= tk.Button(self.window)
        botao6.configure(width= 15, height= 10)
        botao6.grid(column= 2, row= 1)
        
        botao7= tk.Button(self.window)
        botao7.configure(width= 15, height= 10)
        botao7.grid(column= 0, row= 2)
        
        botao8= tk.Button(self.window)
        botao8.configure(width= 15, height= 10)
        botao8.grid(column= 1, row= 2)
        
        botao9= tk.Button(self.window)
        botao9.configure(width= 15, height= 10)
        botao9.grid(column= 2, row= 2)

    def iniciar(self):
        self.window.mainloop()
        
app= Tabuleiro()
app.iniciar()   

