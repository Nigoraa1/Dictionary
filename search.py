from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QApplication
from DATABASE  import*
from menu import*



class Search(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(300,400)
        self.setWindowTitle("Search")
        self.setStyleSheet("background-color: black; color: purple")
        self.initUI()
        self.database = Database()
        self.show()



    def initUI(self):

        self.word_editor = QLineEdit()
        self.word_editor.setPlaceholderText("word..")
        self.word_editor.setStyleSheet("background-color: white; color: purple")


        self.found_word_editor = QLineEdit()
        self.found_word_editor.setStyleSheet("background-color: white; color: black")

        
        self.btn_send = QPushButton("Search")
        self.btn_send.setStyleSheet("background-color: blue; color: black")
        self.btn_send.clicked.connect(self.searched_word)


        self.btn_menu = QPushButton("Menu")
        self.btn_menu.setStyleSheet("background-color: blue; color: black")
        #self.btn_menu.clicked.connect(self.menu)

        self.btn_list = QPushButton("List of words")
        self.btn_list.setStyleSheet("background-color: blue; color: black")

        self.btn_search = QPushButton("Add_new_word")
        self.btn_search.setStyleSheet("background-color: blue; color: black")


    #buttonlani joylashtirish
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.btn_menu)
        self.hbox.addWidget(self.btn_list)
        self.hbox.addWidget(self.btn_search)

        self.vbox.addWidget(self.word_editor)
        self.vbox.addWidget(self.found_word_editor)
        self.vbox.addWidget(self.btn_send)
        self.vbox.addStretch()
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


    #search tugmasi bosilganda chaqiriladigon metod
    def searched_word(self):
        word = self.word_editor.text()


        #editor bo'shmi yo'qmi tekshirish unda so'z bo'lsa so'zni database dan tarjimasini topish
        if len(word) != 0:
            word = word.casefold()
            w = self.database.searched_word(word)
            self.found_word_editor.setPlaceholderText(w)
        else:
            self.label.setText("Undefined!")



    #def menu(self):
    #    menu = Menu()
    #    menu.show()
    #    self.close()
        



        
app = QApplication([])
win = Search()
app.exec_()




            


