import requests

class seachEnd():

    def __init__(self, input_cep):
        input_cep = str(input_cep)
        if(self.valid_cep(input_cep)):
            self.true_cep = input_cep
        
        else:
            raise ValueError ('>> CEP inválido <<')

    def __str__(self):
        return self.show_cep()

    def valid_cep(self, input_cep):
        if (len(input_cep) == 8):
            return True

        else:
            return False
        
    def show_cep(self):
        return f'{self.true_cep[:5]}-{self.true_cep[5:]}'
    
    def acess(self):
        url  = f'https://viacep.com.br/ws/{self.true_cep}/json/'
        info = requests.get(url)
        info = info.json()
        return (
            f'Bairro: {info["bairro"]}',
            f'Rua: {info["localidade"]}',
            f'Uf: {info["uf"]} '
        )