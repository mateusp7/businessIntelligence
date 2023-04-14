# from connection_data_base.connection_data_base import conectar
# from mysql.connector import Error
# from utils.createDimmensionsTables import createUniqueDimmensionTable
# from utils.createDimmensionsTables import createComorbidadeDimmensionTable
#
# from utils.createBigTable import createBigWithMultiplesCollumns
# from utils.createBigTable import insertComorbidadeInBigTable
# from utils.updateBigTable import updateBigTable
#
# connection = conectar()
# cursor = connection.cursor()
#
# if connection:
#     try:
#         createBigWithMultiplesCollumns(tablename="covidbigtable", column_names=['Municipio', 'Bairro', 'Sexo',
#                                                                                 'FaixaEtaria'])
#
#         createUniqueDimmensionTable(tablename="municipioLocalidade", collumnname="municipio", collumnincsv="Municipio")
#         createUniqueDimmensionTable(tablename="bairroLocalidade", collumnname="bairro", collumnincsv="Bairro")
#         createUniqueDimmensionTable(tablename="genero", collumnname="genero", collumnincsv="Sexo")
#         createUniqueDimmensionTable(tablename="faixaEtaria", collumnname="faixaEtaria", collumnincsv="FaixaEtaria")
#         createComorbidadeDimmensionTable(tablename="comorbidade", collumnname="comorbidade")
#         insertComorbidadeInBigTable()
#
#         updateBigTable(tableforjoin="comorbidade", collumnincovidbigtable="Comorbidade",
#                        collumnintableforjoin="comorbidade")
#
#         print('Todos os processos foram realizar com sucesso!!!')
#
#     except Error as e:
#         print("Error while connecting to MySQL", e)


from connection_data_base.connection_data_base import conectar
from mysql.connector import Error
from utils.createDimmensionsTables import createUniqueDimmensionTable
from utils.createDimmensionsTables import createComorbidadeDimmensionTable

from utils.createBigTable import createBigWithMultiplesCollumns
from utils.createBigTable import insertComorbidadeInBigTable
from utils.updateBigTable import updateBigTable


def run():
    connection = conectar()
    cursor = connection.cursor()

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
            createComorbidadeDimmensionTable(connection=connection, tablename="comorbidade", collumnname="comorbidade")
            insertComorbidadeInBigTable(connection=connection)

            # updateBigTable(connection=connection, tableforjoin="comorbidade", collumnincovidbigtable="Comorbidade",
            #                collumnintableforjoin="comorbidade")
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

            print('Todos os processos foram realizados com sucesso!!!')

            cursor.close()
            connection.close()

        except Error as e:
            print("Error while connecting to MySQL", e)
            cursor.close()
            connection.close()


run()
