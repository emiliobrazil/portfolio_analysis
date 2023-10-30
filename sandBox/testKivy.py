from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

class MyTest(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source='MUG-fish7.jpeg'))

        self.greetings = Label(text = 'Olá! Como vai')
        self.window.add_widget(self.greetings)

        self.dialog01 = TextInput(multiline=False)
        self.window.add_widget(self.dialog01)

        self.button = Button(text='Não Click')
        self.window.add_widget(self.button)

        dropdown = DropDown()
        for index in range(10):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text=f'Não Clica não -  {index}', size_hint_y=None,height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        mainbutton = Button(text='Hello', width = 120, size_hint=(None, None))

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        self.window.add_widget(mainbutton)
        return self.window
    # create a dropdown with 10 buttons
mtest = MyTest()
mtest.run()





