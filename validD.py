import re

class TelefoneBR:
    standard = "(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"

    def __init__ (self, n_tel):
        if (self.valid_tel(n_tel)):
            self.validate_tel = n_tel
        
        else:
            raise ValueError('>> Número de Telefone Inválido <<')

    def __str__(self):
         return self.show_tel()

    def valid_tel(self,n_tel):
        resp = re.findall(self.standard, n_tel)
        return resp

    def show_tel(self):
        rematch = re.search(self.standard, self.validate_tel)
        test_dd = rematch.group(1)
        if (test_dd == None):
            test_dd = '055'
        
        string = '+{}({}) {}-{}'.format(test_dd,rematch.group(2),rematch.group(3),rematch.group(4))
        return string