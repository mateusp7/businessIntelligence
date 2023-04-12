from connection_data_base.connection_data_base import conectar
from mysql.connector import Error

connection = conectar()
cursor = connection.cursor()


def updateBigTable(tableforjoin, collumnincovidbigtable, collumnintableforjoin):
    if connection:
        try:
            timewait = "SET innodb_lock_wait_timeout = 10"
            cursor.execute(timewait)

            unsafeSet = "SET SQL_SAFE_UPDATES = 0"
            cursor.execute(unsafeSet)

            query = (f"UPDATE covidbigtable INNER JOIN {tableforjoin} ON covidbigtable.{collumnincovidbigtable} = "
                     f"{tableforjoin}.{collumnintableforjoin} SET covidbigtable.{collumnincovidbigtable} = {tableforjoin}.id")
            cursor.execute(query)

            print(f"Dados atualizados de {tableforjoin} para a covidbigtable")
            connection.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
