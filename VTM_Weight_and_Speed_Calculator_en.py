import PySimpleGUI as sg

def calculate_speed(dex, cel):
    runP = 20 + (3 * (dex + cel))       #mts per round while running normally
    jogP = 12 + (dex + cel)             #mts per round while jogging normally
    runA = (20 + (3 * dex)) * (1 + cel) #mts per round while running with Celerity activated
    jogA = (12 + dex) * (1 + cel)       #mts per round while jogging with Celerity activated
    maxP = round((runP*20*60)/1000, 2)  #kms per hour while running normally 
    maxA = round((runA*20*60)/1000, 2)  #kms per hour while running with Celerity activated
    dic = {"jogging:": [jogP, jogA], "running:": [runP, runA], "max:": [maxP, maxA]}
    return dic

def calculate_weight(strength, potence):
    total = strength + potence
    match total:
        case 0:
            weight = 0
        case 1:
            weight = 20
        case 2:
            weight = 45
        case 3:
            weight = 115
        case 4:
            weight = 180
        case 5:
            weight = 295
        case _:
            weight = 295
            while (total > 5):
                weight += total * 10
                total -= 1
    total = strength
    match strength:
        case 0:
            weight_mul = 0
        case 1:
            weight_mul = 20
        case 2:
            weight_mul = 45
        case 3:
            weight_mul = 115
        case 4:
            weight_mul = 180
        case 5:
            weight_mul = 295
        case _:
            weight_mul = 295
            while (total > 5):
                weight_mul += total * 10
                total -= 1
    weight_mul = (weight_mul + weight) * (potence+1)
    return [weight, weight_mul]

# Define the window's contents
layout = [[sg.Text("Celerity:   "), sg.Input(default_text="0", size=(3, 1), key='-1-')],
          [sg.Text("Dexterity: "), sg.Input(default_text="0", size=(3, 1), key='-2-')],
          [sg.Text(size=(40,6), key='-OUTPUT1-')],
          [sg.Text("Strength: "), sg.Input(default_text="0", size=(3, 1), key='-3-')],
          [sg.Text("Potence: "), sg.Input(default_text="0", size=(3, 1), key='-4-')],
          [sg.Text(size=(40,2), key='-OUTPUT2-')],
          [sg.Button('Calculate'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Vampire the Masquerade Speed and Wheight Calculator', layout)
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    dic = calculate_speed(int(values['-1-']), int(values['-2-']))
    speeds = list(dic.values())
    try:
        window['-OUTPUT1-'].update(f"Passive jogging speed: {speeds[0][0]}mts\nCelerity active jogging speed: {speeds[0][1]}mts\nPassive running speed: {speeds[1][0]}mts\nCelerity active running speed: {speeds[1][1]}mts\nMaximum running speed: {speeds[2][0]}kmh\nCelerity active maximum running speed: {speeds[2][1]}mts")
    except:
        print("error1")
    weights = calculate_weight(int(values['-3-']), int(values['-4-']))
    try:
        window['-OUTPUT2-'].update(f"Maximum weight lifted normally: {weights[0]}kg\nMaximum weight lifted with Potence activated: {weights[1]}kg")
    except:
        print("error2")

# Finish up by removing from the screen
window.close()