import PySimpleGUI as psg
import random
import string

psg.theme("GreenTan")

left_col = [psg.Button("Create")],[psg.Button("Read")],[psg.Button("Update")],[psg.Button("Delete")]

layout_obiad = [[psg.Table('Persistent window')]]
layout_podkladka = [[psg.Text('Persistent window')]]
layout_mieso = [[psg.Text('Persistent window')]]

def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data


data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]
layout_dodatki = [[psg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],]

right_col = [[psg.TabGroup([[psg.Tab("Obiad", layout_obiad),
                             psg.Tab("Podkładka", layout_podkladka),
                             psg.Tab("Mięso", layout_mieso),
                             psg.Tab("Dodatki", layout_dodatki)]])]]

layout = [[psg.Column(left_col, justification="c"), psg.Column(right_col)]]

window = psg.Window("Mniam mniam picker", layout)#.Finalize()
#window.Maximize()
while True:
    event, values = window.read()
    print(event, values)
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    if event == "Do":
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()

