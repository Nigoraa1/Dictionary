from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QApplication
from DATABASE  import*
from menu import*



class Add_new_word(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(300,400)
        self.setWindowTitle("Add new words")
        self.setStyleSheet("background-color: black; color: purple")
        
        self.initUI()
        self.database = Database()
        self.show()



    def initUI(self):

        self.eng_word_editor = QLineEdit()
        self.eng_word_editor.setPlaceholderText("English...")
        self.eng_word_editor.setStyleSheet("background-color: white; color: purple")


        self.uzb_word_editor = QLineEdit()
        self.uzb_word_editor.setPlaceholderText("Uzbek...")
        self.uzb_word_editor.setStyleSheet("background-color: white; color: purple")


        self.label = QLabel("")
        self.label.setStyleSheet("font-size: 30px")
        
 
        self.btn_send = QPushButton("Send")
        self.btn_send.setStyleSheet("background-color: blue; color: black")
        self.btn_send.clicked.connect(self.send_button_clicked)


        self.btn_menu = QPushButton("Menu")
        self.btn_menu.setStyleSheet("background-color: blue; color: black")
        #self.btn_menu.clicked.connect(self.menu)

        self.btn_list = QPushButton("List of words")
        self.btn_list.setStyleSheet("background-color: blue; color: black")

        self.btn_search = QPushButton("Search")
        self.btn_search.setStyleSheet("background-color: blue; color: black")


    #buttonlani joylashtirish
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.btn_menu)
        self.hbox.addWidget(self.btn_list)
        self.hbox.addWidget(self.btn_search)

        self.vbox.addWidget(self.eng_word_editor)
        self.vbox.addWidget(self.uzb_word_editor)
        self.vbox.addWidget(self.btn_send)
        self.vbox.addWidget(self.label)
        self.vbox.addStretch()
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


    #send tugmasi bosilganda chaqiriladigon metod
    def send_button_clicked(self):
        uzb_word = self.uzb_word_editor.text()
        eng_word = self.eng_word_editor.text()

        #editor bo'shmi yo'qmi tekshirish unda so'z bo'lsa so'zni database ga yozish
        if len(uzb_word) != 0 and len(eng_word) != 0:
            self.database.insert_new_word(eng_word,uzb_word)

            self.eng_word_editor.clear()
            self.uzb_word_editor.clear()
            self.label.setText("New word saved !")
        else:
            self.label.setText("It is empty !")



    #def menu(self):
    #    menu = Menu()
    #    menu.show()
    #    self.close()
        



app = QApplication([])
win = Add_new_word()
app.exec_()




            


