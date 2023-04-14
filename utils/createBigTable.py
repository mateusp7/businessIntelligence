from df.covid_df import covid_df
from mysql.connector import Error

dataframe_covid = covid_df()


def createBigWithMultiplesCollumns(connection, tablename, column_names):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{tablename}'")
            result = cursor.fetchone()
            if result:
                drop_table = f"""DROP TABLE {tablename};"""
                cursor.execute(drop_table)
                connection.commit()
                print(f'\nTabela {tablename} dropada com sucesso!')

            column_definitions = [f"{name} VARCHAR(255) NOT NULL DEFAULT 'Desconhecido'" for name in column_names]

            column_definitions_str = ', '.join(column_definitions)

            create_table = f"""CREATE TABLE {tablename} (
                                                id INT AUTO_INCREMENT PRIMARY KEY,
                                                {column_definitions_str}
                                                ) """
            cursor.execute(create_table)
            print(f"Tabela {tablename} criada com sucesso ")

            cursor.execute("ALTER TABLE covidbigtable ADD Comorbidade VARCHAR(50) NOT NULL DEFAULT 'Desconhecido'")
            connection.commit()

            for _, row in dataframe_covid[column_names].iterrows():
                values = [row[name] for name in column_names]
                query = f"INSERT INTO {tablename} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
                cursor.execute(query, values)

            connection.commit()
            print('Dados inseridos na tabela covidbigtable')
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)


def insertComorbidadeInBigTable(connection):
    if connection:
        try:
            indexTable = 0
            cursor = connection.cursor()
            for index, row in dataframe_covid.loc[:, 'ComorbidadePulmao':'ComorbidadeObesidade'].iterrows():
                indexTable = indexTable + 1

                if 'Sim' in row.values:
                    query = f"UPDATE covidbigtable SET Comorbidade = 'Sim' WHERE id={indexTable}"
                    cursor.execute(query)
                else:
                    query = f"UPDATE covidbigtable SET Comorbidade = 'Não' WHERE id={indexTable}"
                    cursor.execute(query)
                if indexTable % 1000 == 0:
                    connection.commit()
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)