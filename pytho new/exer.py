from datetime import datetime, date

print(datetime.today().strftime('%d-%m-%Y'))

#data = date.today()

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
data_= input("")
if(idade < 18):
    print("Cadastro não pode ser concluido.")
elif(date.today > datetime.date(24/3/2022)):
    print("Cadastro não pode ser concluido.")
#elif()
    
    #print("Cadastro concluido.")