# import baza
# import gui
#
#
#
# def update_obiad_window():
#     active_tab_name = gui.tab_group.find_key_from_tab_name(gui.tab_group.Get())
#     list_elements = gui.window.Element(gui.get_table_key_from_tab(str(active_tab_name))).Get()
#
#     selected_element_name = gui.window.Element(str('-TAB_OBIAD-')).Get()
#     selected_podk = list_elements[0][2]
#     selected_mieso = list_elements[0][3]
#     selected_dod = list_elements[0][4]
#     # # print(list_elements[values[get_table_key_from_tab(str(active_tab_name))][0]][0])  # # print id zaznaczonego rowa
#     update_obiad_layout = [
#         [gui.sg.Text("Nazwa ", size=(15, 1)), gui.sg.InputText(str(selected_element_name), key='-UPD_TEXT-')],
#         [gui.sg.Text("Podkładka ", size=(15, 1)),
#          gui.sg.Combo(baza.get_db_podkladka(), str(selected_podk), key='-PODKLADKA-', readonly=True)],
#         [gui.sg.Text("Mięso ", size=(15, 1)),
#          gui.sg.Combo(baza.get_db_mieso(), str(selected_mieso), key='-MIESO-', readonly=True)],
#         [gui.sg.Text("Dodatki", size=(15, 1))],
#         [gui.sg.Listbox(baza.get_db_dodatki(), (selected_dod), select_mode='extended', key='-DODATKI-', size=(30, 6))],
#         [gui.sg.Button("Submit"), gui.sg.Button("Cancel")]]
#     window2 = gui.sg.Window("Obiad - podgląd", update_obiad_layout, modal=True).Finalize()
#     window2.Maximize()
#     while True:
#         event, values = window2.read()
#
#         if event == gui.sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
#             break
#
#         elif event == "Submit":
#             # print("debug", type(values))
#
#             new_obiad_id = baza.add_obiad(str(values['-PODKLADKA-'][0]), str(values['-MIESO-'][0]),
#                                           str(values['-NAZWA-']))
#             a = values['-DODATKI-']
#             for row in a:
#                 # print(row)
#                 baza.add_dodatkiobiadrelation(row[0], new_obiad_id)
#                 window2.refresh()
#             break
#
#     window2.close()
#
#
# def update_window():
#     active_tab_name = gui.tab_group.find_key_from_tab_name(gui.tab_group.Get())
#     list_elements = gui.window.Element(gui.get_table_key_from_tab(str(active_tab_name))).Get()
#
#     element_id = list_elements[1][0]
#
#     update_layout = [[gui.sg.Text("Update position: ", size=(15, 1)), gui.sg.InputText(key= '-UPDATED_TEXT-')],
#                      [gui.sg.Button("OK"), gui.sg.Button("Cancel")]]
#     window4 = gui.sg.Window("Update", update_layout, element_justification='c', modal=True).Finalize()
#     window4.refresh()
#     event, values = window4.read()
#     selected_element_name = list_elements[values[gui.get_table_key_from_tab(str(active_tab_name))][0]][1]  # # print id zaznaczonego rowa
#     window4['-UPDATED_TEXT-'].Update(default_text = selected_element_name)
#
#
#     while True:
#         event, values = window4.read()
#         active_tab_name = gui.tab_group.find_key_from_tab_name(gui.tab_group.Get())
#         list_elements = gui.window.Element(gui.get_table_key_from_tab(str(active_tab_name))).Get()
#         if event == gui.sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
#             break
#         if event == "OK":
#             if active_tab_name == "Podkładka":
#                 baza.update_podkladka(str(values['-UPDATED_TEXT-']), element_id)
#             elif active_tab_name == "Mięso":
#                 baza.update_mieso(str(values['-UPDATED_TEXT-']),element_id)
#             elif active_tab_name == "Dodatki":
#                 baza.update_dodatki(str(values['-UPDATED_TEXT-']), element_id)
#             elif active_tab_name == "Obiad":
#                 baza.update_obiad(str(values['-UPDATED_TEXT-']), element_id)
#             # print("debug")
#
#
#
#     window4.close()
#
#
# # active_tab_name = tab_group.find_key_from_tab_name(tab_group.Get())  # heading aktywnej zakładki
# # if active_tab_name == "Obiad":
# #     cos.update_obiad_window()
# # if active_tab_name == "Podkładka":
# #     cos.update_window()
# # if active_tab_name == "Mięso":
# #     cos.update_window()
# # if active_tab_name == "Dodatki":
# #     cos.update_window()

# zad.1
# import random
# # print(random.randrange(1,7))
#
# zad.2
# a = str(input())
# # print("Hello",a)
#
# zad.3
# a = int(input("Podaj liczbę gości: "))
# b = int(input("Podaj liczbę cukierków: "))
# c = b % a
# # print(c)
#
# zad.4
# # print(20*"*")
#
# zad.5
# a = input("Podaj liczbę: ")
# b = len(a)
# if b < 5:
#     # print("Liczba ma ", b, " cyfry")
# else:
#     # print("Liczba ma ", b, " cyfr")
#
# zad.6
# try:
#     a = int(input())
#     # print(a * 10)
# except:
#     # print("To nie jest poprawna liczba")
#
# zad.7
# a = str(input())
# # print(a[0])
#
# zad.8
# a = int(input())
# if a % 2 == 0:
#     # print("parzysta")
# else:
#     # print("nieparzysta")
#
# zad.9
# try:
#     a = int(input('Podaj wiek'))
#     b = 'jesteś nastolatkiem'
#     if a>13 and a<18:
#         # print(b)
#     else:
#         # print('Nie',b)
# except:
#     # print('Niepoprawne dane')
#
# zad.11
# a = str(input())
# if a[0] == "m" or a[0] == "M":
#     # print("ok")
# else:
#     # print("no")
#
# zad.12
# a = str(input())
# if "kot" in a:
#     # print("true")
# else:
#     # print("false")
#
# zad.13
# a = str(input())
# # print(a.lower())
#
# zad.15
# a = str(input())
# if a[-1] == "m" or a[-1] == "M":
#     # print("ok")
# else:
#     # print("no")
#
# zad.16
# a = int(input())
# b = int(input())
# if a > b:
#     # print(a)
# else:
#     # print(b)
#
# zad.17
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b > c:
#     # print(a)
# else:
#     # print(b)
#
# zad.18
# a = int(input())
# b = int(input())
# # print((a+b)/2)
#
# zad.19
# a = str(input())
# if a[-1] == "a" and a!= "Barnaba":
#     # print("żeńskie")
# else:
#     # print("męskie")
#
# zad.21
# a = int(input())
# # print(1/a)
#
# zad.22
# import random
# # print(random.randrange(1,101))
#
# zad.23
# import math
# r = int(input())
# # print(math.pi*r*r)
#
# zad.24
# a = str(input())
# if a[0] == "A":
#     # print("true")
# else:
#     # print("false")
#
# zad.25
# a = str(input())
# b = str(input())
# if a == b:
#     # print("tak")
# else:
#     # print("nie")
#
# zad.26
# a = str(input())
# b = a[::-1]
# if a == b:
#     # print("palindrom")
# else:
#     "no"


