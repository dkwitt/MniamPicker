import PySimpleGUI as psg

import baza
current_tab = 1
psg.theme("GreenTan")

left_col = [psg.Button("Create")],[psg.Button("Read")],[psg.Button("Update")],[psg.Button("Delete")]

data = baza.get_db_obiad()
print(data)
headings2 = ['Id', 'Nazwa', 'Podkladka', 'Mieso', 'Dodatki']
layout_obiad = [[psg.Table(values=data[0:][:], headings=headings2, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_OBIAD-',
                    row_height=35)]]

data1 = baza.get_db_podkladka()
headings3 = ['Id','Nazwa']
layout_podkladka = [[psg.Table(values=data1[0:][:], headings=headings3, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_PODKLADKA-',
                    row_height=35)]]

data2 = baza.get_db_mieso()
headings4 = ['Id','Nazwa']
layout_mieso = [[psg.Table(values=data2[0:][:], headings=headings4, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_MIESO-',
                    row_height=35)]]

data3 = baza.get_db_dodatki()
headings5 = ['Id','Nazwa']
layout_dodatki = [[psg.Table(values=data3[0:][:], headings=headings5, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_DODATKI-',
                    row_height=35)]]

tab_group = psg.TabGroup([[psg.Tab("Obiad", layout_obiad),
                             psg.Tab("Podkładka", layout_podkladka),
                             psg.Tab("Mięso", layout_mieso),
                             psg.Tab("Dodatki", layout_dodatki)
                             ]])
right_col = [[tab_group]]

layout = [[psg.Column(left_col, justification="c"), psg.Column(right_col)]]

window = psg.Window("Mniam mniam picker", layout).Finalize()
window.Maximize()

def new_window():
    second_layout = [[psg.Text("Nazwa ", size=(15,1)), psg.In(key='-NAZWA-')],
              [psg.Text("Podkładka ", size=(15,1)), psg.Combo(baza.get_db_podkladka(), key='-PODKLADKA-', readonly=True)],
              [psg.Text("Mięso ", size=(15,1)), psg.Combo(baza.get_db_mieso(), key='-MIESO-', readonly=True)],
            [psg.Text("Dodatki", size=(15,1))],
            [psg.Listbox(baza.get_db_dodatki(), select_mode='extended', key='-DODATKI-', size=(30, 6))],
             [psg.Button("Submit"), psg.Button("Cancel", key='-CANCEL-')]]
    window2 = psg.Window("Obiad - podgląd", second_layout, modal=True).Finalize()
    window2.Maximize()
    while True:
        event, values = window2.read()
        print(current_tab)
        if event == psg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        elif event == "Submit":
            print("debug", type(values))

            new_obiad_id=baza.add_obiad(str(values['-PODKLADKA-'][0]), str(values['-MIESO-'][0]), str(values['-NAZWA-']))
            a = values['-DODATKI-']
            for row in a:
                print(row)
                baza.add_dodatkiobiadrelation(row[0],new_obiad_id)
            break

    window2.close()

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Create":
        new_window()
    elif event == "Read":
        psg.popup("popup")
    elif event == "Update":
        new_window()
    elif event == "Delete":
        if psg.popup_yes_no("Are you sure you want to delete this record?"):
            list_elements= window.Element('-TAB_OBIAD-').Get()
            costamn= tab_group.find_key_from_tab_name(tab_group.Get())

            print(list_elements,"\n",costamn)
            # print(list_elements[values['-TAB_OBIAD-'][0]][0])
            baza.delete_obiad(list_elements[values['-TAB_OBIAD-'][0]][0])
        #     currently selected tab
        #     https://pysimplegui.readthedocs.io/en/latest/#the-qt-tableget-call



        else:
            break


window.close()


