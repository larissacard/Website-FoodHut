E,F,C = input().split(' ')
E = int(E)
F =  int(F)
C = int(C)

gv = E + F
bebidos = 0

while gv >= C:
    gvazio = gvazio - C
    bebidos = bebidos + 1
    gv = gv + 1
print(bebidos)