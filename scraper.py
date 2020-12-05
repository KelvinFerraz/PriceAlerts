import requests
from bs4 import BeautifulSoup


def AdegaPrice():
    URL_ADEGA = 'https://loja.electrolux.com.br/adega-24-garrafas-uma-porta-preta-com-acabamento-em-inox-acs24-electrolux/p'

    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    page = requests.get(URL_ADEGA, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find('div', {'class':'productName'}).get_text()
    productPrice = soup.find('strong', {'class':'skuBestPrice'}).get_text()
    converted_price = productPrice[2:12]

    print(productName.strip())
    print()
    print(converted_price)

def FreezerPrice():
    URL_FREEZER = 'https://loja.electrolux.com.br/geladeira-refrigerador-french-door-electrolux-579l-inox-dm84x/p?_ga=2.127683339.72854460.1607046740-1619423647.1607046740&_gac=1.120567930.1607046740.Cj0KCQiAtqL-BRC0ARIsAF4K3WE7fy-yUcg1QGoh19-u5kzdPZ5f3rgVzuLUnuynBpv7LAVPC3NHAaIaAuGZEALw_wcB'
    
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    page = requests.get(URL_FREEZER, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find('div', {'class':'productName'}).get_text()
    productPrice = soup.find('strong', {'class':'skuBestPrice'}).get_text()
    converted_price = productPrice[2:12]

    print(productName.strip())
    print()
    print(converted_price)

def FornoPrice():
    URL_FORNO = 'https://loja.electrolux.com.br/forno-de-embutir-a-gas-og8dx-electrolux/p'
    
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    page = requests.get(URL_FORNO, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find('div', {'class':'productName'}).get_text()
    productPrice = soup.find('strong', {'class':'skuBestPrice'}).get_text()
    converted_price = productPrice[2:12]

    print(productName.strip())
    print()
    print(converted_price)

def LavaLoucaPrice():
    URL_LAVALOUCA = 'https://loja.electrolux.com.br/lava-louca-inox-10-servicos-lv10x/p?_ga=2.30730297.72854460.1607046740-1619423647.1607046740&_gac=1.224836968.1607046740.Cj0KCQiAtqL-BRC0ARIsAF4K3WE7fy-yUcg1QGoh19-u5kzdPZ5f3rgVzuLUnuynBpv7LAVPC3NHAaIaAuGZEALw_wcB'
    
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    page = requests.get(URL_LAVALOUCA, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find('div', {'class':'productName'}).get_text()
    productPrice = soup.find('strong', {'class':'skuBestPrice'}).get_text()
    converted_price = productPrice[2:12]

    print(productName.strip())
    print()
    print(converted_price)

def MicroOndasPrice():
    URL_MICRO = 'https://loja.electrolux.com.br/micro-ondas-tira-odor-electrolux-mt30s/p?_ga=2.206981339.958821350.1606488870-1134548800.1600211757'
    
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    page = requests.get(URL_MICRO, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find('div', {'class':'productName'}).get_text()
    productPrice = soup.find('strong', {'class':'skuBestPrice'}).get_text()
    converted_price = productPrice[2:12]

    print(productName.strip())
    print()
    print(converted_price)

def DepuradorPrice():
    URL_DEPURADOR = 'https://www.shoptime.com.br/produto/1316783013/depurador-de-parede-retratil-tramontina-slide-60-em-aco-inox-60-cm?WT.srch=1&aid=5fc3aefa20d8e0000f33ab8c&chave=vnzpla_5fc3aefa20d8e0000f33ab8c_10368118000201_1316783013&epar=bp_pl_ou_go_b2wads&gclid=Cj0KCQiAtqL-BRC0ARIsAF4K3WFRk_HJngaWHRIUHgEtLToEvcwsiFc7yHVta616fcBHfmoCy3dvDSEaAj_XEALw_wcB&opn=GOOGLEXML&pid=1316783013&sellerid=10368118000201&sid=10368118000201&voltagem=127%20V'

def NotebookPrice():
    URL_NOTEBOOK = 'https://avell.com.br/avell-a60-muv-295765'

    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    page = requests.get(URL_NOTEBOOK, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find('h1', {'class':'prod-title'}).get_text()
    productPrice = soup.find('span', {'class':'boleto-price'}).get_text()
    converted_price = productPrice[2:12]

    print(productName.strip())
    print()
    print(converted_price)

print('........................................................')
print('       PRODUCTS ELETROLUX - www.eletrolux.com.br        ')
print('........................................................')
AdegaPrice()
print('........................................................')
FreezerPrice()
print('........................................................')
FornoPrice()
print('........................................................')
MicroOndasPrice()
print('........................................................')
LavaLoucaPrice()
print()
print('........................................................')
print('                   NOTEBOOK AVELL                       ')
print('........................................................')
NotebookPrice()
print('........................................................')