import requests
from library_cep import BuscaEndereco
cep = "01001000"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/32050400/json/")
#print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
