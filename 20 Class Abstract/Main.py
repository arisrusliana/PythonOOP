# abstract class menginstanciate class / blueprint dari class
# abstract class memaksa class untuk mengimplementasikan method dari abstract class
# method pada abstract class akan diimplementasikan pada class

# membuat abstract class
# abc = abstract base class

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        print("button click")

class PushButton(Button):
    def click(self):
        print("push button clicked")

class RadioButton(Button):
    def click(self):
        print("radio button clicked")

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
# help(tombol1)