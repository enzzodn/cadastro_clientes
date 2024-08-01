from customtkinter import *
from tkinter import *
from view.menu_principal import menu_principal
import time


credenciais = open('credenciais.txt', 'r')
login = credenciais.readlines()
usuario = login[0][:-1]
senha = login[1]


def show_password():
    if password.cget('show') == '':
        password.configure(show='*')
    else:
        password.configure(show='')

def verify_user():
    if user.get() == usuario and password.get() == senha:
        warning.configure(text='')
        janela_login.destroy()
        menu_principal()
    else:
        warning.configure(text=f'Usuário ou Senha informados estão incorretos\n Por favor, tente novamente!\n TENTATIVA {int(chances[0])+1} DE 3', text_color='red')
        chances[0]+=1
        if chances[0] == 4:
            time.sleep(1)
            janela_login.destroy()

# PREPARAÇÃO PRÉVIA
janela_login = CTk()
janela_login.geometry('350x300')
janela_login.title("-- LOGIN --")

texto = CTkLabel(janela_login, text='INFORME SUAS CREDENCIAIS ABAIXO')
texto.pack(padx=10, pady=10)

user = CTkEntry(janela_login, placeholder_text='Usuário')
user.pack(padx=10, pady=10)

password = CTkEntry(janela_login, placeholder_text='Senha', show= "*")
password.pack(padx=10, pady=10)

warning = CTkLabel(janela_login, text="")
warning.pack(pady=5)

mostrar_senha = CTkCheckBox(janela_login, text='Mostrar senha', width=15, command=show_password)
mostrar_senha.pack(padx = 10, pady = 10)

chances=[0]
botao = CTkButton(janela_login, text="ENTRAR", command=verify_user)
botao.pack(padx=10, pady=10)

janela_login.mainloop()