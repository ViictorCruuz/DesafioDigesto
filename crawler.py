import csv

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



def vultr_web_page():
    req_vultr = Request('https://www.vultr.com/products/cloud-compute/#vc2', headers={'User-Agent': 'Chrome/18.0.1025.133'})
    
    vultr_page = urlopen(req_vultr).read()

    soup = BeautifulSoup(vultr_page, 'html.parser')

    return soup.select('strong')


def digitalocean_web_page():
    req_digital = Request('https://www.digitalocean.com/pricing/', headers={'User-Agent': 'Chrome/18.0.1025.133'})

    ocean_page = urlopen(req_digital).read()

    soup = BeautifulSoup(ocean_page, 'html.parser')

    return soup.select('strong')


vultr = vultr_web_page()

ocean = digitalocean_web_page()

with open('crawler.txt', 'w') as file:
    for vr in vultr[:-7]:
        file.write(vr.text + '\n')

    for dt in ocean:
        file.write(dt.text + '\n')

print("Você pode escolher as seguintes opções: \n1) Imprime resultado na tela \n2) Salvar dados em arquivo csv\n3) Salvar em arquivo json\n")

choose = int(input())

if choose == 1:
    with open('crawler.txt', 'r') as r:
        print(r.read())
