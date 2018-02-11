from tkinter import *
from abc import abstractmethod

global DataList
DataList = []

class Window:
    def __init__(self):
        self.window = Tk()

    @abstractmethod
    def show(self):
        self.window.mainloop()

    @abstractmethod
    def childDestroy(self, event):
        self.window.deiconify()

class ManualInputWindow(Window):
    def __init__(self):
        super().__init__()
        self.titleLabel = Label(self.window, text = 'Окно ручного ввода')

    def show(self):
        self.window.geometry('400x300')
        self.titleLabel.pack(side = 'top')
        super().show()

class FileInputWindow(Window):
    def __init__(self):
        super().__init__()
        self.titleLabel = Label(self.window, text = 'Окно файлового ввода')

    def show(self):
        self.window.geometry('400x300')
        self.titleLabel.pack(side = 'top')
        super().show()

class MachineLearningWindow(Window):
    def __init__(self):
        super().__init__()
        self.titleLabel = Label(self.window, text = 'Окно обучения')

    def show(self):
        self.window.geometry('400x300')
        self.titleLabel.pack(side = 'top')
        super().show()


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.MIB = Button(self.window, text = 'Ручной ввод') # MIB - Manual Input Button
        self.FIB = Button(self.window, text = 'Ввод из файла') # FIB - File Input Button
        self.DIB = Button(self.window, text = 'Ввод с устройства') # DIB - Device Input Button
        self.MLB = Button(self.window, text = 'Обучение') # MLB - Machine Learning Button

        self.MIB.bind('<Button-1>', self.MIBClick)
        self.FIB.bind('<Button-1>', self.FIBClick)
        self.DIB.bind('<Button-1>', self.DIBClick)
        self.MLB.bind('<Button-1>', self.MLBClick)

        self.show()

    def show(self):

        self.window.geometry('230x110')

        self.MIB.place(x = 0, y = 0, width = 110, height = 50)
        self.FIB.place(x = 0, y = 60, width = 110, height = 50)
        self.DIB.place(x = 120, y = 0, width = 110, height = 50)
        self.MLB.place(x = 120, y = 60, width = 110, height = 50)

        super().show()

    def MIBClick(self, event):
        self.window.withdraw()
        newWindow = ManualInputWindow()
        newWindow.window.bind('<Destroy>', self.childDestroy)
        newWindow.show()

    def FIBClick(self, event):
        self.window.withdraw()
        newWindow = FileInputWindow()
        newWindow.window.bind('<Destroy>', self.childDestroy)
        newWindow.show()

    def DIBClick(self, event):
        pass

    def MLBClick(self, event):
        self.window.withdraw()
        newWindow = MachineLearningWindow()
        newWindow.window.bind('<Destroy>', self.childDestroy)
        newWindow.show()



main = MainWindow()
