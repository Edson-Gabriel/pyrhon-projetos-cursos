# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Vasco da Gama.

times = (
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 
    'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Red Bull Bragantino', 
    'Atlético Mineiro', 'Santos', 'Corinthians', 'Vasco da Gama', 'Vitória', 
    'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport Recife'
)
print(f"Segue a tabela dos times: {times}")
print(f"Os 5 primeiros colocados, foram os times: {times[0:5]}")
print(f"Os 4 últimos colocados, foram os times: {times[-4:]}")
print(f"Os times em ordem alfabética: {sorted(times)}")
print(f"o Vasco da Gama se encontra na posição: {times.index("Vasco da Gama")+1}º")