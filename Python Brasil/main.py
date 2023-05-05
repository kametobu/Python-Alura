from DOC import Documento
#from validate_docbr import CPF,CNPJ
usuario_cpf = Documento.cria_documento("42141154065")
print(usuario_cpf)

usuario_cnpj = Documento.cria_documento('35379838000112')
print(usuario_cnpj)

usuario_tel = Documento.cria_documento('5511982533866')
print(usuario_tel)

