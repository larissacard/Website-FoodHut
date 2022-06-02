idadesH = []
idadesM = []
contH = 0
contM = 0

print("==== Homens ====")
while (contH < 2):
   idadeH = int(input("Informe sua idade: "))
   idadesH.append(idadeH)
   contH = contH + 1
   
print("==== Mulheres ====")
while (contM < 2):
   idadeM = int(input("Informe sua idade: "))
   idadesM.append(idadeM)
   contM = contM + 1
 
minH = min(int(number) for number in idadesH)
maxH= max(int(number) for number in idadesH)
minM = min(int(number) for number in idadesM)
maxM= max(int(number) for number in idadesM)
 
print('Homem mais velho + Mulher mais nova: ', maxH + minM)
print('Mulher mais velha + homem mais novo: ', maxM + minH)