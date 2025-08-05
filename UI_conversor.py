from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox

import requests

lista = ['EUR', 'USD', 'BRL']

#cores
branco = '#ffffff'
azul = '#40596b'
vermelho = '#b53128'
perto = '#02040d'

#tela
tela = Tk()
tela.geometry('250x350+550+200')
tela.wm_resizable(width=False, height=False)
tela.title('Convertor de Moeda')

#titulo de inicio

lb_titulo_ = Label(bg=azul)
lb_titulo_.place(width=380, height=45, x=0, y=0)
lb_titulo = Label(text='Conversor de Moeda', font='Time 10 bold', fg=branco,bg=azul)
lb_titulo.place(width=150, height=30, x=125, y=25, anchor='center')

label_de = Label(tela, text='De:', font='Time 11 bold', anchor='w')
label_de.place(width=100, height=20, x=10, y=130)
moeda_de = ttk.Combobox(tela, font='Time 11 bold', justify=CENTER)
moeda_de.place(width=100, height=30, x=10, y=150)
moeda_de['values'] = (lista)

label_de_ = Label(tela, text='Para:', font='Time 11 bold', anchor='w')
label_de_.place(width=100, height=20, x=150, y=130)
moeda_para = ttk.Combobox(tela, font='Time 11 bold', justify=CENTER)
moeda_para.place(width=100, height=30, x=135, y=150)
moeda_para['values'] = (lista)

# Valor da coversão
valor_input = Entry(tela,font='Time 11 bold', justify=CENTER)
valor_input.place(width=80, height=30, x=85, y=200)

def converter():
    de = moeda_de.get()
    para = moeda_para.get()

    # request
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/{}'.format(de+'-'+para))
    cotacao = cotacao.json()
    cotacao_moeda = float(cotacao['{}'.format(de+para)]['bid'])

    #formula
    valor = float(valor_input.get())

    r = round(valor * cotacao_moeda,2)

    lb_conversor = Label(tela, text=f'{r}', font='Time 16 bold', fg=vermelho, anchor='center', padx=5)
    lb_conversor.place(width=200, height=30, x=40, y=90)



    conversao = Label(tela, text=f'conversão: {r}', font='Time 11 bold', anchor='center', fg=vermelho)
    conversao.place(width=200, height=30, x=23, y=90)


button = Button(tela,text='converter', command=converter, font='Time 14 bold', bg=azul,fg=branco)
button.place(width=230, height=30, x=10, y=300)

tela.mainloop()
