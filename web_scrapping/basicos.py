from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import pandas

url = 'https://www.python.org/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

try:
    req = Request(url)
    response = urlopen(req)
    html = response.read()
    html = html.decode('utf-8')  # Decodificando


    def tratando_html(arg):
        return ' '.join(html.split()).replace('> <', '><')


    html = tratando_html(html)

    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    # Acessando as tags
    titulo = soup.html.head.title.get_text()
    # print(titulo)

    # Acessando os atributos com metodo find
    img1 = soup.findAll('img')
    # print(img1)

    # Pesquisando com lista de Tags
    textos = soup.findAll(['h1', 'h2', 'h3'])
    # print(textos)

    # Pesquisando pelos atributos
    paragrafos = soup.findAll('p')
    # print(paragrafos)

    paragrafos2 = soup.findAll('p', {'class': 'txt-value'})
    paragrafos3 = soup.findAll('span', {'class': 'message'})
    #print(paragrafos3)

    # Pesquisando pelo conteudo de uma tag
    palavras = soup.findAll('p', text='versions')
    print(palavras)


except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
