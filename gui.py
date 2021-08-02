import PySimpleGUI as sg

import baza
sg.theme("GreenTan")

left_col = [sg.Button("Create")], [sg.Button("Read")], [sg.Button("Update")], [sg.Button("Delete")]

data = baza.get_db_obiad()
headings2 = ['Id', 'Nazwa', 'Podkladka', 'Mieso', 'Dodatki']
layout_obiad = [[sg.Table(values=data[0:][:], headings=headings2, max_col_width=True,
                          auto_size_columns=False,
                          display_row_numbers=False,
                          enable_events=True,
                          justification='c',
                          alternating_row_color='lightyellow',
                          key='-TAB_OBIAD-',
                          row_height=35)]]

data1 = baza.get_db_podkladka()
headings3 = ['Id', 'Nazwa']
layout_podkladka = [[sg.Table(values=data1[0:][:], headings=headings3, max_col_width=True,
                              auto_size_columns=False,
                              select_mode= 'browse',
                              display_row_numbers=False,
                              enable_events=True,
                              justification='c',
                              alternating_row_color='lightyellow',
                              key='-TAB_PODKLADKA-',
                              row_height=35)]]

data2 = baza.get_db_mieso()
headings4 = ['Id', 'Nazwa']
layout_mieso = [[sg.Table(values=data2[0:][:], headings=headings4, max_col_width=True,
                          auto_size_columns=False,
                          display_row_numbers=False,
                          enable_events=True,
                          justification='c',
                          alternating_row_color='lightyellow',
                          key='-TAB_MIESO-',
                          row_height=35)]]

data3 = baza.get_db_dodatki()
headings5 = ['Id', 'Nazwa']
layout_dodatki = [[sg.Table(values=data3[0:][:], headings=headings5, max_col_width=True,
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

window = sg.Window("Mniam mniam picker", layout, resizable=True).Finalize()
window_main = sg.Window("Mniam mniam picker", layout, resizable=True).Finalize()

def get_table_name_from_tab(active_tab_name):
    tabname_dict = {
        "Obiad": "obiad",
        "Podkładka": "podkladka",
        "Mięso": "mieso",
        "Dodatki": "dodatki"
    }
    return tabname_dict[active_tab_name]


def get_table_key_from_tab(active_tab_name):
    tabkey_dict = {
        "Obiad": "-TAB_OBIAD-",
        "Podkładka": "-TAB_PODKLADKA-",
        "Mięso": "-TAB_MIESO-",
        "Dodatki": "-TAB_DODATKI-"
    }
    return tabkey_dict[active_tab_name]


def create_window():
    second_layout = [[sg.Text("Nazwa ", size=(15, 1)), sg.In(key='-NAZWA-')],
                     [sg.Text("Podkładka ", size=(15, 1)),
                      sg.Combo(baza.get_db_podkladka(), key='-PODKLADKA-', readonly=True)],
                     [sg.Text("Mięso ", size=(15, 1)), sg.Combo(baza.get_db_mieso(), key='-MIESO-', readonly=True)],
                     [sg.Text("Dodatki", size=(15, 1))],
                     [sg.Listbox(baza.get_db_dodatki(), select_mode='multiple', key='-DODATKI-', size=(30, 6))],
                     [sg.Button("Submit"), sg.Button("Cancel")]]
    window2 = sg.Window("Create window", second_layout, resizable=True).Finalize()
    while True:
        event, values = window2.read()

        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break

        elif event == "Submit":
            # print("debug", type(values))
            new_obiad_id = baza.add_obiad(str(values['-PODKLADKA-'][0]), str(values['-MIESO-'][0]),
                                          str(values['-NAZWA-']))
            a = values['-DODATKI-']
            for row in a:
                # print(row)
                baza.add_dodatkiobiadrelation(row[0], new_obiad_id)


            break

    window2.close()


def read_windw():
    sort_by_list = ["podkładka", "mięso", "dodatki"]
    third_layout = [[sg.Text("What do you want to eat today?", size=(25, 1))],
                    [sg.Text("Select dinner by: ", size=(15, 1)), sg.Combo(sort_by_list)],
                    [sg.Text("Select podkładka ", size=(15, 1)),
                     sg.Combo(baza.get_db_podkladka(), key='-PODK-', readonly=True)],
                    [sg.Text("Select mięso ", size=(15, 1)),
                     sg.Combo(baza.get_db_mieso(), key='-MIES-', readonly=True)],
                    [sg.Text("Dodatki", size=(15, 1))],
                    [sg.Listbox(baza.get_db_dodatki(), select_mode='extended', key='-DODATKI-', size=(30, 6))],
                    [sg.Button("Submit"), sg.Button("Cancel", key='-CANCEL-')]]
    window3 = sg.Window("Read window", third_layout, modal=True).Finalize()
    while True:
        event, values = window3.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
    window3.close()


def add_new_podkladka_window():
    add_new_layout = [[sg.Text("Add new position: ", size=(15, 1)), sg.In(key='-NEW-')],
                      [sg.Button("OK"), sg.Button("Cancel")]]
    window4 = sg.Window("Create window", add_new_layout, resizable=True).Finalize()
    while True:
        event, values = window4.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_podkladka((str(values['-NEW-'])))
            break
    window4.close()


def add_new_mieso_window():
    add_new_layout = [[sg.Text("Add new position: ", size=(15, 1)), sg.In(key='-NEW-')],
                      [sg.Button("OK"), sg.Button("Cancel")]]
    window5 = sg.Window("Create window", add_new_layout, resizable=True).Finalize()
    while True:
        event, values = window5.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_mieso((str(values['-NEW-'])))
            break
    window5.close()


def add_new_dodatki_window():
    add_new_layout = [[sg.Text("Add new position: ", size=(15, 1)), sg.In(key='-NEW-')],
                      [sg.Button("OK"), sg.Button("Cancel")]]
    window6 = sg.Window("Create window", add_new_layout, resizable=True).Finalize()
    while True:
        event, values = window6.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break
        if event == "OK":
            baza.add_dodatki((str(values['-NEW-'])))

            break

    window6.close()


def get_lista_record(podkladka_list, podkladka_id):
    print("\nget_lista_record", podkladka_list, "\n", podkladka_id, "\n")
    # podkladka_list[0] = [1,nazwa]       spawdz czy podkladkalist[0][0] == 2 jesli tak, zwroic podkladkalist[0] jesli nie szukaj dalej podkladkalist[0+1]
    for ele in podkladka_list:
        print(ele[1], "ele 0\n")
        if ele[1] == podkladka_id:
            print(ele, "ele return")
            return ele
    return "blad"


def lista_dod(id_zazn_dodatkow, list_all_dod):
    ret_list = []
    for i in range(len(list_all_dod)):
        print(f"i={i}\nlist_all_dod[{i}]={list_all_dod[i]}")
        for ele in id_zazn_dodatkow:
            if list_all_dod[i][0] == ele:
                ret_list.append(i)
                print(f"Append i={i}\n")
    return ret_list  # indeksy w liscie


def update_obiad(old_podkladka_name, old_mieso_name, old_dodatki_names, id_obiad):
    cos = None
    podkladka_list = baza.get_db_podkladka()
    mieso_list = baza.get_db_mieso()
    dodatki_list = baza.get_db_dodatki()
    id_dodatkow = baza.get_id_from_dodatkiobiadrelation(id_obiadu)
    print("**************************", id_dodatkow, "************************************")
    second_layout = [[sg.Text("Nazwa ", size=(15, 1)), sg.In(baza.get_obiad_name(id_obiad))],
                     # [sg.Text("Podkładka ", size=(15,1)), sg.Combo(baza.list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0]) (), default_value= lambda person : baza.get_db_podkladka().sort ( person[0] == super.old_podkladka_id, super.cos)[0], key='up_podkladka', readonly=True)],
                     [sg.Text("Podkładka ", size=(15, 1)),
                      sg.Combo(podkladka_list, default_value=get_lista_record(podkladka_list, old_podkladka_name),
                               readonly=True)],
                     [sg.Text("Mięso ", size=(15, 1)),
                      sg.Combo(baza.get_db_mieso(), default_value=get_lista_record(mieso_list, old_mieso_name),
                               readonly=True)],
                     [sg.Text("Dodatki", size=(15, 1))],
                     [sg.Listbox(baza.get_db_dodatki(), select_mode='multiple', default_values=id_dodatkow, key='cos',
                                 enable_events=True, size=(30, 6))],
                     [sg.Button("Submit"), sg.Button("Cancel")]]
    print(old_dodatki_names, "dodatkiiiiiiii")
    print(baza.get_db_dodatki())
    window7 = sg.Window("Update window", second_layout, resizable=True).Finalize()
    currently_selected_dod = lista_dod(id_dodatkow, dodatki_list)
    # id=1,2,3,4
    # i++
    # listaDod lista_wszystkich_dodatki[i]==ktorys_z(id) to dodaj(i) do indeks_listy_dodatkow
    window7.Element('cos').Update(set_to_index=currently_selected_dod)  # indeks_listy_dodatkow) #wiersze
    # dodatki_list[currently_selected_dod][0]

    while True:
        event, values = window7.read()
        print(values, "debug")

        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            break


        elif event == "Submit":
            print(values, "###############################################################################")
            a = values['cos']
            b = []
            for element in a:
                b.append(element[0])
            baza.update_obiad(values[0], id_obiad, values[1][0], values[2][0], b, id_dodatkow)

            break

    window7.close()


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
        list_elements = window.Element(get_table_key_from_tab(str(active_tab_name))).Get()  # zwraca klucz aktywnej zakl
        # print(list_elements, "\n", active_tab_name)
        # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][1])  # # print nazwa zaznaczonego rowa
        input_text = sg.popup_get_text('Update position', 'Update window', default_text=
        list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][1])
        if active_tab_name == "Obiad":
            id_obiadu = list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0]
            print(id_obiadu, "id obiadu")
            id_podkl_i_mies = baza.get_id_from_obiad(id_obiadu)
            print(id_podkl_i_mies, "id podk i miesa")
            a = baza.get_db_obiad()
            id_dodatkow = baza.get_id_from_dodatkiobiadrelation(id_obiadu)
            print(id_dodatkow, "id dodatkow")
            print(a, "obiad row")
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][2][1])
            print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]], "zaznaczony row")
            list_elements = window.Element(
                get_table_key_from_tab(str(active_tab_name))).Get()  # lista wszystkich elementow okn
            print(list_elements, "list elemets")
            update_obiad(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][2],
                         list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][3],
                         list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][4],
                         list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0])
            podkladka_name = list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][2]
            mieso_name = list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][3]
            dodatki_name = list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][4]
            print(podkladka_name, "podkladka name")
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][1])  # nazwa obiadu
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][2])  # nazwa podkladki
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][3])  # nazwa miesa
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][4])  # nazwa dodatkow
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0])  # id obiadu

        if active_tab_name == "Podkładka":
            baza.update_podkladka(input_text, list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0])
        if active_tab_name == "Mięso":
            baza.update_mieso(input_text, list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0])
        if active_tab_name == "Dodatki":
            baza.update_dodatki(input_text, list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0])


    elif event == "Delete":
        if sg.popup_yes_no("Are you sure you want to delete this record?"):

            active_tab_name = tab_group.find_key_from_tab_name(tab_group.Get())  # heading aktywnej zakładki
            list_elements = window.Element(get_table_key_from_tab(str(active_tab_name))).Get()
            # print(list_elements, "\n",active_tab_name)
            # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0]) ## print id zaznaczonego rowa
            baza.delete_from_db(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0],
                                get_table_name_from_tab(str(active_tab_name)))
        else:
            break

window.close()
