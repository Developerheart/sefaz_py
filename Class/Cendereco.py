class Endereco:

    def __init__(self, logradouro=str, numero=str, bairro=str, cidade=str, estado=str, cep=int):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def numero(self):
        return self.__numero

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @property
    def cep(self):
        return self.__cep

    def save_end(self):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        cursor = conexao.cursor()

        cursor.execute('''
        insert into Endereco (logradouro, numero, bairro, cidade, estado, cep) values (?,?,?,?,?,?)
        ''', [self.logradouro, self.numero, self.bairro, self.cidade, self.estado, self.cep])
        conexao.commit()

        dados = cursor.execute(''' 
        select max(id_endereco) from Endereco
        ''').fetchall()
        cursor.close()
        conexao.close()
        print('salvo com sucesso')
        return dados
