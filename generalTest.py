from Extrator import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700" 

react = ExtratorArgumentosUrl(url)

centO, centD = react.ExtractIndex()
valor = react.ExtractValor()
print(centO, centD, valor) 