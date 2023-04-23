from datetime import datetime
from entities.my_methods import *
from time import sleep

while True:
    """
    Mostra se o ZOO está aberto (entre as 8:00 e 17:00 de Brasília)
    """
    data_atual = datetime.now()
    hora_at = data_atual.strftime("%H:%M:%S")
    hora = int(data_atual.strftime("%H"))
    print(f"Hora atual: {hora_at}")
    if 7 < hora < 17:
        zoo_aberto = True
        print('Zoo está aberto para visitações')
    else:
        zoo_aberto = False
        print('Zoo está fechado para visitações')
    if not zoo_aberto:
        print('Finalizando o Sistema!')
        sleep(1)
        break
    resposta = menu(menus)
    if resposta == 1:
        cadastrar_funcionarios_gui()
    elif resposta == 2:
        listar_funcionarios()
    elif resposta == 3:
        listar_visitantes()
    elif resposta == 4:
        cadastrar_visitantes()
    elif resposta == 5:
        compra_ingresso()
    elif resposta == 6:
        valida_entrada_peixes()
    elif resposta == 7:
        valida_entrada_mamiferos()
    elif resposta == 8:
        valida_entrada_aves()
    elif resposta == 9:
        MyMethods.cadastrar_animal()
    elif resposta == 10:
        MyMethods.listar_animais()
    elif resposta == 11:
        MyMethods.excluir_animal()
    elif resposta == 12:
        zerar_ingressos()
        print('Finalizando o Sistema!')
        sleep(1)
        break
    else:
        print('Erro! Botão inválido! Selecione dentre as opções de 1 - 12')
