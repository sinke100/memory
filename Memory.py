import PySimpleGUI as sg
import sys
import os
from random import shuffle as s
from PIL import Image as im
from io import BytesIO as b
from time import sleep
import threading
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

dog = [resource_path(f'dog{i}.PNG') for i in range(1,10)]
cat = [resource_path(f'cat{i}.PNG') for i in range(1,10)]
polja = cat + dog
polja = [im.open(i) for i in polja]
var1, var2 = 140,126
for i in range(len(polja)): polja[i] = polja[i].resize((var1,var2))
for i in range(len(polja)):
    with b() as output:
        polja[i].save(output, format='PNG')
        polja[i] = output.getvalue()
polja = 2*polja
s(polja)
sg.theme('Topanga')
def wait_match(s, win):
        #sleep(1.5)
        win.write_event_value('match','')
def wait_unmatch(s, win):
        sleep(1.5)
        win.write_event_value('unmatch','')
def window(polja):
    c = 0
    igra_gotova = 0
    greske = 0
    ng = False
    prva, druga = '','!'
    list_key = [str(i+1) for i in range(36)]
    img_box = [sg.Image(polja[i], visible = False, key = f'img{i+1}') for i in range(36)]
    button = [sg.Button(' ', visible = True, size=(16,8), key = f'{i+1}') for i in range(36)]
    column_all = [sg.Column([[i,j]]) for i, j in zip(button, img_box)]
    layout = [column_all[i:i+6] for i in range(0,36,6)]
    layout = layout + [[sg.Button('Nova igra', font=('Verdana', 18),size=(10,2),key='nova')],[sg.Text('', font=('Courier',25),key='greske')]]
    #print(layout)
    win = sg.Window('Memory', layout)
    while True:
        e,v = win.read()
        
        if e == sg.WIN_CLOSED:
            ng = False
            break
        if e in list_key and c!=2:
            c+=1
            win[e].update(visible=False)
            win[f'img{e}'].update(visible=True)
            if c == 1:
                prva = polja[int(e)-1]
                prvi_click = e
            if c == 2:
                druga = polja[int(e)-1]
                drugi_click = e
        if prva != druga:
            if c == 2 and e!='match' and e!='unmatch':
                threading.Thread(target=wait_unmatch, args=(1,win), daemon=True).start()
        elif prva == druga:
            
            if c == 2 and e!='match' and e!='unmatch':
                threading.Thread(target=wait_match, args=(1,win), daemon=True).start()
            
        if e == 'unmatch':
            greske+=1
            win[prvi_click].update(visible=True)
            win[f'img{prvi_click}'].update(visible=False)
            win[drugi_click].update(visible=True)
            win[f'img{drugi_click}'].update(visible=False)
            c = 0
        elif e == 'match':
            igra_gotova+=1
            c=0
        if igra_gotova == 18:
            win['greske'].update(f'Igra završena! Broj greški: {greske}')
        if e == 'nova':
            ng = True
            break
    win.close()
    return ng
nova_igra = window(polja)
while nova_igra:
    s(polja)
    nova_igra = window(polja)
