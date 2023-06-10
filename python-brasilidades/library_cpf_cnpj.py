from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_docuemnto(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError ("Cpf Inválido")

    def __str__(self):
        return self.format()

    def valida(self, documeno):
        validador = CPF()
        return validador.validate(documeno)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError ("Cnpj Inválido")

    def __str__(self):
        return self.format()

    def valida (self,documento):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
