from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QApplication,QTableWidget, QTableWidgetItem

from DATABASE import * 

class Words_list(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(300,400)
        self.setWindowTitle("List of Words")
        self.setStyleSheet("background-color: black; color: purple")
        self.initUI()
        self.show()



    def initUI(self):
        self.database = Database()
        words = self.database.get_all_words()

        self.table = QTableWidget()
        self.table.setColumnCount(2)

        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 120)

        self.table.setHorizontalHeaderLabels(["ENGLISH","UZBEK"])
        self.table.setStyleSheet("background-color: white; color: black")
        self.table.setRowCount(len(words))
        
     

        self.btn_menu = QPushButton("Menu")
        self.btn_menu.setStyleSheet("background-color: blue; color: black")
        #self.btn_menu.clicked.connect(self.menu)

        self.btn_list = QPushButton("List of words")
        self.btn_list.setStyleSheet("background-color: blue; color: black")

        self.btn_search = QPushButton("Search")
        self.btn_search.setStyleSheet("background-color: blue; color: black")


        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.btn_menu)
        self.hbox.addWidget(self.btn_list)
        self.hbox.addWidget(self.btn_search)

        self.vbox.addWidget(self.table)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

        row = 0


    #for orqali database degi ma'lumotlani ekranga chiqarish
        for _,eng,uzb in words:
            self.table.setItem(row, 0, QTableWidgetItem(eng))
            self.table.setItem(row, 1, QTableWidgetItem(uzb))
            row +=1



app = QApplication([])
win = Words_list()
app.exec_()


