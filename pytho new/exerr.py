from cmath import inf
from datetime import datetime

dateeve = ('%d-%m-%Y')

data = input("Informe a data de acesso: ")
data = datetime.strptime(data,dateeve)

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if(datetime.strptime("21-3-2022", dateeve) <= data):
    print("Cadastro não concluido.")
elif(idade < 18):
    print("Cadastro não concluido.")
