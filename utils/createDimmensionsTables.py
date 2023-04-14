from df.covid_df import covid_df
from mysql.connector import Error

dataframe_covid = covid_df()


def createUniqueDimmensionTable(connection, tablename, collumnincsv, collumnname):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{tablename}'")
            result = cursor.fetchone()
            if result:
                drop_table = f"""DROP TABLE {tablename};"""
                cursor.execute(drop_table)
                connection.commit()
                print(f'Tabela {tablename} dropada com sucesso!')

            if tablename == 'tempo'.lower():
                create_table = f"""CREATE TABLE {tablename} (
                                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                                    dia VARCHAR(20) NOT NULL,
                                                    mes VARCHAR(20) NOT NULL,
                                                    ano VARCHAR(20) NOT NULL
                                                    ) """
                cursor.execute(create_table)
                print(f"Tabela {tablename} criada com sucesso!")

                dfresult = dataframe_covid[f"{collumnincsv}"].drop_duplicates().tolist()
                for df in dfresult:
                    dia, mes, ano = df.split('-')
                    query = f"INSERT INTO {tablename} (dia, mes, ano) VALUES (%s, %s, %s)"
                    values = (dia, mes, ano)
                    cursor.execute(query, values)
                connection.commit()
                print(f"\n{len(dfresult)} registros inseridos na tabela '{tablename}'.\n")
            else:
                create_table = f"""CREATE TABLE {tablename} (
                                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                                    {collumnname} VARCHAR(255) NOT NULL
                                                    ) """
                cursor.execute(create_table)
                print(f"\nTabela {tablename} criada com sucesso.\n")

                dfresult = dataframe_covid[f"{collumnincsv}"].drop_duplicates().tolist()
                for df in dfresult:
                    query = f"INSERT INTO {tablename} ({collumnname}) VALUES (%s)"
                    values = (df,)
                    cursor.execute(query, values)
                connection.commit()
                print(f"\n{len(dfresult)} registros inseridos na tabela '{tablename}'.\n")
        except Error as e:
            print("Error while connecting to MySQL", e)


def createComorbidadeDimmensionTable(connection, tablename, collumnname):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{tablename}'")
            result = cursor.fetchone()
            if result:
                drop_table = f"""DROP TABLE {tablename};"""
                cursor.execute(drop_table)
                connection.commit()
                print(f'Tabela {tablename} dropada com sucesso!')

            create_table = f"""CREATE TABLE {tablename} (
                                                id INT AUTO_INCREMENT PRIMARY KEY,
                                                {collumnname} VARCHAR(255) NOT NULL
                                                ) """
            cursor.execute(create_table)
            connection.commit()
            print(f"Tabela {tablename} criada com sucesso ")

            for df in ["Sim", "Não"]:
                query = f"INSERT INTO {tablename} ({collumnname}) VALUES (%s)"
                values = (df,)
                cursor.execute(query, values)
            connection.commit()
            print(f"Registros inseridos na tabela '{tablename}'.\n")
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
