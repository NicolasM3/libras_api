from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup



class scraping:

    def __init__(self):
        """Inicia o browser e carrega a página"""

        self.browser = Chrome(ChromeDriverManager().install())
        self.url = "http://www.acessibilidadebrasil.org.br/libras_3/"

        self.browser.get(self.url)

    def _listWords(self):
        """
            Retorna a lista de palavras
        """
        objects = self.browser.find_elements_by_xpath("//select[@id='input-palavras']//option")

        words = []
        for obj in objects:
            words.append(obj.text)

        words.pop(0)
        return words

    def _searchWordPage(self, word):
        """
            Recebe uma palavra e procura ela

            argumentos:
                - word = palavra a ser procurada

            retorno:
                - page_source = source da página
                - None = se não achar a palavras
        """
        self.browser.find_element_by_xpath('//table[@class="search box"]//*[@id="search_field"]').click()
        self.browser.find_element_by_xpath('//table[@class="search box"]//*[@id="search_field"]').send_keys(word.upper())
        self.browser.find_element_by_xpath('//table[@class="search box"]//input[@class="btn submit"]').click()

        try:
            self.browser.find_element_by_xpath(f"//select[@id='input-palavras']//option[text()='{word.upper()}']").click()
        except NoSuchElementException:
            self.browser.quit()
            return None

        html = self.browser.page_source
        return BeautifulSoup(html, 'html.parser')

    def getDictionary(self, letter="a"):
        """
            Retorna a lista de palavras com a letra passada
        
            Argumentos: 
                - latter = letra do dicionario
        """

        self.browser.find_element_by_xpath(f"//a[@id='letter-{letter.upper()}']").click()
        sleep(1)
    
        objects = self._listWords()

        words = []
        for obj in objects:
            words.append(obj.text)
        
        return words

    def getGif(self, word):
        """
            Retorna um GIF demonstrando os sinais

            argumentos:
                - word = palavra a ser procurada
            
            retorno:
                GIF = Gif com os sinais
                None = se não achar
        """

        page = self._searchWordPage(word)
        gif = page.source.get('src')

        return "http://www.acessibilidadebrasil.org.br/libras_3/" + gif
        

if __name__ == "__main__":
    scrap = scraping()

    print(scrap.getGif("ostra"))
    
    #self.browser.quit()
