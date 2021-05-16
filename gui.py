import PySimpleGUI as psg

import baza

psg.theme("GreenTan")

left_col = [psg.Button("Create")],[psg.Button("Read")],[psg.Button("Update")],[psg.Button("Delete")]

data = baza.get_db_obiad()
headings2 = ['Id','Nazwa', 'Podkladka', 'Mieso', 'Dodatki']
layout_obiad = [[psg.Table(values=data[1:][:], headings=headings2, max_col_width= True,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TABLE0-',
                    row_height=35)]]

data = baza.get_db_podkladka()
headings = ['Id','Nazwa']
layout_podkladka = [[psg.Table(values=data[1:][:], headings=headings, max_col_width= 100,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TABLE1-',
                    row_height=35)]]

data2 = baza.get_db_mieso()
headings = ['Id','Nazwa']
layout_mieso = [[psg.Table(values=data2[1:][:], headings=headings, max_col_width= 100,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TABLE2-',
                    row_height=35)]]

data3 = baza.get_db_dodatki()
headings = ['Id','Nazwa']
layout_dodatki = [[psg.Table(values=data3[1:][:], headings=headings, max_col_width= 100,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TABLE3-',
                    row_height=35)]]

right_col = [[psg.TabGroup([[psg.Tab("Obiad", layout_obiad),
                             psg.Tab("Podkładka", layout_podkladka),
                             psg.Tab("Mięso", layout_mieso),
                             psg.Tab("Dodatki", layout_dodatki)]])]]

layout = [[psg.Column(left_col, justification="c"), psg.Column(right_col)]]

window = psg.Window("Mniam mniam picker", layout).Finalize()
window.Maximize()
while True:
    event, values = window.read()
    print(event, values)
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    if event == "Do":
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()

