from customtkinter import *
from model.funcoes_pandas import visualizar
from model.funcoes_pandas import cadastrar
from model.funcoes_pandas import alterar
from model.funcoes_pandas import apagar


def menu_principal():

    # PREPARAÇÃO PRÉVIA
    janela_menu = CTk()
    janela_menu.title('-- MENU PRINCIPAL --')
    janela_menu.geometry('350x320')
    
    #  ----------------------PRIMEIRO FRAME ----------------------
    frame = CTkFrame(janela_menu)
    frame.pack(pady=10)

    aviso = CTkLabel(frame, text='COMANDOS NO BANCO DE DADOS', text_color='brown')
    aviso.pack(padx=10, pady=10)

    #  ----------------------SEGUNDO FRAME ----------------------
    frame1 = CTkFrame(janela_menu)
    frame1.pack(pady=10)

    visual = CTkButton(frame1, text='VISUALIZAR', command=visualizar)
    visual.pack(side='left', padx=10, pady=10)

    cadastro = CTkButton(frame1, text='CADASTRAR', command=cadastrar)
    cadastro.pack(side='left', padx=10, pady=10)

    #  ----------------------TERCEIRO FRAME ----------------------
    frame2 = CTkFrame(janela_menu)
    frame2.pack(pady=10)

    alteracao = CTkButton(frame2, text='ALTERAR', command=alterar)
    alteracao.pack(side='left', padx=10, pady=10)

    erase = CTkButton(frame2, text='APAGAR', command=apagar)
    erase.pack(side='left', padx=10, pady=10)

    #  ----------------------LINHAS DE SEPARAÇÃO ----------------------
    linhas = CTkLabel(janela_menu, text='-'*70, text_color='brown')
    linhas.pack(padx=5, pady=5)

    #  ----------------------QUARTO FRAME ----------------------
    frame3 = CTkFrame(janela_menu)
    frame3.pack(pady=10)

    sair = CTkButton(frame3, text='SAIR', command=janela_menu.destroy)
    sair.pack(padx=10, pady=10)

    # voltar = CTkButton(frame3, text='VOLTAR')
    # voltar.pack(padx=10, pady=10)

    janela_menu.mainloop()