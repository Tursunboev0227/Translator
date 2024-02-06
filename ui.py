from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import Qt

from css import *
def lst():
    with open("translate.txt") as f:
        data = f.read().split('\n')[:-1]
        data = list(map(lambda i: i.split('|'),data))
    return data 

class MenuWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translate English to Uzbek")
        self.__initUI()
        self.show()


    def __initUI(self):

        self.v_box = QVBoxLayout()
        self.v_box.setAlignment(Qt.AlignCenter)

        self.btn_add_new_word = Button('Add New Word')
        self.btn_list_of_words = Button('List of Words')
        self.btn_search_word = Button('Search Word')
        self.btn_exit = Button('Exit')

        self.v_box.addStretch()
        self.v_box.addWidget(self.btn_add_new_word)
        self.v_box.addWidget(self.btn_list_of_words)
        self.v_box.addWidget(self.btn_search_word)
        self.v_box.addWidget(self.btn_exit)
        self.v_box.addStretch()

        self.setLayout(self.v_box)
        self.btn_add_new_word.clicked.connect(self.show_new_word)
        self.btn_list_of_words.clicked.connect(self.show_list)
        self.btn_search_word.clicked.connect(self.show_search)
        self.btn_exit.clicked.connect(self.exit_window)

    def show_new_word(self):
        self.new = NewWordWindow()
        self.close()

    def show_list(self):
        self.new = ListWordsWindow()
        self.close()

    def show_search(self):
        self.new = SearchWindow()
        self.close()

    def exit_window(self):
        self.close()

class NewWordWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Word")
        self.setFixedSize(500, 600)
        self.__initUI()
        self.show()
    

    def __initUI(self):

        self.v_box = QVBoxLayout()
        self.v_box_edits = QVBoxLayout()
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.edit_eng = Edit()
        self.edit_eng.setPlaceholderText("English...")

        self.edit_uzb = Edit()
        self.edit_uzb.setPlaceholderText("Uzbek...")

        self.btn_save = QPushButton('Save')
        self.btn_save.setFixedSize(80,80)
        self.btn_save.setStyleSheet("""
                                        font-size: 20px;
                                        background: #146C94;
                                        border: 2px solid;
                                        border-radius: 15px;
                                        padding: 0 10px; 
                                    """)

        self.btn_menu = FooterButton('Menu')
        self.btn_list = FooterButton('List of words')
        self.btn_search = FooterButton('Search')

        self.v_box_edits.addWidget(self.edit_eng)
        self.v_box_edits.addWidget(self.edit_uzb)

        self.h_box_lang.addLayout(self.v_box_edits)
        self.h_box_lang.addWidget(self.btn_save)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_list)
        self.h_box_btns.addWidget(self.btn_search)

        self.v_box.addLayout(self.h_box_lang)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box_btns)
        self.setLayout(self.v_box)

        self.btn_menu.clicked.connect(self.ret_menu)
        self.btn_list.clicked.connect(self.lst_menu)
        self.btn_search.clicked.connect(self.search_menu)
        self.btn_save.clicked.connect(self.add_new_word)

    def ret_menu(self):
        self.menu = MenuWindow()
        self.close()
        self.menu.show()

    def lst_menu(self):
        self.lst = ListWordsWindow()
        self.close()
        self.lst.show()

    def search_menu(self):
        self.serach = SearchWindow()
        self.close()
        self.serach.show()
    
    def add_new_word(self):
        eng = self.edit_eng.text()
        uzb = self.edit_uzb.text()
        msg = QMessageBox(self)

        eng, uzb = eng.lower(),uzb.lower()
        
        if eng and uzb:
            self.edit_eng.clear()
            self.edit_uzb.clear()

            with open("translate.txt") as f:
                lst = f.read().split("\n")[:-1]
    

            if not lst:
                with open("translate.txt","a") as f:
                    f.write(f"{eng}|{uzb}\n")
                    msg.setText("Succesfullly ")
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg.exec_()

            else:
                lst = list(map(lambda x: x.split("|"),lst))
                bol = True

                for i in lst:
                    if i[0] == eng:
                        bol = False
                        break

                if bol:
                    with open("translate.txt","a") as f:
                        f.write(f"{eng}|{uzb}\n")  
                        msg.setText("Succesfullly ")
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                        msg.exec_()
        else:
            msg.setText("Iltimos hamma yacheykalarni to'ldiring ")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec_()
        
class ListWordsWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List of Words")
        self.setFixedSize(500, 600)
        self.__initUI()
        self.show()

    def __initUI(self):

        self.v_box = QVBoxLayout()
        self.v_box_eng = QVBoxLayout()
        self.v_box_uzb = QVBoxLayout()
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()


        self.label_eng = Label('English')
        self.label_uzb = Label('Uzbek')

        data = lst()
        self.qlw_eng = QLW()
        self.qlw_uzb = QLW()
        
        self.scroll_bar1 = self.qlw_eng.verticalScrollBar()
        self.scroll_bar2 = self.qlw_uzb.verticalScrollBar()
        self.scroll_bar1.valueChanged.connect(self.scrollBarValueChanged1)
        self.scroll_bar2.valueChanged.connect(self.scrollBarValueChanged2)

        for i in data:
            self.qlw_eng.addItem(i[0])
            self.qlw_uzb.addItem(i[1])


        self.btn_menu = FooterButton('Menu')
        self.btn_new_word = FooterButton('Add New Word')
        self.btn_search = FooterButton('Search')

        self.v_box_eng.addWidget(self.label_eng)
        self.v_box_eng.addWidget(self.qlw_eng)

        self.v_box_uzb.addWidget(self.label_uzb)
        self.v_box_uzb.addWidget(self.qlw_uzb)

        self.h_box_lang.addLayout(self.v_box_eng)
        self.h_box_lang.addLayout(self.v_box_uzb)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_new_word)
        self.h_box_btns.addWidget(self.btn_search)

        self.v_box.addLayout(self.h_box_lang)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)

        self.btn_menu.clicked.connect(self.ret_menu)
        self.btn_new_word.clicked.connect(self.new_word)
        self.btn_search.clicked.connect(self.search_menu)

    def ret_menu(self):
        self.men = MenuWindow()
        self.close()
        self.men.show()

    def new_word(self):
        self.new = NewWordWindow()
        self.close()
        self.new.show()

    def search_menu(self):
        self.search = SearchWindow()
        self.close()
        self.search.show()
    
    def scrollBarValueChanged1(self, value):
        self.scroll_bar2 = self.qlw_uzb.verticalScrollBar()
        self.scroll_bar2.setValue(value)
    
    def scrollBarValueChanged2(self, value):
        self.scroll_bar1 = self.qlw_eng.verticalScrollBar()
        self.scroll_bar1.setValue(value)

class SearchWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Word")
        self.setFixedSize(500, 600)
        self.__initUI()
        self.show()


    def __initUI(self):

        self.v_box = QVBoxLayout()
        self.h_box_search = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.edit_search = Edit()
        self.edit_search.setPlaceholderText("Enter a word...")

        self.btn_search = FooterButton('Search')
        self.btn_search.setFixedHeight(35)

        self.qlw_search = QLW()

        self.btn_menu = FooterButton('Menu')
        self.btn_new_word = FooterButton('Add New Word')
        self.btn_list = FooterButton('List of words')

        self.h_box_search.addWidget(self.edit_search)
        self.h_box_search.addWidget(self.btn_search)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_new_word)
        self.h_box_btns.addWidget(self.btn_list)

        self.v_box.addLayout(self.h_box_search)
        self.v_box.addWidget(self.qlw_search)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)

        self.btn_menu.clicked.connect(self.ret_menu)
        self.btn_new_word.clicked.connect(self.ret_new_word)
        self.btn_list.clicked.connect(self.ret_list)
        self.btn_search.clicked.connect(self.search_wrd)


    def search_wrd(self):
        data = lst()
        text = self.edit_search.text().lower()
        msg = QMessageBox(self)
        bl = True
        if text:
            self.qlw_search.clear()
            for i in data:
                if text == i[0]:
                    self.qlw_search.addItem(i[1])
                    bl = False
                    break
                elif text == i[1]:
                    self.qlw_search.addItem(i[0])
                    bl = False
                    break
            if bl:
                msg.setText("Bunday so'z topilmadi")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec_()
                
    def ret_menu(self):
        self.men = MenuWindow()
        self.close()
        self.men.show()
    
    def ret_new_word(self):
        self.new = NewWordWindow()
        self.close()
        self.new.show()

    def ret_list(self):
        self.lst = ListWordsWindow()
        self.close()
        self.lst.show()
