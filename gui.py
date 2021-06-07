import PySimpleGUI as sg

import baza

sg.theme("GreenTan")

left_col = [sg.Button("Create")],[sg.Button("Read")],[sg.Button("Update")],[sg.Button("Delete")]

data = baza.get_db_obiad()
print(data)
headings2 = ['Id', 'Nazwa', 'Podkladka', 'Mieso', 'Dodatki']
layout_obiad = [[sg.Table(values=data[0:][:], headings=headings2, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_OBIAD-',
                    row_height=35)]]

data1 = baza.get_db_podkladka()
headings3 = ['Id','Nazwa']
layout_podkladka = [[sg.Table(values=data1[0:][:], headings=headings3, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_PODKLADKA-',
                    row_height=35)]]

data2 = baza.get_db_mieso()
headings4 = ['Id','Nazwa']
layout_mieso = [[sg.Table(values=data2[0:][:], headings=headings4, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_MIESO-',
                    row_height=35)]]

data3 = baza.get_db_dodatki()
headings5 = ['Id','Nazwa']
layout_dodatki = [[sg.Table(values=data3[0:][:], headings=headings5, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_DODATKI-',
                    row_height=35)]]

tab_group = sg.TabGroup([[sg.Tab("Obiad", layout_obiad),
                             sg.Tab("Podkładka", layout_podkladka),
                             sg.Tab("Mięso", layout_mieso),
                             sg.Tab("Dodatki", layout_dodatki)]],
                        key='-TAB_GROUP-',
                        enable_events=True)
right_col = [[tab_group]]
# tab_keys = ('-TAB_OBIAD-', '-TAB_PODKLADKA-', '-TAB_MIESO-', '-TAB_DODATKI-')

layout = [[sg.Column(left_col, justification="c", key='mytabs'), sg.Column(right_col)]]

window = sg.Window("Mniam mniam picker", layout).Finalize()
window.Maximize()
def get_table_name_from_tab(active_tab_name):
    tabname_dict = {
        "Obiad" : "obiad",
        "Podkładka" : "podkladka",
        "Mięso" : "mieso",
        "Dodatki" : "dodatki"
    }
    # tu pobierasz tab_name- string który jest zwracany jako nazwa aktywnej zakładki, i zwracasz poprawną nazwę tabeli z bazy. Możesz to zrobić słownikiem.
    return tabname_dict[active_tab_name]
def get_table_key_from_tab(active_tab_name):
    tabkey_dict = {
        "Obiad" : "-TAB_OBIAD-",
        "Podkładka" : "-TAB_PODKLADKA-",
        "Mięso" : "-TAB_MIESO-",
        "Dodatki" : "-TAB_DODATKI-"
    }
    # tu pobierasz tab_name- string który jest zwracany jako nazwa aktywnej zakładki, i zwracasz poprawną nazwę tabeli z bazy. Możesz to zrobić słownikiem.
    return tabkey_dict[active_tab_name]
def create_window():
    second_layout = [[sg.Text("Nazwa ", size=(15,1)), sg.In(key='-NAZWA-')],
              [sg.Text("Podkładka ", size=(15,1)), sg.Combo(baza.get_db_podkladka(), key='-PODKLADKA-', readonly=True)],
              [sg.Text("Mięso ", size=(15,1)), sg.Combo(baza.get_db_mieso(), key='-MIESO-', readonly=True)],
            [sg.Text("Dodatki", size=(15,1))],
            [sg.Listbox(baza.get_db_dodatki(), select_mode='extended', key='-DODATKI-', size=(30, 6))],
             [sg.Button("Submit"), sg.Button("Cancel")]]
    window2 = sg.Window("Obiad - podgląd", second_layout, modal=True).Finalize()
    window2.Maximize()
    while True:
        event, values = window2.read()

        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
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
    third_layout = [[sg.Text("What do you want to eat today?", size=(25, 1))],
                     [sg.Text("Select dinner by: ", size=(15, 1)), sg.Combo(sort_by_list)],
                     [sg.Text("Select podkładka ", size=(15, 1)), sg.Combo(baza.get_db_podkladka(), key='-PODK-', readonly=True)],
                    [sg.Text("Select mięso ", size=(15, 1)), sg.Combo(baza.get_db_mieso(), key='-MIES-', readonly=True)],
                     [sg.Text("Dodatki", size=(15, 1))],
                     [sg.Listbox(baza.get_db_dodatki(), select_mode='extended', key='-DODATKI-', size=(30, 6))],
                     [sg.Button("Submit"), sg.Button("Cancel", key='-CANCEL-')]]
    window3 = sg.Window("Obiad - podgląd", third_layout, modal=True).Finalize()
    while True:
        event, values = window3.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
    window3.close()

def update_window():
    update_layout = [[sg.Text("Update position: ", size=(15,1)), sg.In(key='-NEW-')],
                      [sg.Button("OK"),sg.Button("Cancel")]]
    window4 = sg.Window("Update", update_layout, element_justification='c', modal=True).Finalize()
    while True:
        event, values = window4.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
    window4.close()
def add_new_podkladka_window():
    add_new_layout = [[sg.Text("Add new position: ", size=(15,1)), sg.In(key='-NEW-')],
                      [sg.Button("OK"),sg.Button("Cancel")]]
    window5 = sg.Window("Add new", add_new_layout, modal=True).Finalize()
    while True:
        event, values = window5.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_podkladka((str(values['-NEW-'])))
            window5.refresh()
            break
    window5.close()

def add_new_mieso_window():
    add_new_layout = [[sg.Text("Add new position: ", size=(15, 1)), sg.In(key='-NEW-')],
                          [sg.Button("OK"),sg.Button("Cancel")]]
    window5 = sg.Window("Add new", add_new_layout, modal=True).Finalize()
    while True:
        event, values = window5.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_mieso((str(values['-NEW-'])))
            break
    window5.close()
def add_new_dodatki_window():
    add_new_layout = [[sg.Text("Add new position: ", size=(15,1)), sg.In(key='-NEW-')],
                      [sg.Button("OK"),sg.Button("Cancel")]]
    window5 = sg.Window("Add new", add_new_layout, modal=True).Finalize()
    while True:
        event, values = window5.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_dodatki((str(values['-NEW-'])))
            break
    window5.close()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
        break
    elif event == "Create":
        active_tab_name = tab_group.find_key_from_tab_name(tab_group.Get())  # heading aktywnej zakładki
        if active_tab_name == "Obiad":
            create_window()
        if active_tab_name == "Podkładka":
            add_new_podkladka_window()
        if active_tab_name == "Mięso":
            add_new_mieso_window()
        if active_tab_name == "Dodatki":
            add_new_dodatki_window()

    elif event == "Read":
        read_window()

    elif event == "Update":
        active_tab_name = tab_group.find_key_from_tab_name(tab_group.Get())  # heading aktywnej zakładki
        if active_tab_name == "Obiad":
            create_window()
        if active_tab_name == "Podkładka":
            update_window()
        if active_tab_name == "Mięso":
            update_window()
        if active_tab_name == "Dodatki":
            update_window()

    elif event == "Delete":
        if sg.popup_yes_no("Are you sure you want to delete this record?"):

            active_tab_name = tab_group.find_key_from_tab_name(tab_group.Get()) #heading aktywnej zakładki
            list_elements = window.Element(get_table_key_from_tab(str(active_tab_name))).Get() #zwraca klucz aktywnej zakl
            print(list_elements, "\n",active_tab_name)
            print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0]) #print id zaznaczonego rowa
            baza.delete_from_db(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0],get_table_name_from_tab(str(active_tab_name)))
        else:
            break


window.close()


