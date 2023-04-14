from connection_data_base.connection_data_base import conectar
from mysql.connector import Error
from utils.webScrapping import executeWebScrapping
from utils.createTables import createUniqueDimmensionTable
from utils.createTables import createComorbidadeDimmensionTable

from utils.createBigTable import createBigWithMultiplesCollumns
from utils.createBigTable import insertComorbidadeInBigTable
from utils.updateBigTable import updateBigTable
from utils.createTables import createFactTable


def run():
    connection = conectar()
    cursor = connection.cursor()
    executeWebScrapping()

    if connection:
        try:
            createBigWithMultiplesCollumns(connection=connection, tablename="covidbigtable",
                                           column_names=['Municipio', 'Bairro', 'Sexo', 'FaixaEtaria'])

            createUniqueDimmensionTable(connection=connection, tablename="municipioLocalidade", collumnname="municipio",
                                        collumnincsv="Municipio")
            createUniqueDimmensionTable(connection=connection, tablename="bairroLocalidade", collumnname="bairro",
                                        collumnincsv="Bairro")
            createUniqueDimmensionTable(connection=connection, tablename="genero", collumnname="genero",
                                        collumnincsv="Sexo")
            createUniqueDimmensionTable(connection=connection, tablename="faixaEtaria", collumnname="faixaEtaria",
                                        collumnincsv="FaixaEtaria")
            createUniqueDimmensionTable(connection=connection, tablename="tempo", collumnname="tempo",
                                        collumnincsv="DataObito")
            createComorbidadeDimmensionTable(connection=connection, tablename="comorbidade", collumnname="comorbidade")

            insertComorbidadeInBigTable(connection=connection)

            updateBigTable(connection=connection, tableforjoin="comorbidade", collumnincovidbigtable="Comorbidade",
                           collumnintableforjoin="comorbidade")
            updateBigTable(connection=connection, tableforjoin="genero", collumnincovidbigtable="Sexo",
                           collumnintableforjoin="genero")
            updateBigTable(connection=connection, tableforjoin="faixaetaria", collumnincovidbigtable="FaixaEtaria",
                           collumnintableforjoin="faixaEtaria")
            updateBigTable(connection=connection, tableforjoin="bairrolocalidade", collumnincovidbigtable="Bairro",
                           collumnintableforjoin="bairro")
            updateBigTable(connection=connection, tableforjoin="municipiolocalidade",
                           collumnincovidbigtable="Municipio",
                           collumnintableforjoin="municipio")
            updateBigTable(connection=connection, tableforjoin="comorbidade", collumnincovidbigtable="Comorbidade",
                           collumnintableforjoin="comorbidade")
            createFactTable(connection=connection)

            print('Todos os processos foram realizados com sucesso!!!')

            cursor.close()
            connection.close()

        except Error as e:
            print("Error while connecting to MySQL", e)
            cursor.close()
            connection.close()


run()
