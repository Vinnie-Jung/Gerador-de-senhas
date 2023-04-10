import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):

        # Layout
        sg.theme('Black')
        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Text('Website/Software', size=(15, 1)),
             sg.Input(key='website', size=(20, 1)), sg.Push()],
            [sg.Push(), sg.Text('E-mail/User', size=(15, 1)),
             sg.Input(key='user', size=(20, 1)), sg.Push()],
            [sg.Push(), sg.Text('Password size'),
             sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1)), sg.Push()],
            [sg.Push(), sg.Output(size=(32, 5)), sg.Push()],
            [sg.Push(), sg.Button('Generate'), sg.Push()],
            [sg.VPush()]
        ]

        # Window
        self.window = sg.Window('Password Generator', layout, size=(500, 500))

    def Start(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Generate':
                new_password = self.GeneratePassword(values)
                print(new_password)
                self.SavePassword(new_password, values)

    def GeneratePassword(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(values['total_chars']))
        return ''.join(chars)

    def SavePassword(self, new_password, values):
        with open('passwords.txt', 'a', newline='') as file:
            file.write(f"website: {values['website']}, user: {values['user']}, new password: {new_password} /n")
            print('File saved!')

gen = PassGen()
gen.Start()