import time
import mysql.connector
import tkinter as tk
from tkinter import ttk, Tk, Label, Listbox, Scrollbar, Frame, Button, END, messagebox
from entities.Animais import Animais
from repositories.AnimaisRepository import *

menus = ['1 - Cadastrar Funcionários', '2 - Ver Funcionários', '3 - Listar Visitantes',
         '4 - Cadastro de Visitantes', '5 - Compra de Ingressos', '6 - Ver peixes',
         '7 - Ver mamíferos', '8 - Ver aves', '9 - Cadastrar Animais', '10 - Listar Animais',
         '11 - Excluir animal', '12 - Sair']

ingressos = ['1 - PASSEIO COMPLETO COM GUIAS E ALIMENTAÇÃO: R$ 100,00', '2 - PASSEIO COM GUIAS: R$ 70,00',
             '3 - PASSEIO SEM GUIAS: R$ 50,00']


def leia_int(msg):
    """
    Método para ler um número inteiro

    :param msg: recebe um número para verificação de menu
    :return: retorna 0
    """
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('Usuário não digitou esse número')
            return 0
        else:
            return numero


def linha():
    """
    Método para criar uma separação de menu.

    :return: retorna o caractere " - " 50 vezes.
    """
    return '-' * 50


def cabecalho(txt):
    """
    Método para criar um cabeçalho organizado

    :param txt: Recebe uma frase para ser inserida no cabeçalho.
    :return: retorna a frase centralizada em exatamente 50 caracteres.
    """
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    """
    Método que organiza a criação de menus.

    :param lista: recebe a lista de opções.
    :return: retorna a opção escolhida pelo usuário
    """
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{item}')
        c += 1
    print(linha())
    opcao = leia_int('Sua opção: ')
    return opcao


def cadastrar_funcionarios_gui():
    """
    Método para criar uma interface para cadastrar um funcionário
    :return: void
    """
    global nome_caixa, idade_caixa, cpf_caixa, matricula_caixa

    # Criar a janela na interface gráfica
    janela_cadastro = tk.Tk()
    janela_cadastro.title('Cadastro de funcionários')

    # Adicionar widgets
    nome_label = tk.Label(janela_cadastro, text='Nome:')
    nome_label.pack()

    nome_caixa = tk.Entry(janela_cadastro)
    nome_caixa.pack()

    idade_label = tk.Label(janela_cadastro, text='Idade:')
    idade_label.pack()

    idade_caixa = tk.Entry(janela_cadastro)
    idade_caixa.pack()

    cpf_label = tk.Label(janela_cadastro, text='CPF:')
    cpf_label.pack()

    cpf_caixa = tk.Entry(janela_cadastro)
    cpf_caixa.pack()

    matricula_label = tk.Label(janela_cadastro, text='Matrícula:')
    matricula_label.pack()

    matricula_caixa = tk.Entry(janela_cadastro)
    matricula_caixa.pack()

    cadastrar_button = tk.Button(janela_cadastro, text='Cadastrar', command=cadastrar_funcionarios)
    cadastrar_button.pack()

    janela_cadastro.mainloop()


def cadastrar_funcionarios():
    """
    Método para cadastrar um funcionário no sistema, por meio da interface anterior
    :return: void
    """
    try:
        nome = nome_caixa.get().upper()
        idade = int(idade_caixa.get())
        cpf = int(cpf_caixa.get())
        matricula = int(matricula_caixa.get())
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = f"INSERT INTO funcionarios(func_nome, func_cpf, func_idade, func_matricula) VALUES ('{nome}', '{cpf}', '{idade}', '{matricula}');"
        cursor.execute(comando)
        conexao.commit()
        time.sleep(1)
        conexao.close()
    except ValueError:
        print('Erro! Digite valores numéricos para idade, CPF e Matrícula.')
    except KeyboardInterrupt:
        print('Dados não repassados')


def listar_funcionarios():
    """
    Método para listar os funcionários do zoológico por meio da interface tkinter.
    :return: Retorna a lista de funcionários no banco de dados
    """
    # Configuração da janela do Tkinter
    window = tk.Tk()
    window.title("Lista de Funcionários")
    window.geometry("500x500")

    # Criação do frame para exibir a lista de funcionários
    frame = ttk.Frame(window)
    frame.pack(pady=20)

    # Criação do cabeçalho da tabela
    ttk.Label(frame, text="Nome").grid(row=0, column=0)
    ttk.Label(frame, text="CPF").grid(row=0, column=1)
    ttk.Label(frame, text="Idade").grid(row=0, column=2)
    ttk.Label(frame, text="Matrícula").grid(row=0, column=3)

    # Conexão com o banco de dados e execução do comando SQL
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
    cursor = conexao.cursor()
    comando = 'SELECT * FROM zoo.funcionarios;'
    cursor.execute(comando)
    resposta = cursor.fetchall()

    # Loop para exibir cada linha da tabela
    for i, (id, nome, cpf, idade, matricula) in enumerate(resposta):
        ttk.Label(frame, text=nome).grid(row=i+1, column=0)
        ttk.Label(frame, text=cpf).grid(row=i+1, column=1)
        ttk.Label(frame, text=idade).grid(row=i+1, column=2)
        ttk.Label(frame, text=matricula).grid(row=i+1, column=3)

    # Botão para fechar a janela
    ttk.Button(window, text="Fechar", command=window.destroy).pack(pady=20)

    # Início do loop de eventos do Tkinter
    window.mainloop()


def listar_visitantes():
    """
    Método para listar os visitantes do zoológico por meio da interface tkinter.

    :return: None
    """
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
    cursor = conexao.cursor()
    comando = 'SELECT * FROM zoo.visitantes;'
    cursor.execute(comando)
    resposta = cursor.fetchall()

    # Criando a janela principal
    root = Tk()
    root.title('Lista de Visitantes')
    root.geometry('500x300')

    # Criando o frame principal
    frame_principal = Frame(root)
    frame_principal.pack(fill='both', expand=True)

    # Criando o rótulo para a lista de visitantes
    label_visitantes = Label(frame_principal, text='Lista de Visitantes')
    label_visitantes.pack(pady=10)

    # Criando a lista de visitantes
    listbox_visitantes = Listbox(frame_principal, width=60)
    listbox_visitantes.pack(side='left', fill='both', padx=10, pady=10)

    # Adicionando os visitantes à lista
    for id, nome, cpf, idade, ingresso in resposta:
        visitante = f'ID: {id} - Nome: {nome}, CPF: {cpf}, {idade} anos'
        listbox_visitantes.insert(END, visitante)

    # Criando a barra de rolagem para a lista de visitantes
    scrollbar_visitantes = Scrollbar(frame_principal, orient='vertical')
    scrollbar_visitantes.pack(side='right', fill='y', padx=10, pady=10)
    listbox_visitantes.config(yscrollcommand=scrollbar_visitantes.set)
    scrollbar_visitantes.config(command=listbox_visitantes.yview)

    # Criando o botão para fechar a janela
    botao_fechar = Button(frame_principal, text='Fechar', command=root.destroy)
    botao_fechar.pack(pady=10)

    root.mainloop()


def cadastrar_visitantes():
    """
    Método para cadastrar um visitante no zoológico e inserí-lo no banco de dados por meio da interface tkinter.
    :return: 0
    """
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        janela = tk.Tk()
        janela.title("Cadastro de Visitantes")

        nome_label = tk.Label(janela, text="Nome:")
        nome_label.pack()
        nome_caixa = tk.Entry(janela)
        nome_caixa.pack()

        idade_label = tk.Label(janela, text="Idade:")
        idade_label.pack()
        idade_caixa = tk.Entry(janela)
        idade_caixa.pack()

        cpf_label = tk.Label(janela, text="CPF (Somente números):")
        cpf_label.pack()
        cpf_caixa = tk.Entry(janela)
        cpf_caixa.pack()

        def cadastrar():
            try:
                nome = nome_caixa.get().upper()
                idade = int(idade_caixa.get())
                cpf = int(cpf_caixa.get())
                cursor = conexao.cursor()
                comando = f"INSERT INTO visitantes(vis_nome, vis_cpf, vis_idade, vis_ingresso) VALUES ('{nome}', " \
                          f"'{cpf}', '{idade}', '{0}');"
                cursor.execute(comando)
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Cadastro", f"{nome} inserido com sucesso!")
                janela.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Digite valores numéricos para idade e/ou CPF")
            except mysql.connector.Error as erro:
                messagebox.showerror("Erro", f"Erro ao inserir visitante: {erro}")

        cadastrar_button = tk.Button(janela, text="Cadastrar", command=cadastrar)
        cadastrar_button.pack()

        janela.mainloop()
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {erro}")
    except KeyboardInterrupt:
        print('Dados não repassados corretamente')


def compra_ingresso():
    """
    Método que faz uma validação de CPF do visitante para, após isso, realizar a compra do ingresso do mesmo.
    :return: 0
    """
    valida = int(input('Digite seu CPF: '))
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
        cursor.execute(comando)
        banco = cursor.fetchall()
        if len(banco) == 0:
            print('Lista de Visitantes vazia! ')
            return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(valida) == cpf_vis:
                print(f'Usuário {nome_vis} encontrado')
                resp = menu(ingressos)
                while resp != 1 or resp != 2 or resp != 3:
                    if resp == 1:
                        forma_pag = input('Forma de pagamento: ').upper()
                        if forma_pag == 'DINHEIRO':
                            recebido = int(input('Quantidade recebida: '))
                            if recebido == 100:
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido > 100:
                                troco = recebido - 100
                                print(f'Troco: R${troco}')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido < 100:
                                print('Dinheiro insuficiente!')
                                resp = 1
                        else:
                            print(f'Pagamento somente em Dinheiro!')
                            return
                    if resp == 2:
                        forma_pag = input('Forma de pagamento: ').upper()
                        if forma_pag == 'DINHEIRO':
                            recebido = int(input('Quantidade recebida: '))
                            if recebido == 70:
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido > 70:
                                troco = recebido - 70
                                print(f'Troco: R${troco}')
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido < 70:
                                print('Dinheiro insuficiente!')
                                resp = 2
                        else:
                            print(f'Pagamento somente em Dinheiro!')
                            return
                    if resp == 3:
                        forma_pag = input('Forma de pagamento: ').upper()
                        if forma_pag == 'DINHEIRO':
                            recebido = int(input('Quantidade recebida: '))
                            if recebido == 50:
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido > 50:
                                troco = recebido - 50
                                print(f'Troco: R${troco}')
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido < 50:
                                print('Dinheiro insuficiente!')
                                resp = 3
                        else:
                            print(f'Pagamento somente em dinheiro!')
                            return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(valida) != cpf_vis:
                print('Faça o cadastro antes de comprar o ingresso!')
                return
    except ValueError:
        print('Digite um valor numérico inteiro e sem hífens, barras ou espaços para o CPF!')
    except KeyboardInterrupt as erro:
        print(erro)


def valida_entrada_peixes():
    """
    Método que faz uma validação com o CPF do visitante e verifica se o mesmo tem um ingresso no banco de dados.
    Após a verificação validada o sistema o libera para ver os peixes.
    :return: 0
    """
    def buscar_visitante():
        """
        Faz uma varredura no banco de dados e retorna a lista de visitantes
        :return: lista de objetos no banco de dados
        """
        cpf_valida = entrada_cpf.get()
        try:
            conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
            cursor = conexao.cursor()
            comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
            cursor.execute(comando)
            banco = cursor.fetchall()
            encontrado = False
            for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
                if str(cpf_valida) == cpf_vis:
                    encontrado = True
                    if ingresso_vis == 1:
                        text.insert(tk.END, 'Visualizando Peixes\n')
                        text.insert(tk.END, "Aqui vão algumas curiosidades sobre os peixes: \n")
                        text.insert(tk.END,
                                    "Os peixes usam suas cordas vocais para emitir sons e se comunicarem com seus pares. É isso\n"
                                    "mesmo! Apesar de ser inaudível para nós, os peixes costumam se comunicar pela vocalização.\n")
                        text.insert(tk.END,
                                    "Alguma vez você já se perguntou se os peixes sentem frio? A resposta é sim! Inclusive \n"
                                    "quando a temperatura da água está extremamente baixa, o metabolismo desacelera \n e faz com "
                                    "que o peixe se movimente mais lentamente e, por vezes, perca até o apetite. \n")
                    else:
                        text.insert(tk.END, "Não tem ingresso, compre um antes de visitar os peixes!\n")
                    break
            if not encontrado:
                text.insert(tk.END, "CPF não encontrado, faça o cadastro antes de visitar os peixes!\n")
        except ValueError:
            text.insert(tk.END, 'Digite um valor numérico inteiro e sem hífens, barras ou espaços para o CPF!\n')
        except KeyboardInterrupt as erro:
            text.insert(tk.END, str(erro))

    janela = tk.Tk()
    janela.title('Validação de entrada - Peixes')

    # Widgets
    lbl_cpf = tk.Label(janela, text='CPF:')
    entrada_cpf = tk.Entry(janela)
    btn_buscar = tk.Button(janela, text='Buscar', command=buscar_visitante)
    text = tk.Text(janela, width=50, height=10)

    # Layout
    lbl_cpf.grid(row=0, column=0, padx=5, pady=5)
    entrada_cpf.grid(row=0, column=1, padx=5, pady=5)
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)
    text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    janela.mainloop()


def valida_entrada_mamiferos():
    """
    Método que faz uma validação com o CPF do visitante e verifica se o mesmo tem um ingresso no banco de dados.
    Após a verificação validada o sistema o libera para ver os mamíferos.
    :return: 0
    """
    def buscar_visitante():
        """
        Faz uma varredura no banco de dados e retorna a lista de visitantes
        :return: lista de objetos no banco de dados
        """
        cpf_valida = entrada_cpf.get()
        try:
            conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
            cursor = conexao.cursor()
            comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
            cursor.execute(comando)
            banco = cursor.fetchall()
            encontrado = False
            for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
                if str(cpf_valida) == cpf_vis:
                    encontrado = True
                    if ingresso_vis == 1:
                        text.insert(tk.END, 'Visualizando Mamíferos, não são magníficos?\n')
                        text.insert(tk.END, "Aqui vão algumas curiosidades sobre os mamíferos: \n")
                        text.insert(tk.END,
                                    "O morcego é o único mamífero capaz de voar. Esta habilidade foi desenvolvida ao longo do "
                                    "tempo, visando à sobrevivência da espécie.\n")
                        text.insert(tk.END,
                                    "Os mamíferos são os únicos animais que têm o corpo coberto de pelos, mas algumas espécies "
                                    "possuem apenas resquícios de pelos e uma camada de gordura subcutânea para o aquecimento "
                                    "do animal.\n")
                    else:
                        text.insert(tk.END, "Não tem ingresso, compre um antes de visitar os mamíferos!\n")
                    break
            if not encontrado:
                text.insert(tk.END, "CPF não encontrado, faça o cadastro antes de visitar os mamíferos!\n")
        except ValueError:
            text.insert(tk.END, 'Digite um valor numérico inteiro e sem hífens, barras ou espaços para o CPF!\n')
        except KeyboardInterrupt as erro:
            text.insert(tk.END, str(erro))

    janela = tk.Tk()
    janela.title('Validação de entrada - Mamíferos')

    # Widgets
    lbl_cpf = tk.Label(janela, text='CPF:')
    entrada_cpf = tk.Entry(janela)
    btn_buscar = tk.Button(janela, text='Buscar', command=buscar_visitante)
    text = tk.Text(janela, width=50, height=10)

    # Layout
    lbl_cpf.grid(row=0, column=0, padx=5, pady=5)
    entrada_cpf.grid(row=0, column=1, padx=5, pady=5)
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)
    text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    janela.mainloop()


def valida_entrada_aves():
    """
        Método que faz uma validação com o CPF do visitante e verifica se o mesmo tem um ingresso no banco de dados.
        Após a verificação validada o sistema o libera para ver as aves.
        :return: 0
        """
    def buscar_visitante():
        """
        Faz uma varredura no banco de dados e retorna a lista de visitantes
        :return: lista de objetos no banco de dados
        """
        cpf_valida = entrada_cpf.get()
        try:
            conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
            cursor = conexao.cursor()
            comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
            cursor.execute(comando)
            banco = cursor.fetchall()
            encontrado = False
            for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
                if str(cpf_valida) == cpf_vis:
                    encontrado = True
                    if ingresso_vis == 1:
                        text.insert(tk.END, 'Visualizando Aves, não são esplendorosas?\n')
                        text.insert(tk.END, "Aqui vão algumas curiosidades sobre as aves: \n")
                        text.insert(tk.END,
                                    "As aves são diferentes de todos os outros animais porque elas têm penas, bico, duas asas e "
                                    "não têm dentes.\n")
                        text.insert(tk.END,
                                    "A maioria das aves pode voar. Algumas podem nadar como o pingüim, e correr como o avestruz.")
                    else:
                        text.insert(tk.END, "Não tem ingresso, compre um antes de visitar as aves!\n")
                    break
            if not encontrado:
                text.insert(tk.END, "CPF não encontrado, faça o cadastro antes de visitar as aves!\n")
        except ValueError:
            text.insert(tk.END, 'Digite um valor numérico inteiro e sem hífens, barras ou espaços para o CPF!\n')
        except KeyboardInterrupt as erro:
            text.insert(tk.END, str(erro))

    janela = tk.Tk()
    janela.title('Validação de entrada - Aves')

    # Widgets
    lbl_cpf = tk.Label(janela, text='CPF:')
    entrada_cpf = tk.Entry(janela)
    btn_buscar = tk.Button(janela, text='Buscar', command=buscar_visitante)
    text = tk.Text(janela, width=50, height=10)

    # Layout
    lbl_cpf.grid(row=0, column=0, padx=5, pady=5)
    entrada_cpf.grid(row=0, column=1, padx=5, pady=5)
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)
    text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    janela.mainloop()


def zerar_ingressos():
    """
    Método que zera o ingresso de todos os visitantes no banco de dados ao fechar o programa.
    :return: vis_ingresso = 0
    """
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
    cursor = conexao.cursor()
    comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
    cursor.execute(comando)
    banco = cursor.fetchall()
    for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
        if ingresso_vis == 1:
            comando = f"update visitantes set vis_ingresso = '{0}' where vis_ingresso = '{1}';"
            cursor.execute(comando)
            conexao.commit()
            conexao.close()


class MyMethods:
    @staticmethod
    def cadastrar_animal():
        """
        Método estático para cadastrar animais no banco de dados.
        :return: 0
        """
        try:
            nome = input('Digite o nome do animal: ').upper()
            classe = input('Classe do animal: ').upper()
            idade = int(input('Idade: '))
            sexo = input('Sexo: ').upper()
            ani_cadastrar = Animais(nome, classe, idade, sexo)
            AnimaisRepository.create(ani_cadastrar)
        except ValueError as erro:
            print(erro)
        except KeyboardInterrupt as aviso:
            print(aviso)

    @staticmethod
    def listar_animais():
        """
        Método estático que deve solicitar que o repositorio realize uma consulta de todos os animais cadastrados
        no banco de dados. Listando cada animal e seu respectivo indice na lista de animais recebida pelo repositorio.
        """
        AnimaisRepository.listar(AnimaisRepository._read())

    @staticmethod
    def excluir_animal():
        """
        Método estático que deve solicitar ao usuario o nome de um Animal, pedir que o repositorio busque por este
        animal no banco, e caso o animal exista no banco de dados, deverá realize a remoção do animal no banco de
        dados.
        """
        try:
            busca = input('Digite o nome do animal: ').upper()
            AnimaisRepository.delete(busca)
        except ValueError as erro:
            print(erro)
        except KeyboardInterrupt as erro:
            print(erro)
