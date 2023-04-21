from utils.VerificaDownload import *
from selenium.webdriver.common.by import By

"""
    A janela de download do Chrome que será aberta pela classe VerificaDownload
    DEVE ficar aberta, não podemos mudar de aba enquanto o download está sendo feito, uma vez que a verificação é feita nessa página
"""


def executeWebScrapping():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    elemento = VerificaDownload(driver)

    driver.get('https://coronavirus.es.gov.br/painel-covid-19-es')

    ele = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/article/div/div/div/div/div/div['

                                        '1]/p/a[1]')
    elemento.arquivo_nome(ele, tempo_espera=3000)
    driver.quit()
