from mysql.connector import Error


def updateBigTable(connection, tableforjoin, collumnincovidbigtable, collumnintableforjoin):
    if connection:
        try:
            cursor = connection.cursor()
            timewait = "SET innodb_lock_wait_timeout = 10"
            cursor.execute(timewait)

            unsafeSet = "SET SQL_SAFE_UPDATES = 0"
            cursor.execute(unsafeSet)

            query = (f"UPDATE covidbigtable INNER JOIN {tableforjoin} ON covidbigtable.{collumnincovidbigtable} = "
                     f"{tableforjoin}.{collumnintableforjoin} SET covidbigtable.{collumnincovidbigtable} = {tableforjoin}.id")
            cursor.execute(query)

            connection.commit()
            print(f"Dados atualizados de {tableforjoin} para a covidbigtable")
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
