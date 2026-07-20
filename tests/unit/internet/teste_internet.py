from app.search.providers.internet import InternetProvider

provider = InternetProvider()

resultado = provider.search("Quem é o presidente do Brasil?")

print(resultado.content)