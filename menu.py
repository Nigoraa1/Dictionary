from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout


class Menu(QWidget):
    def __init__(self) -> None:
        super().__init__()
    
        self.setWindowTitle("My dictionary 📘")
        self.setStyleSheet("background-color: black; color: black")

        self.initUI()
        self.show()



    def initUI(self):
        self.vbox = QVBoxLayout()


    #Add new word tugmasi 
        self.btn_add_word = QPushButton("Add new word",self)
        self.btn_add_word.setStyleSheet("font-size: 75 px; font-weight:bold; background-color: blue")
        self.btn_add_word.setGeometry(75,80,150,50)

        self.btn_add_word.clicked.connect(self.add_word)
        
    #list of words tugmasi
        self.btn_list = QPushButton("List of words",self)
        self.btn_list.setStyleSheet("font-size: 75 px; font-weight :bold; background-color: blue")
        self.btn_list.setGeometry(75,140,150,50)

        self.btn_list.clicked.connect(self.list_of_words)


    #Search word tugmasi
        self.btn_search = QPushButton("Search word",self)
        self.btn_search.setStyleSheet("font-size: 75 px; font-weight :bold; background-color: blue")
        self.btn_search.setGeometry(75,200,150,50)

        self.btn_search.clicked.connect(self.search_word)



    #Exit tugmasi
        self.btn_exit = QPushButton("Exit",self)
        self.btn_exit.setFixedSize(150,50)
        self.btn_exit.setStyleSheet("font-size: 75 px; font-weight :bold; background-color: blue")
        self.btn_exit.setGeometry(75,260,150,50)

        self.btn_exit.clicked.connect(self.exit)



    def  list_of_words(self):
        self.close()
        return "list"



    def add_word(self):
        self.close()
        return "add_word"
    


    def search_word(self):
        self.close()
        return "search"
    


    def exit(self):
        self.close()
    
     

    
app = QApplication([])
win = Menu()
app.exec_()









