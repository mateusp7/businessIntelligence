from connection_data_base.connection_data_base import conectar
from mysql.connector import Error
from utils.createDimmensionsTables import createUniqueDimmensionTable
from utils.createDimmensionsTables import createComorbidadeDimmensionTable

from utils.createBigTable import createBigWithMultiplesCollumns
from utils.createBigTable import insertComorbidadeInBigTable
from utils.updateBigTable import updateBigTable
connection = conectar()
cursor = connection.cursor()

if connection:
    try:
        createBigWithMultiplesCollumns(tablename="covidbigtable", column_names=['Municipio', 'Bairro', 'Sexo',
                                                                                'FaixaEtaria'])

        createUniqueDimmensionTable(tablename="municipioLocalidade", collumnname="municipio", collumnincsv="Municipio")
        createUniqueDimmensionTable(tablename="bairroLocalidade", collumnname="bairro", collumnincsv="Bairro")
        createUniqueDimmensionTable(tablename="genero", collumnname="genero", collumnincsv="Sexo")
        createUniqueDimmensionTable(tablename="faixaEtaria", collumnname="faixaEtaria", collumnincsv="FaixaEtaria")
        createComorbidadeDimmensionTable(tablename="comorbidade", collumnname="comorbidade")
        insertComorbidadeInBigTable()

        updateBigTable(tableforjoin="comorbidade", collumnincovidbigtable="Comorbidade",
                       collumnintableforjoin="comorbidade")
        # updateBigTable(tableforjoin="genero", collumnincovidbigtable="Sexo",
        #                collumnintableforjoin="genero")
        # updateBigTable(tableforjoin="faixaetaria", collumnincovidbigtable="FaixaEtaria",
        #                collumnintableforjoin="faixaEtaria")
        # updateBigTable(tableforjoin="bairrolocalidade", collumnincovidbigtable="Bairro",
        #                collumnintableforjoin="bairro")
        # updateBigTable(tableforjoin="municipiolocalidade", collumnincovidbigtable="Municipio",
        #                collumnintableforjoin="municipio")
        # updateBigTable(tableforjoin="comorbidade", collumnincovidbigtable="Comorbidade",
        #                collumnintableforjoin="comorbidade")

        print('Todos os processos foram realizar com sucesso!!!')

    except Error as e:
        print("Error while connecting to MySQL", e)
