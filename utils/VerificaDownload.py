from logging import info, exception
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import JavascriptException

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class VerificaDownload:
    """
    Verifica se o download já finalizou e pega o nome do arquivo que foi baixado.
    """

    def __init__(self, driver: webdriver.Chrome):

        self.__driver = driver
        self.__handle = self.__driver.current_window_handle
        self.__nome_arquivo = None

        self.__get_percent = '''
            return document.querySelector('downloads-manager')
                .shadowRoot.querySelector('#downloadsList downloads-item')
                .shadowRoot.querySelector('#progress').value
        '''

        self.__get_file_name = '''
            return document.querySelector('downloads-manager')
                .shadowRoot.querySelector('#downloadsList downloads-item')
                .shadowRoot.querySelector('div#content #file-link').text
        '''

        self.__remove_btn = '''
            return document.querySelector('downloads-manager')
                .shadowRoot.querySelector('#downloadsList downloads-item')
                .shadowRoot.querySelector('div#content #remove')
                .style.visibility
        '''

        self.__remove_download = '''
            document.querySelector('downloads-manager')
                .shadowRoot.querySelector('#downloadsList downloads-item')
                .shadowRoot.querySelector('div#content #remove')
                .click()
        '''

    def arquivo_nome(self, ele: WebElement, tempo_espera: int = 60, tempo_espera_dl_ini: int = 30,
                     tentativas: int = 3):

        try:
            self.__processa_download_nome(ele, tempo_espera, tempo_espera_dl_ini, tentativas)

        except:
            raise Exception(f'Depois de {tentativas}, não foi possível baixar o arquivo')

        finally:
            return self.__nome_arquivo

    def __processa_download_nome(self, ele, tempo_espera, tempo_espera_dl_ini, tentativas):

        for i in range(0, tentativas):
            try:
                sleep(2)

                ele.click()

                self.__abre_nova_aba()
                self.__verifica_porcentagem(tempo_espera, tempo_espera_dl_ini)
                self.__pega_nome_arquivo()
                self.__limpa_historico()

                info(f'Download do arquivo {self.__nome_arquivo} concluído com sucesso!')

                return

            except Exception:
                exception('PROBELMA NA HORA DE VERIFICAR O DOWNLOAD')

            finally:
                for handle in self.__driver.window_handles:
                    if handle != self.__handle:
                        self.__driver.switch_to.window(handle)
                        self.__driver.close()

                self.__driver.switch_to.window(self.__handle)

    def __abre_nova_aba(self):

        try:
            self.__driver.execute_script("window.open()")

            # # Muda para nova aba
            self.__driver.switch_to.window(self.__driver.window_handles[1])

            # Navega até a janela de transferência
            self.__driver.get('chrome://downloads')

        except:
            raise Exception('Não foi possível abrir uma nova aba')

    def __verifica_porcentagem(self, tempo_espera: int, tempo_espera_dl_ini: int):

        for i in range(0, tempo_espera_dl_ini):
            try:
                for x in range(0, tempo_espera):
                    sleep(1)

                    # Captura a porcentagem do download
                    porcentagem = self.__driver.execute_script(self.__get_percent)

                    info(f'Porcentagem de download: {porcentagem} ...')

                    # Verifica se o donload chegou a 100%
                    if porcentagem == 100:
                        return
                    else:
                        continue

                raise Exception('Tempo de espera de download excedido')

            except JavascriptException as inst:

                if "Cannot read property 'value' of null" in inst.msg:
                    # info('Download não parece ter começado ou já terminou antes de ser analisado ...')

                    if self.__verifica_conclusao_download():
                        return

                    sleep(1)

                elif i < tempo_espera_dl_ini - 1:
                    info('Esperando download iniciar ...')
                    sleep(1)

                    continue

                else:
                    exception('Download não pode ser iniciado')

            except:

                raise Exception('Porcentagem do download não pôde ser verificada')

    def __pega_nome_arquivo(self):

        try:
            self.__nome_arquivo = self.__driver.execute_script(self.__get_file_name)

        except:
            raise Exception('Nome do arquivo não pode ser capturado')

    def __verifica_conclusao_download(self):

        try:
            self.__pega_nome_arquivo()

            return True

        except:
            info('Arquivo não começou a ser baixado')

            return False

    def __limpa_historico(self):
        try:
            WebDriverWait(self.__driver, 15).until(
                lambda driver: self.__driver.execute_script(self.__remove_btn) == '')

            self.__driver.execute_script(self.__remove_download)

        except:
            raise Exception('NÃO FOI POSSÍVEL CLICAR NO BOTÃO DE REMOVER O DOWNLOAD')



