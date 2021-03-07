from bd.criando_bd import cria_bd
from class_all.basic_class import *
from class_all.Ccliente import Cliente
from class_all.Cendereco import Endereco
import os

if os.path.exists('banco_imobiliario.bd'):
    print('banco já criado')
else:
    cria_bd()

    while True:
        global opc
        ''' MENU '''
        print()
        print('[ 1 ] PARA LISTAR')
        print('[ 2 ] PARA PESQUISAR')
        print('[ 3 ] PARA INSERIR')
        print('[ 4 ] PARA ATUALIZAR')
        print()

        while True:
            try:
                opc = int(input('Escolha: '))

            except Exception as error:
                print(error)
                continue

            else:
                break

        if opc == 1:
            user = Basic()
            dados = user.all()
            for valor in dados:
                print(valor)

        elif opc == 2:
            id = 0
            while True:
                try:
                    id = int(input('Digite o id de pesquisa: '))

                except Exception as error:
                    print(error)
                    continue

                else:
                    break
            user = Basic()

            dadosALL = user.pesquisar(id_client=id)
            print()
            if dadosALL == ([]):
                print('USER NÃO ENCONTRADO')
            else:
                print(dadosALL)
            print()


        elif opc == 3:

            ''' add '''
            print('Dados da pessoa!!')
            nome = str(input('Digite o nome: '))
            sobrenome = str(input('Digite o sobrenome: '))
            nascimento = str(input('Digite a data de nascimento [dd/mm/aaaa]: '))
            sexo = str(input('Digite o sexo: '))
            print()

            print('sobre o endereço')

            logradouro = input('Digite o logradouro: ')
            numero = input('Digite o numero: ')
            bairro = input('Digite o bairro: ')
            cidade = input('Digite a cidade: ')
            estado = input('Digite o estado: ')
            cep = int(input('Digite o CEP: '))
            print()

            newEnd = Endereco(logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado,
                              cep=cep)
            id = newEnd.save_end()
            for valor in id:
                for var in valor:
                    id = var

            newUser = Cliente(nome=nome, sobrenome=sobrenome, nascimento=nascimento, sexo=sexo, id_endereco=id)
            newUser.save()


        elif opc == 4:

            ''' atualizar '''

            while True:
                try:
                    id_att = int(input('Digite o id a ser atualizado: '))

                except Exception as error:
                    print(error)

                else:
                    break

            newUser = Basic.atualizar(id_att)
            print(newUser[1])
            print()
            print(tuple(newUser))
            ''' update'''
            print('INSIRA OS DADOS ATUALIZADOS !!')
            nome = str(input(f'Digite o nome old[{newUser[1]}]: '))
            sobrenome = str(input(f'Digite o sobrenome old[{newUser[2]}]: '))
            nascimento = str(input(f'Digite a data de nascimento [dd/mm/aaaa]  old[{newUser[3]}]: '))
            sexo = str(input(f'Digite o sexo  old[{newUser[4]}]: '))
            id_endereco = newUser[5]
            print()

            print('sobre o endereço')

            logradouro = input(f'Digite o logradouro old[{newUser[7]}]: ')
            numero = input(f'Digite o numero  old[{newUser[8]}]: ')
            bairro = input(f'Digite o bairro  old[{newUser[9]}]: ')
            cidade = input(f'Digite a cidade  old[{newUser[10]}]: ')
            estado = input(f'Digite o estado  old[{newUser[11]}]: ')
            cep = int(input(f'Digite o CEP  old[{newUser[12]}]: '))
            print()

            Basic.inserindo_att_cliente(nome=nome, sobrenome=sobrenome, nascimento=nascimento, sexo=sexo, id=id_att)

            Basic.inserindo_att_endereco(numero=numero, logradouro=logradouro, bairro=bairro, cidade=cidade,
                                         estado=estado,
                                         cep=cep, id=id_endereco)



        elif opc not in [1, 2, 3, 4]:
            print('opção não encontrada!!! ')
