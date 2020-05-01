from validate_docbr import CPF, CNPJ

class factoryDoc:
    @staticmethod
    def factory(n_doc):
        n_doc = str(n_doc)

        if (len(n_doc) == 11):
            return doc_CPF(n_doc)

        elif(len(n_doc) == 14):
            return doc_CNPJ(n_doc)
        
        else:
            raise ValueError('>> Quantidade de números inválida <<')

class doc_CPF():
    
    def __init__(self, n_doc):
        if self.valid(n_doc):
            self.n_cpf = n_doc

        else:
            raise ValueError('>> CPF Inválido <<')

    def __str__(self):
        return self.sep_cpf()

    def valid(self, n_doc):
        model = CPF()
        return model.validate(n_doc)

    def sep_cpf(self):
        model = CPF()
        return model.mask(self.n_cpf)

class doc_CNPJ():

    def __init__(self, n_doc):

        if self.valid(n_doc):
            self.n_cnpj = n_doc

        else:
            raise ValueError('>> CNPJ Inválido <<')

    def __str__(self):
        return self.sep_cnpj()

    def valid(self, n_doc):
        model = CNPJ()
        return model.validate(n_doc)

    def sep_cnpj(self):
        model = CNPJ()
        return model.mask(self.n_cnpj)

