#Verifica se o site Google.com está acessivel

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/')

except urllib.error.URLError:
    print('Site não acessivel!')
else:
    print('Tudo certo!')