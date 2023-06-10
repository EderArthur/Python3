from library_cpf_cnpj import Documento
from validate_docbr import CNPJ
cpf_um = ("15316264754")
#print(cpf_um)
exemplo_cnpj = "68428422000104"
#exemplo_cpf = "16260053622"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_docuemnto (cpf_um)
print(documento)