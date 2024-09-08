from menu import *
from add_new_word import*
from words_list import*
from search import*

class Main:
    def __init__(self) -> None:
        selected_button = Menu()
        self.check_button(selected_button)


    def check_button(self,button):

        if button == "add_word":
            self.add_new_word()
        elif button == "menu":
            self.menu()
        elif button == "list":
            self.show_List()

        elif button == "search":
            self.search()
    

    
    def menu(self):
        menu = Menu()
        self.check_button(menu)



    def add_new_word(self):
        add_word = Add_new_word()
        self.check_button(add_word)



    
    def show_List(self):
        lst = Words_list()
        self.check_button(lst)



    def search(self):
        s = Search()
        self.check_button(s)

        
        
       

win = Main()