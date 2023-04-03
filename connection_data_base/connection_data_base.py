import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        connection = mysql.connector.connect(host='localhost', database='covid_data', user='root', password='1234')
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Conectado com MySQL Server - Versão -> ", db_info)
            return connection
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
        return None


if __name__ == '__main__':
    conectar()
