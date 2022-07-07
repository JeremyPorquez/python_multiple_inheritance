from threading import Thread
from time import sleep
from PySide6 import QtCore


class A(Thread):
    def __init__(self, variable=None):
        super().__init__(daemon=True)
        self.variable = variable

    def run(self):
        while True:
            print('A')
            sleep(1)


class B(QtCore.QObject):
    my_name = "this is B"

    def run(self):
        while True:
            print(self.variable)
            sleep(1)


class C(A, B, QtCore.QThread):
    def __init__(self):
        A.__init__(self, "this is A")
        B.__init__(self)
        QtCore.QThread.__init__(self)
        print(self.variable)
        print(self.my_name)
        self.variable = "this"
        print(self.variable)

    def run(self):
        print(self.my_name)
        QtCore.QThread.sleep(1)
        print(self.my_name)
        B.run(self)


if __name__ == "__main__":
    c = C()
    c.start()
