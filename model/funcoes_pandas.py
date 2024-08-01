import pandas as pd
from customtkinter import * 
from tkinter import * 


dict_clientes = [
    ["Ana Silva", "(11) 98765-4321", "123.456.789-01"],
    ["Carlos Souza", "(21) 91234-5678", "234.567.890-12"],
    ["Fernanda Lima", "(31) 99876-5432", "345.678.901-23"],
    ["João Oliveira", "(41) 97654-3210", "456.789.012-34"],
    ["Mariana Costa", "(51) 96543-2109", "567.890.123-45"],
]


try:
    df_clientes = pd.read_excel('df_clientes.xlsx')
except:
    df_clientes = pd.DataFrame(dict_clientes, columns=['NOME', 'TELEFONE', 'CPF'])


def visualizar():

    janela_visualizar = CTk()
    janela_visualizar.geometry('680x600')
    janela_visualizar.title('-- VISUALIZAÇÃO DE DADOS --')

    frame1 = CTkFrame(janela_visualizar)
    frame1.pack(padx=20, pady=20, expand=True, fill='both')

    df_dados = Text(frame1, font=("Courier", 12), wrap='none', bg='#9E9E9E', fg='black')
    df_dados.pack(fill='both', padx=20, pady=20)
    df_dados.insert(END, df_clientes.to_string())
    df_dados.configure(state='disabled')  

    frame2 = CTkFrame(janela_visualizar)
    frame2.pack(pady=10)

    voltar = CTkButton(frame2, text='VOLTAR', command=janela_visualizar.destroy)
    voltar.pack(side= 'left', padx=10, pady=10)

    janela_visualizar.mainloop()


def cadastrar():
    janela_cadastrar = CTk()
    janela_cadastrar.geometry('420x400')
    janela_cadastrar.title('-- CADASTRO DE CLIENTES --')

    texto = CTkLabel(janela_cadastrar, text='INFORME OS DADOS DO CLIENTE ABAIXO')
    texto.pack(padx=10, pady=10)

    # -------------------- frame 1 --------------------
    frame_nome = CTkFrame(janela_cadastrar)
    frame_nome.pack(pady=10)

    texto_nome = CTkLabel(frame_nome, text='Nome completo: ')
    texto_nome.pack(padx=10, pady=10, side='left')

    nome = CTkEntry(frame_nome)
    nome.pack(padx=10, pady=10, side='right')

    # ----------------- AVISO ----------------
    texto = CTkLabel(janela_cadastrar, text="TELEFONE E CPF SEM FORMATAÇÃO [ ' - ' ; ' . ' ; ' ( ) ' ] \n SE CERTIFIQUE DE QUE O TELEFONE E O CPF POSSUEM 11 DÍGITOS", text_color='red')
    texto.pack(padx=5)

    # -------------------- frame 2 --------------------
    frame_telefone = CTkFrame(janela_cadastrar)
    frame_telefone.pack(pady=10)

    texto_telefone = CTkLabel(frame_telefone, text='Telefone com DDD: ')
    texto_telefone.pack(padx=10, pady=10, side='left')

    telefone = CTkEntry(frame_telefone)
    telefone.pack(padx=10, pady=10)

    # -------------------- frame 3 --------------------
    frame_cpf = CTkFrame(janela_cadastrar)
    frame_cpf.pack(pady=10)

    texto_cpf = CTkLabel(frame_cpf, text='CPF (Só números): ')
    texto_cpf.pack(padx=10, pady=10, side='left')

    cpf = CTkEntry(frame_cpf)
    cpf.pack(padx=10, pady=10)

    # -------------------- frame 4 --------------------
    def confirmar():

        def registrar():
            
            # COMANDOS DO 'BANCO DE DADOS'
            novo_dado = {'NOME':f'{nome.get()}', 'TELEFONE': f'{telefone_formatado}', 'CPF': f'{cpf_formatado}'}
            df_clientes.loc[len(df_clientes)] = novo_dado
            df_clientes.to_excel('df_clientes.xlsx', index=False)

            janela_confirmar.destroy()
            janela_cadastrar.destroy()

            janela_ok = CTk()
            janela_ok.title('-- CLIENTE CADASTRADO --')

            frame_ok = CTkFrame(janela_ok)
            frame_ok.pack(padx=20,pady=20)
 
            label = CTkLabel(frame_ok, text='✔', font=CTkFont(size=76))
            label.pack(pady=20)

            aviso = CTkLabel(frame_ok, text='CLIENTE CADASTRADO COM SUCESSO!', text_color='green')
            aviso.pack(padx=20, pady=20)

            aviso = CTkLabel(frame_ok, text='Clique abaixo para voltar ao menu principal')
            aviso.pack(padx=20, pady=20)

            voltar_menu = CTkButton(frame_ok, text='VOLTAR', command=janela_ok.destroy)
            voltar_menu.pack(padx=10, pady=10)

            janela_ok.mainloop()
            

        if len(list(telefone.get())) != 11 or len(list(cpf.get())) != 11:
            warning.configure(text= 'SEU TELEFONE OU SEU CPF NÃO POSSUEM O \nNÚMERO CORRETO DE DÍGITOS \n POR FAVOR, TENTE NOVAMENTE!', text_color='red')
        else:
        
            janela_confirmar = CTk()
            janela_confirmar.title('-- CONFIRMAR DADOS --')

            lt = list(telefone.get())
            telefone_formatado = f'({lt[0]}{lt[1]}) {lt[2]}{lt[3]}{lt[4]}{lt[5]}{lt[6]}-{lt[7]}{lt[8]}{lt[9]}{lt[10]}'

            lcpf = list(cpf.get())
            cpf_formatado = f'{lcpf[0]}{lcpf[1]}{lcpf[2]}.{lcpf[3]}{lcpf[4]}{lcpf[5]}.{lcpf[6]}{lcpf[7]}{lcpf[8]}-{lcpf[9]}{lcpf[10]}'

            titulo = CTkLabel(janela_confirmar, text='VOCÊ CONFIRMA OS DADOS ABAIXO?')
            titulo.pack(padx=20, pady=20)

            frm_nome = CTkFrame(janela_confirmar)
            frm_nome.pack(padx=10, pady=10)

            text1 = CTkLabel(frm_nome, text='NOME: ')
            text1.pack(side='left', padx=10, pady=10)
            text10 = CTkLabel(frm_nome, text=nome.get())
            text10.pack(side='left', padx=10, pady=10)

            frm_telefone = CTkFrame(janela_confirmar)
            frm_telefone.pack(padx=10, pady=10)

            text2 = CTkLabel(frm_telefone, text='TELEFONE: ')
            text2.pack(side='left', padx=10, pady=10)
            text20 = CTkLabel(frm_telefone, text=telefone_formatado)
            text20.pack(side='left', padx=10, pady=10)

            frm_cpf = CTkFrame(janela_confirmar)
            frm_cpf.pack(padx=10, pady=10)

            text3 = CTkLabel(frm_cpf, text='CPF: ')
            text3.pack(side='left', padx=10, pady=10)
            text30 = CTkLabel(frm_cpf, text=cpf_formatado)
            text30.pack(side='left', padx=10, pady=10)

            frame = CTkFrame(janela_confirmar)
            frame.pack(padx=10, pady=10)

            voltar = CTkButton(frame, text='CORRIGIR', command=janela_confirmar.destroy)
            voltar.pack(side= 'left', padx=10, pady=10)

            avancar = CTkButton(frame, text='REGISTRAR', command=registrar)
            avancar.pack(side= 'left', padx=10, pady=10)

            janela_confirmar.mainloop()
    
    warning = CTkLabel(janela_cadastrar, text='')
    warning.pack(pady=5)

    frame2 = CTkFrame(janela_cadastrar)
    frame2.pack(pady=10)

    voltar = CTkButton(frame2, text='VOLTAR', command=janela_cadastrar.destroy)
    voltar.pack(side= 'left', padx=10, pady=10)

    avancar = CTkButton(frame2, text='AVANÇAR', command=confirmar)
    avancar.pack(side= 'left', padx=10, pady=10)

    janela_cadastrar.mainloop()


def alterar():

    def mudar():
        try:

            num_indice = int(q2.get())

            if type(num_indice) == int:

                if num_indice >= len(df_clientes) or num_indice < 0:

                    aviso.configure(text='DIGITE UM\n VALOR VÁLIDO', text_color='red')

                else:

                    def nome():

                        def confirmar_nome():

                            def alterar_nome():

                                # COMANDOS DO 'BANCO DE DADOS'
                                df_clientes.loc[num_indice, 'NOME'] = nome.get()
                                df_clientes.to_excel('df_clientes.xlsx', index=False)
                                
                                janela_confirmar_nome.destroy()
                                janela_nome.destroy()
                                janela_change.destroy()
                                janela_alterar.destroy()

                                w_nome = CTk()
                                w_nome.title('-- NOVO NOME REGISTRADO --')

                                frame_ok = CTkFrame(w_nome)
                                frame_ok.pack(padx=20,pady=20)
                    
                                label = CTkLabel(frame_ok, text='✔', font=CTkFont(size=76))
                                label.pack(pady=20)

                                aviso1 = CTkLabel(frame_ok, text='NOVO NOME REGISTRADO COM SUCESSO!', text_color='green')
                                aviso1.pack(padx=20, pady=20)

                                aviso2 = CTkLabel(frame_ok, text='Clique abaixo para voltar ao menu principal')
                                aviso2.pack(padx=20, pady=5)

                                voltar_menu = CTkButton(frame_ok, text='VOLTAR', command=w_nome.destroy)
                                voltar_menu.pack(padx=10, pady=10)

                                w_nome.mainloop()

                            janela_confirmar_nome = CTk()
                            janela_confirmar_nome.title('-- CONFIRMAR NOME --')

                            frame_texto = CTkFrame(janela_confirmar_nome)
                            frame_texto.pack(padx=10, pady=10)

                            frame_principal = CTkFrame(janela_confirmar_nome)
                            frame_principal.pack(padx=10, pady=10)

                            nome_novo = Text(frame_texto, font=("Courier", 12), wrap='none', width=40, height=5, bg='#9E9E9E', fg='black')
                            nome_novo.pack(padx=20, pady=20)
                            nome_novo.insert(END, nome.get())
                            nome_novo.configure(state='disabled')

                            text = CTkLabel(frame_principal, text='VOCÊ CONFIRMA O NOME ACIMA?')
                            text.pack(padx=10, pady=10)

                            gravar = CTkButton(frame_principal, text='GRAVAR', command=alterar_nome)
                            gravar.pack(padx=10, pady=10)

                            editar = CTkButton(frame_principal, text='EDITAR', command=janela_confirmar_nome.destroy)
                            editar.pack(padx=10, pady=10)

                            janela_confirmar_nome.mainloop()

                        janela_nome = CTk()
                        janela_nome.title('-- ALTERAR NOME --')

                        frame_nome = CTkFrame(janela_nome)
                        frame_nome.pack(padx=20, pady=20)
                        
                        frame_botao = CTkFrame(janela_nome)
                        frame_botao.pack(padx=20, pady=20)

                        texto_nome = CTkLabel(frame_nome, text='Nome completo: ')
                        texto_nome.pack(padx=10, pady=10, side='left')

                        nome = CTkEntry(frame_nome)
                        nome.pack(padx=10, pady=10, side='right')

                        registrar = CTkButton(frame_botao, text='REGISTRAR', command=confirmar_nome)
                        registrar.pack(padx=10, pady=10)

                        voltar_menu = CTkButton(frame_botao, text='VOLTAR', command=janela_nome.destroy)
                        voltar_menu.pack(padx=10, pady=10)

                        janela_nome.mainloop()

                    def telefone():

                        def confirmar_telefone():

                            def alterar_telefone():

                                # COMANDOS DO 'BANCO DE DADOS'
                                df_clientes.loc[num_indice, 'TELEFONE'] = telefone_formatado
                                df_clientes.to_excel('df_clientes.xlsx', index=False)
                                
                                janela_confirmar_telefone.destroy()
                                janela_telefone.destroy()
                                janela_change.destroy()
                                janela_alterar.destroy()

                                w_telefone = CTk()
                                w_telefone.title('-- NOVO TELEFONE REGISTRADO --')

                                frame_ok = CTkFrame(w_telefone)
                                frame_ok.pack(padx=20,pady=20)
                    
                                label = CTkLabel(frame_ok, text='✔', font=CTkFont(size=76))
                                label.pack(pady=20)

                                aviso1 = CTkLabel(frame_ok, text='NOVO TELEFONE REGISTRADO COM SUCESSO!', text_color='green')
                                aviso1.pack(padx=20, pady=20)

                                aviso2 = CTkLabel(frame_ok, text='Clique abaixo para voltar ao menu principal')
                                aviso2.pack(padx=20, pady=5)

                                voltar_menu = CTkButton(frame_ok, text='VOLTAR', command=w_telefone.destroy)
                                voltar_menu.pack(padx=10, pady=10)

                                w_telefone.mainloop()

                            janela_confirmar_telefone = CTk()
                            janela_confirmar_telefone.title('-- CONFIRMAR TELEFONE --')

                            frame_texto = CTkFrame(janela_confirmar_telefone)
                            frame_texto.pack(padx=10, pady=10)

                            frame_principal = CTkFrame(janela_confirmar_telefone)
                            frame_principal.pack(padx=10, pady=10)

                            lt = list(telefone.get())
                            telefone_formatado = f'({lt[0]}{lt[1]}) {lt[2]}{lt[3]}{lt[4]}{lt[5]}{lt[6]}-{lt[7]}{lt[8]}{lt[9]}{lt[10]}'

                            telefone_novo = Text(frame_texto, font=("Courier", 12), wrap='none', width=40, height=5, bg='#9E9E9E', fg='black')
                            telefone_novo.pack(padx=20, pady=20)
                            telefone_novo.insert(END, telefone_formatado)
                            telefone_novo.configure(state='disabled')

                            text = CTkLabel(frame_principal, text='VOCÊ CONFIRMA O TELEFONE ACIMA?')
                            text.pack(padx=10, pady=10)

                            gravar = CTkButton(frame_principal, text='GRAVAR', command=alterar_telefone)
                            gravar.pack(padx=10, pady=10)

                            editar = CTkButton(frame_principal, text='EDITAR', command=janela_confirmar_telefone.destroy)
                            editar.pack(padx=10, pady=10)

                            janela_confirmar_telefone.mainloop()

                        janela_telefone = CTk()
                        janela_telefone.title('-- ALTERAR TELEFONE --')

                        frame_telefone = CTkFrame(janela_telefone)
                        frame_telefone.pack(padx=20, pady=20)
                        
                        frame_botao = CTkFrame(janela_telefone)
                        frame_botao.pack(padx=20, pady=20)

                        texto_telefone = CTkLabel(frame_telefone, text='Telefone com DDD: ')
                        texto_telefone.pack(padx=10, pady=10, side='left')

                        telefone = CTkEntry(frame_telefone)
                        telefone.pack(padx=10, pady=10, side='right')

                        registrar = CTkButton(frame_botao, text='REGISTRAR', command=confirmar_telefone)
                        registrar.pack(padx=10, pady=10)

                        voltar_menu = CTkButton(frame_botao, text='VOLTAR', command=janela_telefone.destroy)
                        voltar_menu.pack(padx=10, pady=10)

                        janela_telefone.mainloop()

                    def cpf():

                        def confirmar_cpf():

                            def alterar_cpf():

                                # COMANDOS DO 'BANCO DE DADOS'
                                df_clientes.loc[num_indice, 'CPF'] = cpf_formatado
                                df_clientes.to_excel('df_clientes.xlsx', index=False)
                                
                                janela_confirmar_cpf.destroy()
                                janela_cpf.destroy()
                                janela_change.destroy()
                                janela_alterar.destroy()

                                w_cpf = CTk()
                                w_cpf.title('-- NOVO CPF REGISTRADO --')

                                frame_ok = CTkFrame(w_cpf)
                                frame_ok.pack(padx=20,pady=20)
                    
                                label = CTkLabel(frame_ok, text='✔', font=CTkFont(size=76))
                                label.pack(pady=20)

                                aviso1 = CTkLabel(frame_ok, text='NOVO CPF REGISTRADO COM SUCESSO!', text_color='green')
                                aviso1.pack(padx=20, pady=20)

                                aviso2 = CTkLabel(frame_ok, text='Clique abaixo para voltar ao menu principal')
                                aviso2.pack(padx=20, pady=5)

                                voltar_menu = CTkButton(frame_ok, text='VOLTAR', command=w_cpf.destroy)
                                voltar_menu.pack(padx=10, pady=10)

                                w_cpf.mainloop()

                            janela_confirmar_cpf = CTk()
                            janela_confirmar_cpf.title('-- CONFIRMAR CPF --')

                            frame_texto = CTkFrame(janela_confirmar_cpf)
                            frame_texto.pack(padx=10, pady=10)

                            frame_principal = CTkFrame(janela_confirmar_cpf)
                            frame_principal.pack(padx=10, pady=10)

                            lcpf = list(cpf.get())
                            cpf_formatado = f'{lcpf[0]}{lcpf[1]}{lcpf[2]}.{lcpf[3]}{lcpf[4]}{lcpf[5]}.{lcpf[6]}{lcpf[7]}{lcpf[8]}-{lcpf[9]}{lcpf[10]}'
                            
                            cpf_novo = Text(frame_texto, font=("Courier", 12), wrap='none', width=40, height=5, bg='#9E9E9E', fg='black')
                            cpf_novo.pack(padx=20, pady=20)
                            cpf_novo.insert(END, cpf_formatado)
                            cpf_novo.configure(state='disabled')

                            text = CTkLabel(frame_principal, text='VOCÊ CONFIRMA O CPF ACIMA?')
                            text.pack(padx=10, pady=10)

                            gravar = CTkButton(frame_principal, text='GRAVAR', command=alterar_cpf)
                            gravar.pack(padx=10, pady=10)

                            editar = CTkButton(frame_principal, text='EDITAR', command=janela_confirmar_cpf.destroy)
                            editar.pack(padx=10, pady=10)

                            janela_confirmar_cpf.mainloop()

                        janela_cpf = CTk()
                        janela_cpf.title('-- ALTERAR CPF --')

                        frame_cpf = CTkFrame(janela_cpf)
                        frame_cpf.pack(padx=20, pady=20)
                        
                        frame_botao = CTkFrame(janela_cpf)
                        frame_botao.pack(padx=20, pady=20)

                        texto_cpf = CTkLabel(frame_cpf, text='CPF (Somente números): ')
                        texto_cpf.pack(padx=10, pady=10, side='left')

                        cpf = CTkEntry(frame_cpf)
                        cpf.pack(padx=10, pady=10, side='right')

                        registrar = CTkButton(frame_botao, text='REGISTRAR', command=confirmar_cpf)
                        registrar.pack(padx=10, pady=10)

                        voltar_menu = CTkButton(frame_botao, text='VOLTAR', command=janela_cpf.destroy)
                        voltar_menu.pack(padx=10, pady=10)

                        janela_cpf.mainloop()

                    janela_change = CTk()
                    janela_change.title('-- ALTERANDO DADOS --')

                    frame1 = CTkFrame(janela_change)
                    frame1.pack(padx=20, pady=20)

                    df_dados = Text(frame1, font=("Courier", 12), wrap='none', width=55, height=7, bg='#9E9E9E', fg='black')
                    df_dados.pack(padx=20, pady=20)
                    df_dados.insert(END, df_clientes.loc[num_indice].to_string())
                    df_dados.configure(state='disabled')

                    texto = CTkLabel(janela_change, text='CLIQUE NO BOTÃO CORRESPONDENTE AO DADO QUE VOCÊ DESEJA MODIFICAR')
                    texto.pack(padx=10, pady=10)

                    frame = CTkFrame(janela_change)
                    frame.pack(padx=20, pady=20)

                    frame_voltar = CTkFrame(janela_change)
                    frame_voltar.pack(padx=10, pady=10)

                    nome_botao = CTkButton(frame, text='NOME', command=nome)
                    nome_botao.pack(side='left', padx=10, pady=10)

                    tel_botao = CTkButton(frame, text='TELEFONE', command=telefone)
                    tel_botao.pack(side='left', padx=10, pady=10)

                    cpf_botao = CTkButton(frame, text='CPF', command=cpf)
                    cpf_botao.pack(side='left', padx=10, pady=10)

                    back = CTkButton(frame_voltar, text='VOLTAR', command=janela_change.destroy)
                    back.pack(side='left', padx=10, pady=10)

                    janela_change.mainloop()

        except:

            aviso.configure(text='DIGITE UM\n VALOR VÁLIDO', text_color='red')

    janela_alterar = CTk()
    janela_alterar.title('-- ALTERAÇÃO DE DADOS --')
    
    frame1 = CTkFrame(janela_alterar)
    frame1.pack(padx=20, pady=20, expand=True, fill='both')

    df_dados = Text(frame1, font=("Courier", 12), wrap='none', bg='#9E9E9E', fg='black')
    df_dados.pack(fill='both', padx=20, pady=20)
    df_dados.insert(END, df_clientes.to_string())
    df_dados.configure(state='disabled')

    frame_opcoes = CTkFrame(janela_alterar)
    frame_opcoes.pack(padx=10, pady=10)

    frame2 = CTkFrame(frame_opcoes)
    frame2.pack(padx=10, pady=10, side='right')

    q1 = CTkLabel(frame2, text='DIGITE ABAIXO O ÍNDICE DA LINHA\n A QUAL VOCÊ DESEJA ALTERAR: ')
    q1.pack(padx=10, pady=5)

    botao_apagar = CTkButton(frame2, text= 'ALTERAR', command=mudar)
    botao_apagar.pack(padx=10, pady=10, side='bottom')

    q2 = CTkEntry(frame2)
    q2.pack(padx=10, pady=10, side='bottom')

    voltar = CTkButton(frame_opcoes, text='VOLTAR', command=janela_alterar.destroy)
    voltar.pack(side= 'left', padx=10, pady=5)

    aviso = CTkLabel(frame_opcoes, text='')
    aviso.pack(side= 'left', padx=20, pady=20)

    janela_alterar.mainloop()


def apagar():

    def excluir():

        try:

            num_indice = int(q2.get())

            if type(num_indice) == int:

                if num_indice >= len(df_clientes) or num_indice < 0:

                    aviso.configure(text='DIGITE UM\n VALOR VÁLIDO', text_color='red')

                else:

                    def remover():

                        # COMANDOS DO 'BANCO DE DADOS'
                        df_clientes.drop(num_indice, axis=0, inplace=True)
                        df_clientes.reset_index(drop=True, inplace=True)
                        df_clientes.to_excel('df_clientes.xlsx', index=False)

                        janela_confirmar.destroy()
                        janela_apagar.destroy()

                        janela_ok = CTk()
                        janela_ok.title('-- CLIENTE EXCLUÍDO --')

                        frame_ok = CTkFrame(janela_ok)
                        frame_ok.pack(padx=20,pady=20)
            
                        label = CTkLabel(frame_ok, text='✔', font=CTkFont(size=76))
                        label.pack(pady=20)

                        aviso1 = CTkLabel(frame_ok, text='CLIENTE EXCLUÍDO COM SUCESSO!', text_color='red')
                        aviso1.pack(padx=20, pady=20)

                        aviso2 = CTkLabel(frame_ok, text='Clique abaixo para voltar ao menu principal')
                        aviso2.pack(padx=20, pady=5)

                        voltar_menu = CTkButton(frame_ok, text='VOLTAR', command=janela_ok.destroy)
                        voltar_menu.pack(padx=10, pady=10)

                        janela_ok.mainloop()

                    janela_confirmar = CTk()
                    janela_confirmar.title('-- CONFIRMAR DADOS --')

                    frame1 = CTkFrame(janela_confirmar)
                    frame1.pack(padx=20, pady=20)

                    df_dados = Text(frame1, font=("Courier", 12), wrap='none', width=55, height=7, bg='#9E9E9E', fg='black')
                    df_dados.pack(padx=20, pady=20)
                    df_dados.insert(END, df_clientes.loc[num_indice].to_string())
                    df_dados.configure(state='disabled')

                    texto = CTkLabel(janela_confirmar, text='CLIQUE NO BOTÃO ABAIXO PARA COMPLETAR A EXECUÇÃO')
                    texto.pack(padx=10, pady=10)

                    frame2 = CTkFrame(janela_confirmar)
                    frame2.pack(pady=20)

                    back = CTkButton(frame2, text='VOLTAR', command=janela_confirmar.destroy)
                    back.pack(side='left', padx=10, pady=10)

                    ok = CTkButton(frame2, text='CONFIRMAR', command=remover)
                    ok.pack(side='left', padx=10, pady=10)

                    janela_confirmar.mainloop()

        except:

            aviso.configure(text='DIGITE UM\n VALOR VÁLIDO', text_color='red')

    janela_apagar = CTk()
    janela_apagar.geometry('680x700')
    janela_apagar.title('-- EXCLUSÃO DE DADOS --')

    frame1 = CTkFrame(janela_apagar)
    frame1.pack(padx=20, pady=20, expand=True, fill='both')

    df_dados = Text(frame1, font=("Courier", 12), wrap='none', bg='#9E9E9E', fg='black')
    df_dados.pack(fill='both', padx=20, pady=20)
    df_dados.insert(END, df_clientes.to_string())
    df_dados.configure(state='disabled')

    frame_opcoes = CTkFrame(janela_apagar)
    frame_opcoes.pack(padx=10, pady=10)

    frame2 = CTkFrame(frame_opcoes)
    frame2.pack(padx=10, pady=10, side='right')

    q1 = CTkLabel(frame2, text='DIGITE ABAIXO O ÍNDICE DA LINHA\n A QUAL VOCÊ DESEJA EXCLUIR: ')
    q1.pack(padx=10, pady=5)

    botao_apagar = CTkButton(frame2, text= 'APAGAR', command=excluir)
    botao_apagar.pack(padx=10, pady=10, side='bottom')

    q2 = CTkEntry(frame2)
    q2.pack(padx=10, pady=10, side='bottom')

    voltar = CTkButton(frame_opcoes, text='VOLTAR', command=janela_apagar.destroy)
    voltar.pack(side= 'left', padx=10, pady=5)

    aviso = CTkLabel(frame_opcoes, text='')
    aviso.pack(side= 'left', padx=20, pady=20)

    janela_apagar.mainloop()


if __name__ == "__main__":
    # visualizar()
    # cadastrar()
    alterar()
    # apagar()