from kivy.core.window import Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

import operator

Builder.load_file("design.kv")
Window.size = (360, 640)

class MyInterface(FloatLayout):
    first_number = "0"
    second_number = False
    operation = ""

    def reversing_number(self):
        number = self.ids.user_input.text
        if number[0] != "-":
            self.ids.user_input.text = "-" + number
        else:
            self.ids.user_input.text = number[1:]

    def save_first_number(self, value):
        self.first_number = self.ids.user_input.text
        self.second_number = True
        self.operation = value

    def next_number(self):
        if self.second_number:
            self.ids.user_input.text = "0"
            self.second_number = False

    def to_read(self, value):
        self.next_number()
        if len(self.ids.user_input.text) > 0:
            if value == ".":
                if "." in self.ids.user_input.text:
                    print("У числі є крапка")
                else:
                    self.ids.user_input.text += "."
            elif value == "0" and len(self.ids.user_input.text) == 1:
                if self.ids.user_input.text[0] == "0":
                    self.ids.user_input.text = value
                else:
                    self.ids.user_input.text += value
            elif value != "0" and self.ids.user_input.text[0] == "0":
                if len(self.ids.user_input.text) == 1:
                    self.ids.user_input.text = value
                else:
                    self.ids.user_input.text += value
            else:
                self.ids.user_input.text += value
        else:
            if value != ".":
                self.ids.user_input.text = value

    def to_clear(self):
        self.ids.user_input.text = "0"

    def to_count(self):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        try:
            number_1 = float(self.first_number)
            number_2 = float(self.ids.user_input.text)

            if self.operation in ops:
                if self.operation == "/" and number_2 == "0":
                    return
                func = ops[self.operation]
                res = func(number_1, number_2)
                res = round(res, 12)
                if res == int(res):
                    self.ids.user_input.text = str(int(res))
                else:
                    self.ids.user_input.text = str(res)
                self.first_number = self.ids.user_input.text
                self.operation = ""
            else:
                print("Оператор не було введено!")
        except Exception as e:
            print(f"Помилка обчислення: {e}")
            self.ids.user_input.text = "Error"

class MainApp(App):
    def build(self):
        return MyInterface()

if __name__ == "__main__":
    MainApp().run()

