from tkinter import *
import tkinter
from datetime import datetime 

import pyglet
pyglet.font.add_file("font/digital-7.ttf")

###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor6

#Base do relogio
janela =  Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

def relogio():
    #Atribuindo hora da maquina local
    tempo=datetime.now()

    #Atribuindo hora,semana,mes,ano 
    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")
    
    l1.config(text=hora)
    #Atribuindo intervalo de tempo
    l1.after(200, relogio)
    l2.config(text=dia_semana +" "+ str(dia) + "/" 
              + str(mes) + "/" + str(ano))

#label do relogio Hora
l1=Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
#label do relogio dia da semana
l2=Label(janela, text="", font=("digital-7 17"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()