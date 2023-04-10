import pandas as pd


def covid_df():
    covid_dataframe = pd.read_csv("microdados.csv", sep=";", encoding="latin-1", on_bad_lines='skip',
                                  usecols=['DataObito', 'FaixaEtaria', 'Municipio', 'Bairro', 'Sexo', 'ComorbidadePulmao', 'ComorbidadeCardio', 'ComorbidadeRenal', 'ComorbidadeDiabetes', 'ComorbidadeTabagismo', 'ComorbidadeObesidade'])\
                                .dropna(subset=["DataObito"])
    covid_dataframe['Bairro'].fillna('NAO ENCONTRADO', inplace=True)
    covid_dataframe['Sexo'].fillna('NAO ENCONTRADO', inplace=True)
    covid_dataframe['FaixaEtaria'].fillna('NAO ENCONTRADO', inplace=True)

    return covid_dataframe
