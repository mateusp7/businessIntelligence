from connection_data_base.connection_data_base import conectar
from mysql.connector import Error
from utils.createTable import createtable
from utils.createBigTable import createBigWithMultiplesCollumns
from utils.createTable import createtableComorbidade
connection = conectar()
cursor = connection.cursor()

print('oi')
if connection:
    try:
        createBigWithMultiplesCollumns(tablename="covidBigTable", column_names=['Municipio', 'Bairro', 'Sexo',
                                                                                'FaixaEtaria'])
        createtable(tablename="municipioLocalidade", collumnname="municipio", collumnincsv="Municipio")
        createtable(tablename="bairroLocalidade", collumnname="bairro", collumnincsv="Bairro")
        createtable(tablename="genero", collumnname="genero", collumnincsv="Sexo")
        createtable(tablename="faixaEtaria", collumnname="faixaEtaria", collumnincsv="FaixaEtaria")
        createtableComorbidade(tablename="comorbidade", collumnname="comorbidade")
    except Error as e:
        print("Error while connecting to MySQL", e)
