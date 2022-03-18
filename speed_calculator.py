
dexterity = int(input('Enter your Dexterity trait: '))
celerity = int(input('Enter your Celerity trait: '))
run = 20 + (3*dexterity)
jog = 12 + dexterity
if (celerity > 0):
    usage = input('Are you spending 1 blood point to activate Celerity?  Y/N ')
    if (usage.lower() == 'y'):
        run = run * (celerity + 1)
        jog = jog * (celerity + 1)
    else:
        run += (celerity*3)
        jog += celerity
print('Walking speed: 7mts \Jogging speed: ', jog, 'mts\nRunning speed: ', run, 'mts', sep="")
print('Maximum speed: ', round((run*20*60)/1000, 2), 'kmh', sep="")
input()