distâcia = float(input("informe a distância (em km):"))
consumo_do_carro = float(input("informe o consumo do carro: "))
combustivel = float(input("preço do combustivel(RS)"))

litro = distâcia / consumo_do_carro
custo_total = litro * combustivel

print(f"custo total: {custo_total}")