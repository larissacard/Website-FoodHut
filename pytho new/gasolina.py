preco = 0
litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")

#Se a escolha for alcool seguir com as determinadas condições para o desconto:
if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100 #Desconto sobre o litro
    else:
        preco -= 1.9 * litros * 5 / 100 #Desconto sobre o litro
        
#Se a escolha for gasolina seguir com as determinadas condições para o desconto:        
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100 #Desconto sobre o litro
    else:
        preco -= 2.5 * litros * 6 / 100 #Desconto sobre o litro
        
print(f"O preço a pagar é R${preco:.2f}")