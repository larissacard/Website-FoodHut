jtrabalho = int(input("Informe quantidade de horas trabalhadas no mês."))
salarioh = int(5) #5 reais por hora
salariot = 0 #Salario total sem horas extras
salariote = 0 #Salario total com horas extras
acres = 5 * 50 / 100 #Acrescimo de hora extras
horaex = jtrabalho - 160 #Quantidade de horas extras

if (jtrabalho > 160):
    salariote = jtrabalho * 5 + acres * horaex
    print('Salario total com hora extra: ',salariote)
    
else:
    salariot = jtrabalho * salarioh
    print("Salario total: ", salariot)
    