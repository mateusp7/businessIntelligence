from connection_data_base.connection_data_base import conectar
from df.covid_df import covid_df
from mysql.connector import Error
from utils.createTable import createtableComorbidade

connection = conectar()
dataframe_covid = covid_df()


def createBigWithMultiplesCollumns(tablename, column_names):
    cursor = connection.cursor()
    if connection:
        try:
            print('Passou')
            # cursor.execute(f"SHOW TABLES LIKE '{tablename}'")
            # result = cursor.fetchone()
            # if result:
            #     drop_table = f"""DROP TABLE {tablename};"""
            #     cursor.execute(drop_table)
            #     connection.commit()
            #     print(f'Tabela {tablename} dropada com sucesso!')

            # column_definitions = [f"{name} VARCHAR(255) NOT NULL DEFAULT 'Desconhecido'" for name in column_names]
            #
            # column_definitions_str = ', '.join(column_definitions)
            #
            # create_table = f"""CREATE TABLE {tablename} (
            #                                     id INT AUTO_INCREMENT PRIMARY KEY,
            #                                     {column_definitions_str}
            #                                     ) """
            # cursor.execute(create_table)
            # print(f"Tabela {tablename} criada com sucesso ")

            # for _, row in dataframe_covid[column_names].iterrows():
            #     values = [row[name] for name in column_names]
            #     query = f"INSERT INTO {tablename} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
            #     cursor.execute(query, values)

            # for index, row in dataframe_covid.loc[:, 'ComorbidadePulmao':'ComorbidadeObesidade'].iterrows():
            #     if 'Sim' in row.values:
            #         query = f"""UPDATE covidbigtable SET Comorbidade == 'Sim' WHERE id={row}"""
            #         cursor.execute(query)
            #     else:
            #         query = f"""UPDATE covidbigtable SET Comorbidade == 'Nao' WHERE id={row}"""
            #         cursor.execute(query)
            # connection.commit()

        except Error as e:
            print("Error while connecting to MySQL", e)