from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):

    def __init__(self):

        super().__init__()

        self.label = Label(text='')
        self.input_data = TextInput(hint_text='Введите название файла')
        self.input_data2 = TextInput(hint_text='Введите текст для файла')
        self.button = Button(text='Открыть файл')
        self.button_2 = Button(text='Создать файл')
        self.button_3 = Button(text='Записать в файл')

        self.button.bind(on_press=self.open_file)
        self.button_2.bind(on_press=self.create_file)
        self.button_3.bind(on_press=self.write_file)

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.input_data)
        layout.add_widget(self.input_data2)
        layout.add_widget(self.button)
        layout.add_widget(self.button_2)
        layout.add_widget(self.button_3)
        layout.add_widget(self.label)
        return layout

    def open_file(self, *args):
        name = self.input_data.text
        try:
            with open(name, 'r') as f:
                content = f.read()
                if content:
                    self.label.text = content
                else:
                    self.label.text = "Файл пуст"
        except FileNotFoundError:
            self.label.text = "Такого файла нет"



    def create_file(self, *args):
        name = self.input_data.text
        try:
            with open(name, 'w') as f:
                self.label.text = f"Файл '{name}' создан"
        except Exception as e:
            self.label.text = "Ошибка: " + str(e)


    def write_file(self, *args):
        name = self.input_data.text
        text = self.input_data2.text
        try:
            with open(name, 'a') as f:
                f.write(text + "\n")
                self.label.text = "Текст записан в файл"
        except FileNotFoundError:
            self.label.text = "Такого файла нет"


if __name__ == '__main__':
    MyApp().run()
