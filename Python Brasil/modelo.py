import re

padrao = "[0-9][a-z]{2}[0-9]"

texto = "123 1ca2 1cc aa1 b2b"

email = "alannbatista1@gmail.com.br"

padrao_email = "\w{5,50}@[a-z]{3,10}.com.br"

reporta = re.search(padrao, texto)

print(reporta.group())

reporta = re.search(padrao_email, email)

print(reporta.group())