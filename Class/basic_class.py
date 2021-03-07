class Basic:

    @staticmethod
    def pesquisar(id_client):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        cursor = conexao.cursor()
        cursor.execute(''' 
        select * from Cliente inner join Endereco on Cliente.id_endereco = Endereco.id_endereco where id_cliente = ?''',
                       [id_client])
        dados_e = cursor.fetchall()

        cursor.close()
        conexao.close()
        return dados_e

    @staticmethod
    def excluir(id_to_delet, id_to_endereco):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        cursor = conexao.cursor()

        cursor.execute(''' 
                DELETE FROM Endereco WHERE id_endereco = ?
                ''', [id_to_endereco])
        cursor.execute(''' 
                        DELETE FROM Cliente WHERE id_cliente = ?
                        ''', [id_to_delet])

        conexao.commit()
        conexao.close()

        print('excluido com sucesso')

    @staticmethod
    def all():
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')

        cursor = conexao.cursor()
        cursor.execute(''' 
        select * from Cliente
        ''')
        dados_l = cursor.execute(''' select * from Cliente INNER JOIN Endereco ON Cliente.id_endereco = Endereco.id_endereco
        ''').fetchall()

        cursor.close()
        conexao.close()
        return dados_l

    @staticmethod
    def atualizar(id_client):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute(''' 
        select * from Cliente inner join Endereco on Cliente.id_endereco = Endereco.id_endereco where id_cliente = ?''',
                       [id_client])
        dados_e = cursor.fetchone()

        cursor.close()
        conexao.close()
        return dados_e


    @staticmethod
    def inserindo_att_cliente(id, nome, sobrenome, nascimento, sexo):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        cursor = conexao.cursor()
        cursor.execute(''' 
        UPDATE Cliente SET  nome_cliente= ?, sobrenome = ?, data_nascimento = ?, sexo = ? where id_cliente = ?
        ''', [nome, sobrenome, nascimento, sexo, id])

        conexao.commit()
        cursor.close()
        conexao.close()

        print('Cliente atualizado com sucesso')


    @staticmethod
    def inserindo_att_endereco(logradouro, numero, bairro, cidade, estado, cep, id):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        cursor = conexao.cursor()
        cursor.execute(''' 
                UPDATE Endereco SET  logradouro= ?, numero = ?, bairro = ?, cidade = ?, estado = ?, cep = ?  
                where id_endereco = ?''', [logradouro, numero, bairro, cidade, estado, cep, id])

        conexao.commit()
        cursor.close()
        conexao.close()

        print('endereço atualizado com sucesso')
