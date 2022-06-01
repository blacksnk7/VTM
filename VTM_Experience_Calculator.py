import PySimpleGUI as sg

def calculate_attributes(old, new):
    total = 0
    times = new - old
    for n in range (times):
        total += 4 * (old + n)
    return total

def calculate_skills(old, new):
    if (old == 0):
        total = 3
    else:
        total = 0
    times = new - old
    for n in range (times):
        total += 2 * (old + n)
    return total

def calculate_disciplines(clan, old, new):
    if (old == 0):
        total = 10
    else:
        total = 0
    if (new > 1):
        times = new - old
        if (clan):
            for n in range (times):
                total += 5 * (old + n)
        else:
            for n in range (times):
                total += 7 * (old + n)
    return total

def calculate_path(old, new):
    if (old == 0):
        total = 7
    else:
        total = 0
    times = new - old
    for n in range (times):
        total += 4 * (old + n)
    return total

layout = [[sg.Text("Original Attribute Level: "), sg.Input(default_text="1", size=(3, 1), key='-ATR_OLD-')],
          [sg.Text("New Attribute Level: "), sg.Input(default_text="1", size=(3, 1), key='-ATR_NEW-')],
          [sg.Text(size=(40,2), key='-OUTPUT1-')],
          [sg.Text("Original Skill/Virtue Level: "), sg.Input(default_text="0", size=(3, 1), key='-SKL_OLD-')],
          [sg.Text("New Skill/Virtue Level: "), sg.Input(default_text="1", size=(3, 1), key='-SKL_NEW-')],
          [sg.Text(size=(40,2), key='-OUTPUT2-')],
          [sg.Text("Original Discipline Level: "), sg.Input(default_text="0", size=(3, 1), key='-DSC_OLD-')],
          [sg.Text("New Discipline Level: "), sg.Input(default_text="1", size=(3, 1), key='-DSC_NEW-')],
          [sg.Checkbox(text="Is the discipline 'in clan'?", size=(18,2), key='-CLAN-')],
          [sg.Text(size=(40,2), key='-OUTPUT3-')],
          [sg.Text(size=(20,2), key='-OUTPUT4-')],
          [sg.Button('Calculate'), sg.Button('Quit')]]

window = sg.Window('Vampire the Masquerade Experience Costs Calculator', layout)
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    try:
        cost_atr = calculate_attributes(int(values['-ATR_OLD-']), int(values['-ATR_NEW-']))
    except ValueError:
        cost_atr = 'enter a number'
    try:
        window['-OUTPUT1-'].update(f"The experience cost to increase an attribute from {values['-ATR_OLD-']} to {values['-ATR_NEW-']} is: {cost_atr}xp")
    except:
        print("error1")
    try:
        cost_skl = calculate_skills(int(values['-SKL_OLD-']), int(values['-SKL_NEW-']))
    except ValueError:
        cost_skl = 'enter a number'
    try:
        window['-OUTPUT2-'].update(f"The experience cost to increase a skill from {values['-SKL_OLD-']} to {values['-SKL_NEW-']} is: {cost_skl}xp")
    except:
        print("error2")
    try:
        cost_dsc = calculate_disciplines(values['-CLAN-'], int(values['-DSC_OLD-']), int(values['-DSC_NEW-']))
    except ValueError:
        cost_dsc = 'enter a number'
    except:
        print('unknown error')
    try:
        window['-OUTPUT3-'].update(f"The experience cost to increase a discipline from {values['-DSC_OLD-']} to {values['-DSC_NEW-']} is: {cost_dsc}xp")
    except:
        print("error3")
    try:
        window['-OUTPUT4-'].update(f"Total experience cost: {cost_atr + cost_skl + cost_dsc}")
    except:
        print("error4")

# Finish up by removing from the screen
window.close()
