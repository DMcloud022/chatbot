from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.image import Image
from kivy.core.text import LabelBase
from kivy.clock import Clock
Window.size = (350, 550)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 15

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 14

class ResponseImage(Image):
    source = StringProperty()

class ChatBot(MDApp):
    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text !="":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"


    def response(self, *args):
        response =""
        if value == "Hello" or value == "hello" or value == "start" or value == "Start" or value == "hi"or value == "Hi":
            response = f"Hello {screen_manager.get_screen('chats').bot_name.text}, I am Lucy your Personal Assistant for today. How can I help you?\n\n1. Project Biblioteca\n2. Book Genres\n3. Application Services\n4. The Developers\n\n Type 'help' for more information."
        elif value == "Menu" or value == "menu" or value == "Main" or value == "main" or value == "back"or value == "Back":
            response = "--- MAIN MENU ---\n\n1. Project Biblioteca\n2. Book Genres\n3. Application Services\n4. The Developers\n\n Type 'help' for more information."


        # Menu Navigation
        elif value == "Biblioteca" or value == "biblioteca" or value == "app" or value == "App" or value =='1':
            response = "Biblioteca is a library system that can help you access different fictional and non-fictional books in one single app.\n\n Type 'help' for more information."
        elif value == "Books" or value == "books" or value == "book" or value == "Book" or value == "Genre" or value == "genre" or value == "Book genre" or value == '2':
            response ="Lucy: The genres available in this app are:\n\n Fiction\n Non Fiction\n Academic"
        elif value == "Service" or value == "service" or value == "services" or value == "Services" or value == '3':
            response ="This application provides the following:\n\n1. This application provides list of books available in the Bibilioteca mobile application that you can borrow.\n2. It provides ... \n3. It provides ...\n\n Type 'help' for more information."
        elif value == "Developers" or value == "developers" or value == "Devs" or value == "devs" or value =='4':
            response ="--- DEVELOPERS ---\n\n1. Florencio, Daniel\n2. Herrera, Mikaela\n3. Medrano, Yvette\n4. Noprada, Shane\n5. Revilla, Aarone\n\n Type 'help' for more information."
        elif value == "Help" or value == "help" or value == "info" or value == "Info":
            response = "Lucy: These are the keywords that you can use to navigate the app.\n\nbiblioteca - project information\ndevs - the developers\nbooks - list of books\nfiction - fictional books"
        # Optional
        elif value == "best" or value == "Best" or value == "top" or value == "Top":
            response ="--- TOP 5 BOOKS ---\n\n1. Book Title\n2. Book Title\n3. Book Title\n4. Book Title\n5. Book Title\n\n Type 'help' for more information."
        # All of the books
        elif value == "list" or value == "List" or value == "all" or value == "All"or value == "Directory"or value == "directory" or value == "List of Books" or value == "list of books":
            response ="--- LIST OF BOOKS ---\n\n1. Book Title\n2. Book Title\n3. Book Title\n4. Book Title\n5. Book Title\n\n Type 'help' for more information."
            # Course description
        elif value == "Intelligent agents" or value == "intelligent agents" or value == "course" or value == "Course":
            response ="  --- FINAL PROJECT ---\n           GROUP 5\n CS 403 - CS31S1\n Intelligent Agents\n\n Submitted to: Ms. Lorna C. Lim\n\n\n Type 'menu' to go to the main menu."

        elif value == "Stop" or value == "stop" or value == "done" or value == "Done" or value =='out'or value =='Out':
            response = "Lucy: Thank you for using our application."
            # Fictional books (All)
        elif value == "Fiction" or value == "fiction":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/img_cat/bg.png"))
            response = "FICTIONAL\n\n1. Sea of Tranquility\n2. Game of Thrones\n3. Fifty Shades of Grey"
            # Non-Fictional books (All)
        elif value == "Non-Fiction" or value == "non-fiction" or value == "non fiction" or value == "Non fiction" or value == "not fiction" or value == "Not fiction":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/img_cat/bg.png"))
            response = "1. Book 1\n2. Book 2\n3. Book 3"
            # Academic books (All)
        elif value == "Academic" or value == "academic" or value == "acad" or value == "Acad" or value == "educational" or value == "Educational":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/img_cat/bg.png"))
            response = "1. Book 1\n2. Book 2\n3. Book 3"

        # FICTION

        elif value == "Sea of Tranquility" or value == "sea of tranquility":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/SoT.png"))
            response = f" Book Title: Sea of Tranquility\n Author: Emily St. John Mandel\n Published: April 5, 2022"

        elif value == "Game of Thrones" or value == "game of thrones" or value == "a game of thrones" or value == "A Game of Thrones":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/AGoT.png"))
            response = f" Book Title: A Game of Thrones\n Author: George R.R. Martin\n Published: August 1, 1996"

        elif value == "Fifty Shades of Grey" or value == "fifty shades of grey" or value == "50 shades of grey" or value == "50 Shades of Grey" or value == "50 Shades" or value == "50 shades":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/FSG.png"))
            response = f" Book Title: Fifty Shades of Grey\n Author: E. L. James\n Published: June 20, 2011"

        elif value == "To Paradise" or value == "to paradise":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/TP.png"))
            response = f" Book Title: To Paradise\n Author: Hanya Yanagihara\n Published: January 11, 2022"

        elif value == "Pride and Prejudice" or value == "pride and prejudice":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/PaP.png"))
            response = f" Book Title: Pride and Prejudice\n Author: Jane Austin\n Published: January 28, 1813"

        elif value == "The Lord of the Rings" or value == "the lord of the rings" or value == "lord of the rings" or value == "Lord of the Rings" or value == "The Lord of the Ring" or value == "the lord of the ring" or value == "lord of the ring" or value == "Lord of the Ring":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/LOR.png"))
            response = f" Book Title: The Lord of the Rings\n Author: J. R. R. Tolkien\n Published: July 26, 1954"

        elif value == "Harry Potter and the Deathly Hallows" or value == "harry potter and the deathly hallows" or value == "harry potter" or value == "Harry Potter" or value == "deathly hallows" or value == "Deathly Hallows":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/HPDH.png"))
            response = f" Book Title: Harry Potter and the Deathly Hallows\n Author: J.K. Rowling\n Published: July 21, 2007"

        elif value == "The Notebook" or value == "the notebook" or value == "notebook" or value == "Notebook":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/TN.png"))
            response = f" Book Title: The Notebook\n Author: Nicholas Sparks\n Published: October 1, 1996"

        elif value == "The Fault in Our Stars" or value == "the fault in our stars" or value == "Fault in Our Stars" or value == "fault in our stars":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/TFIOS.png"))
            response = f" Book Title: The Fault in Our Stars\n Author: John Green\n Published: January 10, 2012"

        elif value == "Me Before You" or value == "me before you":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/MBY.png"))
            response = f" Book Title: Me Before You\n Author: Jojo Moyes\n Published: January 5, 2012"

        # NON - FICTION
        # possible keyword
        elif value == "" or value == "" or value == "" or value == " " or value == " ":
            # edit image location
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))

            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        # Academic

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        elif value == " " or value == " " or value == " " or value == " ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: \n Author: \n Published: "

        else:
            response = "Sorry could you say that again?"
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=.75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""

if __name__ == '__main__':
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()