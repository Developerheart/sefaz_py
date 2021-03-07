class Cliente:
    def __init__(self, nome=str, sobrenome=str, nascimento=str, sexo=str, id_endereco=int):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nascimento = nascimento
        self.__sexo = sexo
        self.__endereco = id_endereco

    """
    :type nome: str
    :type endereco: int
    :type sexo: str
    """

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def sexo(self):
        return self.__sexo

    @property
    def endereco(self):
        return self.__endereco

    def save(self):
        import sqlite3
        conexao = sqlite3.connect('dadosCliente.bd')
        cursor = conexao.cursor()
        cursor.execute(''' 
        insert into Cliente (nome_cliente, sobrenome, data_nascimento, sexo, id_endereco) values (?,?,?,?,?)
        ''', [self.nome, self.sobrenome, self.nascimento, self.sexo, self.endereco])

        conexao.commit()
        cursor.close()
        conexao.close()
        print('salvo com sucesso')
