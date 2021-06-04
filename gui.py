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

layout = [[psg.Column(left_col, justification="c", key='mytabs'), psg.Column(right_col)]]

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
                window2.refresh()
            break

    window2.close()

def read_window():
    sort_by_list = ["podkładka", "mięso", "dodatki"]
    third_layout = [[psg.Text("What do you want to eat today?", size=(25, 1))],
                     [psg.Text("Select dinner by: ", size=(15, 1)), psg.Combo(sort_by_list)],
                     [psg.Text("Select podkładka ", size=(15, 1)), psg.Combo(baza.get_db_podkladka(), key='-PODK-', readonly=True)],
                    [psg.Text("Select mięso ", size=(15, 1)), psg.Combo(baza.get_db_mieso(), key='-MIES-', readonly=True)],
                     [psg.Text("Dodatki", size=(15, 1))],
                     [psg.Listbox(baza.get_db_dodatki(), select_mode='extended', key='-DODATKI-', size=(30, 6))],
                     [psg.Button("Submit"), psg.Button("Cancel", key='-CANCEL-')]]
    window3 = psg.Window("Obiad - podgląd", third_layout, modal=True).Finalize()
    while True:
        event, values = window3.read()
        if event == psg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
    window3.close()

def update_window():
    update_layout = [[psg.Text("Select what do you want to update", size=(25, 1))],
                     [psg.Button("Podkładka", size=(15, 1))],
                     [psg.Button("Mięso", size=(15, 1))],
                     [psg.Button("Dodatki", size=(15, 1))],
                     [psg.Button("Cancel", key='-CANCEL-')]]
    window4 = psg.Window("Update", update_layout, modal=True).Finalize()
    while True:
        event, values = window4.read()
        if event == psg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        elif event == "Podkładka":
            add_new_podkladka_window()
        elif event == "Mięso":
            add_new_mieso_window()
        elif event == "Dodatki":
            add_new_dodatki_window()
    window4.close()
def add_new_podkladka_window():
    add_new_layout = [[psg.Text("Add new position: ", size=(15,1)), psg.In(key='-NEW-')],
                      [psg.Button("OK")]]
    window5 = psg.Window("Add new", add_new_layout, modal=True).Finalize()
    while True:
        event, values = window5.read()
        if event == psg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_podkladka((str(values['-NEW-'])))
            window5.refresh()
            break
    window5.close()

def add_new_mieso_window():
    add_new_layout = [[psg.Text("Add new position: ", size=(15, 1)), psg.In(key='-NEW-')],
                          [psg.Button("OK")]]
    window5 = psg.Window("Add new", add_new_layout, modal=True).Finalize()
    while True:
        event, values = window5.read()
        if event == psg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_mieso((str(values['-NEW-'])))
            break
    window5.close()
def add_new_dodatki_window():
    add_new_layout = [[psg.Text("Add new position: ", size=(15,1)), psg.In(key='-NEW-')],
                      [psg.Button("OK")]]
    window5 = psg.Window("Add new", add_new_layout, modal=True).Finalize()
    while True:
        event, values = window5.read()
        if event == psg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_dodatki((str(values['-NEW-'])))
            break
    window5.close()
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Create":
        new_window()
    elif event == "Read":
        read_window()
    elif event == "Update":
        update_window()
    elif event == 'mytabs':
      activeTab = window['mytabs'].Get()
    elif event == "Delete":
        if psg.popup_yes_no("Are you sure you want to delete this record?"):
            list_elements= window.Element('-TAB_OBIAD-').Get()
            costamn= tab_group.find_key_from_tab_name(tab_group.Get())
            #activeTab = window['mytabs'].Get()

            print(list_elements,"\n",costamn)
            print(list_elements[values['-TAB_OBIAD-'][0]][0])
            baza.delete_obiad(list_elements[values['-TAB_OBIAD-'][0]][0])
        #     currently selected tab
        #     https://pysimplegui.readthedocs.io/en/latest/#the-qt-tableget-call



        else:
            break


window.close()


