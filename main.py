from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRoundFlatButton,MDFlatButton,MDFloatingActionButton
from decimal import Decimal

Window.size=(350,600)

class NumericTextInput(TextInput):
    def insert_text(self,substring,from_undo=False):
        if substring.isdigit() or substring==".":
            return super().insert_text(substring,from_undo)

class calculator_layout(MDFloatLayout):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Purple"
        return calculator_layout()

    def clear(self):
        self.root.ids.calc_input.text=''

    def button_press(self,button_num):
        #print("button pressed!")
        #create a var to hold whatever was in the text field already
        temp=self.root.ids.calc_input.text
        if temp=='0':
            self.root.ids.calc_input.text=""
            self.root.ids.calc_input.text=f'{button_num}'
        else:
            self.root.ids.calc_input.text=f'{temp}{button_num}'

    def backspace(self):
        temp=self.root.ids.calc_input.text
        temp=temp[:-1]
        self.root.ids.calc_input.text=temp

    def change_sign(self):
        temp=self.root.ids.calc_input.text
        if "-" in temp:
            self.root.ids.calc_input.text= f'{temp.replace("-","")}'
        else:
            self.root.ids.calc_input.text=f'-{temp}'


    def dot(self):
        temp=self.root.ids.calc_input.text
        parts=temp.split("+") + temp.split("-")
        last_part=parts[-1]
        if '.' in last_part:
            return
        
        temp=f'{temp}.'
        self.root.ids.calc_input.text=temp
            

    def math_sign(self,operator):
        temp=self.root.ids.calc_input.text
        self.root.ids.calc_input.text=f'{temp}{operator}'

    def equals_to(self):
        expression =self.root.ids.calc_input.text
        answer=eval(expression)
        rounded_result=round(answer,5)
        self.root.ids.calc_input.text=str(rounded_result)
        
       




if __name__=="__main__":
    MainApp().run()