from asyncio.windows_events import NULL

tracajas = []
tracajasVel = []
tracajaNum = int(input("Digite o numero dos tracajas do grupo: "))
while(not 0 < len(tracajas)):
    if(1 <= tracajaNum <= 50):
        for i in range(0,tracajaNum):
            vel = int(input("Digite a velocidade do tracaja {}: ".format(i+1)))
            if(1 <= vel<= 25):
                tracajas.append(i + 1)
                tracajasVel.append(vel)
            else:
                while(not 1 <= vel <= 25):
                    print("Valor de velocidade inválida!!!\nDigite novamente a seguir a velocidade do tracaja {}".format(i + 1))
                    vel = int(input("Digite a velocidade: "))
                tracajas.append(i + 1)
                tracajasVel.append(vel)
    else:
        while(not 0 <= tracajaNum <= 50):
            print("Numero de tracajas não permitidos")
            tracajaNum = int(input("Digite o numero dos tracajas do grupo: "))

resultado = []
for trac,tracVel in zip(tracajas, tracajasVel):
    list = []
    list.append(trac)
    list.append(tracVel)
    resultado.append(list)

maior = []
c = 0
for result in range(len(resultado)):
    if(resultado[result][1] > c):
        if(len(maior) > 0):
            maior.remove(c)
            maior.append(resultado[result][1])
            c = resultado[result][1]

        else:
            maior.append(resultado[result][1])
            c = resultado[result][1]
    else:
        NULL

if(15 <= maior[0]):
    print(3)
elif(10 <= maior[0] < 15):
    print(2)
else:
    print(1)
'''print(tracajas)
print(tracajasVel)
print(resultado)
print(resultado[1][1])
print(maior)
print(c)'''