import sys

from PyQt5.QtWidgets import QApplication

from ui import *

app = QApplication(sys.argv)
menu = MenuWindow()

sys.exit(app.exec_())