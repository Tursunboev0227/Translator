from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QListWidget
from PyQt5.Qt import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(300, 60)
        self.setStyleSheet('''
                        background: #146C94;
                        font-size: 25px;
                        border: 2px solid;
                        border-radius: 15px 
                        ''')
        

class FooterButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(150, 40)
        self.setStyleSheet('''
                        background: #146C94;
                        font-size: 20px;
                        border: 2px solid;
                        border-radius: 15px 
                        ''')

class Label(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet('''font-size: 20px;''')
        self.setAlignment(Qt.AlignCenter)

class Edit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
                        font-size: 25px;
                        background: #F6F1F1;
                        border: 2px solid;
                        border-radius: 15px;
                        padding: 0 10px;                          
                        """)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(500, 600)
        self.setStyleSheet('background: #AFD3E2')

class QLW(QListWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('''
                        font-size:25px;
                        background: #F6F1F1;
                        border: 2px solid;
                        border-radius: 15px;
                        padding: 0 10px; 
                        ''')