import PySimpleGUI as sg
import pandas as pd

sg.ChangeLookAndFeel("DarkGrey10")

menu_def = [['File', ['Open', 'Close']]]

excel_file = 'Treenikirja.xlsx'
df = pd.read_excel(excel_file)

# ------ Column Definition ------ #

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('TREENIKIRJA', size=(50, 1), justification='center', font=("Helvetica", 25))],  # Otsikko
    [sg.Text('Päivän treeni oli:', size=(14,1)), sg.Input(size=(110), key='Treeni')], # Treenin nimeäminen
    [sg.Frame(layout=[], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Text('Treenin kuvaus:', size=(14)), sg.Multiline(size=(35, 3), key='Kuvaus'), # Kuvaus palkki
        sg.Input(key='PVM', size=(20,3)),
        sg.CalendarButton('PVM', close_when_date_chosen=True, target='PVM'),
        sg.Text('Kesto:', size=(5)), sg.Slider(range=(0, 120), tick_interval=(15), orientation='h', size=(25, 20), key='Kesto')],
    [sg.Text('Liikkeiden määrä:', size=(12)), sg.InputCombo((1, 2, 3, 4, 5), key='-KPL-', size=(5, 1)),
    sg.Button('Lisää tiedot')],

    [sg.Text('_'  * 120)],
    [sg.Text('Liike', justification='center', size=(19,1), visible=True),
        sg.Text('Sarjat', justification='center', size=(19,1), visible=True),
        sg.Text('Toistot', justification='center', size=(19,1), visible=True),
        sg.Text('Paino', justification='center', size=(19,1), visible=True)],

#SARJAT/TOISTOT/PAINOT OSIO
   [sg.Input(size=(20,3),key=1, visible=False), 
    sg.Slider(range=(0, 10), orientation='h', tick_interval=(5), key=2, visible=False),   #1
    sg.Slider(range=(0, 20), orientation='h', tick_interval=(5), key=3, visible=False), 
    sg.Slider(range=(0, 200), orientation='h', size=(40, 20), tick_interval=(25), key=4, visible=False)],

    [sg.Input(size=(20,3), key=5, visible=False), 
    sg.Slider(range=(0, 10), orientation='h', tick_interval=(5), key=6, visible=False),  #2
    sg.Slider(range=(0, 20), orientation='h', tick_interval=(5), key=7, visible=False), 
    sg.Slider(range=(0, 200), orientation='h', size=(40, 20), tick_interval=(25), key=8, visible=False)],

    [sg.Input(size=(20,3), key=9, visible=False), 
    sg.Slider(range=(0, 10), orientation='h', tick_interval=(5), key=10, visible=False),  #3
    sg.Slider(range=(0, 20), orientation='h', tick_interval=(5), key=11, visible=False), 
    sg.Slider(range=(0, 200), orientation='h', size=(40, 20), tick_interval=(25), key=12, visible=False)],

    [sg.Input(size=(20,3), key=13, visible=False), 
    sg.Slider(range=(0, 10), orientation='h', tick_interval=(5), key=14, visible=False),  #4
    sg.Slider(range=(0, 20), orientation='h', tick_interval=(5), key=15, visible=False), 
    sg.Slider(range=(0, 200), orientation='h', size=(40, 20), tick_interval=(25), key=16, visible=False)],
    
    [sg.Input(size=(20,3), key=17, visible=False), 
    sg.Slider(range=(0, 10), orientation='h', tick_interval=(5), key=18, visible=False),  #5
    sg.Slider(range=(0, 20), orientation='h', tick_interval=(5), key=19, visible=False), 
    sg.Slider(range=(0, 200), orientation='h', size=(40, 20), tick_interval=(25), key=20, visible=False)],




    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit('Tallenna', tooltip='Click to submit this window'), sg.Cancel('Poistu'), sg.Button('Tyhjää')]
]

def tyhjenna():
    for key in values:
        window[key]("")
    for key in range(21):
        window[key].update(visible = False)
    return None

def lisaa_tiedot(KPL):
    if KPL == 1:
        kpl = 0
        while kpl <= 4:
            window[kpl].update(visible=True)
            kpl += 1
    if KPL == 2:
        kpl = 0
        while kpl <= 8:
            window[kpl].update(visible=True)
            kpl += 1
    if KPL == 3:
        kpl = 0
        while kpl <= 12:
            window[kpl].update(visible=True)
            kpl += 1
    if KPL == 4:
        kpl = 0
        while kpl <= 16:
            window[kpl].update(visible=True)
            kpl += 1
    if KPL == 5:
        kpl = 0
        while kpl <= 20:
            window[kpl].update(visible=True)
            kpl += 1


window = sg.Window('Treenikirja', layout, resizable= True, default_element_size=(100, 1), grab_anywhere=True, )


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit') or event == 'Poistu':
        break
    elif event == 'Tallenna':
        print(event, values)
        df = df.append(values, ignore_index = True)
        df.to_excel(excel_file, index = False)
        sg.popup('Tallennettu')
        tyhjenna()
    elif event == 'Tyhjää':
        tyhjenna()
    elif event == 'Lisää tiedot':  
        KPL = values['-KPL-']
        lisaa_tiedot(KPL)
        #if kpl == 1:
            #window[1].update(visible=True), window[11].update(visible=True), window[12].update(visible=True), window[13].update(visible=True)
            #window[2].update(visible=False), window[21].update(visible=False), window[22].update(visible=False), window[23].update(visible=False)
            #window[3].update(visible=False), window[31].update(visible=False), window[32].update(visible=False), window[33].update(visible=False)
            #window[4].update(visible=False), window[41].update(visible=False), window[42].update(visible=False), window[43].update(visible=False)
            #window[5].update(visible=False), window[51].update(visible=False), window[52].update(visible=False), window[53].update(visible=False)
        #if kpl == 2:
            #window[1].update(visible=True), window[11].update(visible=True), window[12].update(visible=True), window[13].update(visible=True)
           # window[2].update(visible=True), window[21].update(visible=True), window[22].update(visible=True), window[23].update(visible=True)
            #window[3].update(visible=False), window[31].update(visible=False), window[32].update(visible=False), window[33].update(visible=False)
           # window[4].update(visible=False), window[41].update(visible=False), window[42].update(visible=False), window[43].update(visible=False)
          #  window[5].update(visible=False), window[51].update(visible=False), window[52].update(visible=False), window[53].update(visible=False)
        #if kpl == 3:
           # window[1].update(visible=True), window[11].update(visible=True), window[12].update(visible=True), window[13].update(visible=True)
          #  window[2].update(visible=True), window[21].update(visible=True), window[22].update(visible=True), window[23].update(visible=True)
          #  window[3].update(visible=True), window[31].update(visible=True), window[32].update(visible=True), window[33].update(visible=True)
          #  window[4].update(visible=False), window[41].update(visible=False), window[42].update(visible=False), window[43].update(visible=False)
          #  window[5].update(visible=False), window[51].update(visible=False), window[52].update(visible=False), window[53].update(visible=False)
       # if kpl == 4:
        #    window[1].update(visible=True), window[11].update(visible=True), window[12].update(visible=True), window[13].update(visible=True)
          #  window[2].update(visible=True), window[21].update(visible=True), window[22].update(visible=True), window[23].update(visible=True)
           # window[3].update(visible=True), window[31].update(visible=True), window[32].update(visible=True), window[33].update(visible=True)
          #  window[4].update(visible=True), window[41].update(visible=True), window[42].update(visible=True), window[43].update(visible=True)
          #  window[5].update(visible=False), window[51].update(visible=False), window[52].update(visible=False), window[53].update(visible=False)
       # if kpl == 5:
          #  window[1].update(visible=True), window[11].update(visible=True), window[12].update(visible=True), window[13].update(visible=True)
           # window[2].update(visible=True), window[21].update(visible=True), window[22].update(visible=True), window[23].update(visible=True)
          #  window[3].update(visible=True), window[31].update(visible=True), window[32].update(visible=True), window[33].update(visible=True)
          #  window[4].update(visible=True), window[41].update(visible=True), window[42].update(visible=True), window[43].update(visible=True)
          #  window[5].update(visible=True), window[51].update(visible=True), window[52].update(visible=True), window[53].update(visible=True)
window.close()