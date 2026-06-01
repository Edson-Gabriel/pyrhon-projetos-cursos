# Crie um código em Python que teste se o site informado 
# está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://edson-gabriel.github.io/enxovalCasaNova/")
    print(f"Site no ar")
except urllib.error.URLError:
    print("O site não esta acessivel no momento!")