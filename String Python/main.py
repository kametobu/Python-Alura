url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

indice_interrogacao =url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)
print(url_parametros.split("&"))
url_parametros = url_parametros.split("&")

parametro_busca = "quantidade"
indecedo_parametro = url_parametros[2].find(parametro_busca)
indece_valor = indecedo_parametro+len(parametro_busca)+1
valor = url_parametros[2][indece_valor:]
print(valor)
