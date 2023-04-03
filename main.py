from connection_data_base.connection_data_base import conectar
from mysql.connector import Error
from utils.createTable import createtable

connection = conectar()
cursor = connection.cursor()


if connection:
    try:
        createtable(tablename="municipioLocalidade", collumnname="municipio", collumnincsv="Municipio")
        createtable(tablename="municipioBairro", collumnname="bairro", collumnincsv="Bairro")
        createtable(tablename="genero", collumnname="genero", collumnincsv="Sexo")
        createtable(tablename="faixaEtaria", collumnname="faixaEtaria", collumnincsv="FaixaEtaria")
    except Error as e:
        print("Error while connecting to MySQL", e)
