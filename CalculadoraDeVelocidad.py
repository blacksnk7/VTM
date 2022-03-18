
dexterity = int(input('Ingrese su puntuacion de Destreza: '))
celerity = int(input('Ingrese su puntuacion de Celeridad: '))
run = 20 + (3*dexterity)
jog = 12 + dexterity
if (celerity > 0):
    usage = input('Esta gastando sangre para activar Celeridad?  Y/N ')
    if (usage.lower() == 'y'):
        run = run * (celerity + 1)
        jog = jog * (celerity + 1)
    else:
        run += (celerity*3)
        jog += celerity
print('Velocidad caminando: 7mts \nVelocidad trotando: ', jog, 'mts\nVelocidad corriendo: ', run, 'mts', sep="")
print('Velocidad maxima: ', round((run*20*60)/1000, 2), 'kmh', sep="")
input()