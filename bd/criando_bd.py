def cria_bd():
    import sqlite3

    conexao = sqlite3.connect('dadosCliente.bd')
    cursor = conexao.cursor()
    cursor.execute('''
            create table if not exists Endereco(
            id_endereco integer not null primary key autoincrement,
            logradouro TEXT not null,
            numero varchar not null,
            bairro varchar(255) not null,
            cidade varchar(100) not null,
            estado varchar(100) not null,
            cep varchar(30) not null   
            );        
        ''')

    cursor.execute('''
        create table IF NOT EXISTS Cliente  (

            id_cliente integer not null primary key autoincrement,
            nome_cliente varchar(255) not null,
            sobrenome varchar(255) not null,
            data_nascimento date not null,
            sexo varchar(30) not null,
            id_endereco varchar,
            foreign key(id_endereco) references Endereco(id_endereco)

        );
        ''')

    conexao.close()
    print('banco criando com sucesso')
