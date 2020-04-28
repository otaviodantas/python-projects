# Nesta aula vamos fazer uma função que recebe a URL e desmembra ela

class ExtratorArgumentosUrl():
    def __init__(self, url):
        if (self.ValidaURL(url)):
            self.url = url.lower() 
        
        else:
            raise LookupError('URL inválida!')
    
    @staticmethod
    def ValidaURL(url):
        if (url):
            return True
        
        else:
            return False

    def ExtractIndex(self):
        fixCent_O = 'moedaorigem='
        fixCent_D = 'moedadestino='

        Index_CentOrigin_I = self.AuxIndex(fixCent_O)
        Index_CentOrigin_E = self.url.find('&') 

        Index_CentDestiny_I = self.AuxIndex(fixCent_D)
        Index_CentDestiny_E = self.url.find('&', 60)

        centOring   = self.url[Index_CentOrigin_I:Index_CentOrigin_E]
        centDestiny = self.url[Index_CentDestiny_I:Index_CentDestiny_E]

        return centDestiny, centOring

    def AuxIndex(self, cent):
        return self.url.find(cent) + len(cent)

    def ExtractValor(self):
        valor = 'valor='
        IndexValor = self.AuxIndex(valor)
        only_valor = self.url[IndexValor:]
        return only_valor
