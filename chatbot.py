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
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/librarian.png"))
            response = f"Hello {screen_manager.get_screen('chats').bot_name.text}, I am Lucy your Personal Assistant for today. How can I help you?\n\n1. Project Biblioteca\n2. Book Genres\n3. Application Services\n4. The Developers\n\n Type 'help' for more information."
        elif value == "Menu" or value == "menu" or value == "Main" or value == "main" or value == "back"or value == "Back":
            response = "--- MAIN MENU ---\n\n1. Project Biblioteca\n2. Book Genres\n3. Application Services\n4. The Developers\n\n Type 'help' for more information."


        # Menu Navigation
        elif value == "Biblioteca" or value == "biblioteca" or value == "app" or value == "App" or value =='1':
            response = "Biblioteca is an online library system that allows their users to browse books from their catalouge and borrow those books to read them in the comfort of their homes, Users would be able access different fictional, non-fictional, and academic books in one single app. \n\nBiblioteca is also equipped with a chatbot to help entertain any questions or concerns of the users, That chatbot is the one you're currently using!! Chatbot is more than willing to hear any questions that you have.\n\nType 'help' for more information."
        elif value == "Books" or value == "books" or value == "book" or value == "Book" or value == "Genre" or value == "genre" or value == "Book genre" or value == '2':
            response ="Lucy: The genres available in this app are:\n\n Fiction\n Non Fiction\n Academic\n\nType 'help' for more information."
        elif value == "Service" or value == "service" or value == "services" or value == "Services" or value == '3':
            response ="This application provides the following:\n\n1. This application provides list of books available in the Bibilioteca mobile application that you can borrow in the Biblioteca Library System.\n\n2. The application provides the title, date published, and author of the book that you want to borrow.\n\n3. It provides ...\n\n\nType 'help' for more information."
        elif value == "Developers" or value == "developers" or value == "Devs" or value == "devs" or value =='4':
            response ="--- DEVELOPERS ---\n\n1. Florencio, Daniel\n2. Herrera, Mikaela\n3. Medrano, Yvette\n4. Noprada, Shane\n5. Revilla, Aarone\n\n Type 'help' for more information."
        elif value == "Help" or value == "help" or value == "info" or value == "Info":
            response = "Lucy: These are the keywords that you can use to navigate the app.\n\nacademic - academic books\nbiblioteca - project information\nbooks - list of books\ndevs - the developers\nfiction - fictional books\nnon fiction - non fictional books\n\n Type 'help' for more information."
        # Optional
        elif value == "best" or value == "Best" or value == "top" or value == "Top":
            #screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/best/bestFiveBooks.png"))
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/best/Sadako and the Thousand Paper Cranes.png"))
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/best/House of Furies by Madeleine Roux.png"))
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/best/Alone With You in the Ether by Olivia Blake.png"))
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/best/A Gentle Reminder by Bianca.png"))
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/best/A Walk to Remember by Nicholas Sparks.png"))
            response ="--- TOP 5 BOOKS ---\n\n1. Sadako and the Thousand Paper Cranes by Eleanor Coerr\n2. House of Furies by Madeleine Roux\
            \n3. Alone With You in the Ether by Olivia Blake\n4. A Gentle Reminder by Bianca Sparacino\
            \n5.  A Walk to Remember by Nicholas Sparks\n\n Type 'help' for more information."
        # All of the books
        elif value == "list" or value == "List" or value == "all" or value == "All"or value == "Directory"or value == "directory" or value == "List of Books" or value == "list of books":
            response ="--- LIST OF BOOKS ---\n\n•A Brief History of Time\n•A Gentle Reminder\n•A Room of One’s Own \
            \n•A Walk to Remember\n•Alone With You in the Ether\n•Atomic Habits\n•Beyond Good and Evil\n•Cry of the Kalahari\
            \n•Dune\n•Educated\n•Emma\n•Fahrenheit 451\n•Fifty Shades of Grey\n•Game of Thrones\
            \n•Harry Potter and the Deathly Hallows\n•House of Furies\n•How to Write a Lot\n•Introduction to Academic Writing\
            \n•Me Before You\n•On the Origins of Species\n•Pride and Prejudice\n•Queen of Our Times\
            \n• Quiet: The Power of Introverts in a World that Can’t Stop Talking\n•Sadako and the Thousand Paper Cranes\
            \n•Scary Smart\n•Sea of tranquility\n•Song of Achilles\n•The Book of Minds\n•The Colour of Madness\
            \n•The Communist Manifesto\n•The Diary of a Young Girl\n•The Fault in Our Stars\n•The Golden Compass\
            \n•The Great Gatsby\n•The Lion, the Witch and the wardrobe\n•The Lord of the Rings\n•The Meaning of Relativity\
            \n•The Notebook\n•The Reluctant Career\n•The Secret Wisdom of the Earth\n•The Shakespeare Requirement\
            \n•The Uses of Literacy\n•Where the Crawdads Sing\n•Writing for Social Scientists\n\n Type 'help' for more information."
            # Course description
        elif value == "Intelligent agents" or value == "intelligent agents" or value == "course" or value == "Course":
            response ="  --- FINAL PROJECT ---\n           GROUP 5\n CS 403 - CS31S1\n Intelligent Agents\n\n Submitted to: Ms. Lorna C. Lim\n\n\n Type 'menu' to go to the main menu."

        elif value == "Stop" or value == "stop" or value == "done" or value == "Done" or value =='out'or value =='Out':
            response = "Lucy: Thank you for using our application."
           
            # Fictional books (All)
        elif value == "Fiction" or value == "fiction":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/img_cat/bg.png"))
            response = "FICTIONAL\n\n1. Harry Potter and the Deathly Hallows\n2. Game of Thrones\n3. Fifty Shades of Grey\
            \n4. Me Before You\n5. Pride and Prejudice\n6. Sea of Tranquility\n7. The Fault in Our Stars\n8. The Lord of the Rings\
            \n9. The Notebook\n10. To Paradise " 

           
            # Non-Fictional books (All)
        elif value == "Non-Fiction" or value == "non-fiction" or value == "non fiction" or value == "Non fiction" or value == "not fiction" or value == "Not fiction":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/img_cat/bg.png"))
            response = "1. The Reluctant Carer\n2. Queen of Our Times\n3. The Book of Minds\n4. The Colour of Madness\n5. Scary Smart\n6. The Diary of a Young Girl\n7. Quiet\n8. A Room of One's Own\n9. Atomic Habits\n10. Educated"
           
            # Academic books (All)
        elif value == "Academic" or value == "academic" or value == "acad" or value == "Acad" or value == "educational" or value == "Educational":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/img_cat/bg.png"))
            response = "1. A Brief History of Time\n2. On the Origins of Species 2\n3. The Uses of Literacy\n4. The Meaning of Relativity\n5. How to Write a Lot\n6. Writing for Social Scientists\n7. Introduction to Academic Writing, Third Edition \n8. The Shakespeare Requirement: A Novel \n9. The Communist Manifesto \n10. Beyond Good and Evil "
               
        # FICTION
        elif value == "Sea of Tranquility" or value == "sea of tranquility":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/SoT.png"))
            response = " Book Title: Sea of Tranquility\n Author: Emily St. John Mandel\n Published: April 5, 2022"

        elif value == "Game of Thrones" or value == "game of thrones" or value == "a game of thrones" or value == "A Game of Thrones":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/AGoT.png"))
            response = " Book Title: A Game of Thrones\n Author: George R.R. Martin\n Published: August 1, 1996"

        elif value == "Fifty Shades of Grey" or value == "fifty shades of grey" or value == "50 shades of grey" or value == "50 Shades of Grey" or value == "50 Shades" or value == "50 shades":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/FSG.png"))
            response = " Book Title: Fifty Shades of Grey\n Author: E. L. James\n Published: June 20, 2011"

        elif value == "To Paradise" or value == "to paradise":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/TP.png"))
            response = " Book Title: To Paradise\n Author: Hanya Yanagihara\n Published: January 11, 2022"

        elif value == "Pride and Prejudice" or value == "pride and prejudice":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/PaP.png"))
            response = " Book Title: Pride and Prejudice\n Author: Jane Austin\n Published: January 28, 1813"

        elif value == "The Lord of the Rings" or value == "the lord of the rings" or value == "lord of the rings" or value == "Lord of the Rings" or value == "The Lord of the Ring" or value == "the lord of the ring" or value == "lord of the ring" or value == "Lord of the Ring":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/LOR.png"))
            response = " Book Title: The Lord of the Rings\n Author: J. R. R. Tolkien\n Published: July 26, 1954"

        elif value == "Harry Potter and the Deathly Hallows" or value == "harry potter and the deathly hallows" or value == "harry potter" or value == "Harry Potter" or value == "deathly hallows" or value == "Deathly Hallows":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/HPDH.png"))
            response = " Book Title: Harry Potter and the Deathly Hallows\n Author: J.K. Rowling\n Published: July 21, 2007"

        elif value == "The Notebook" or value == "the notebook" or value == "notebook" or value == "Notebook":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/TN.png"))
            response = " Book Title: The Notebook\n Author: Nicholas Sparks\n Published: October 1, 1996"

        elif value == "The Fault in Our Stars" or value == "the fault in our stars" or value == "Fault in Our Stars" or value == "fault in our stars":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/TFIOS.png"))
            response = " Book Title: The Fault in Our Stars\n Author: John Green\n Published: January 10, 2012"

        elif value == "Me Before You" or value == "me before you":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/fiction/MBY.png"))
            response = " Book Title: Me Before You\n Author: Jojo Moyes\n Published: January 5, 2012"

        # NON - FICTION
        # possible keyword
        elif value == "The Reluctant Carer" or value == "the reluctant carer" or value == "Reluctant Carer" or value == "reluctant carer":
            # edit image location
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/reluctant_carer.png"))

            response = " Book Title: The Reluctant Carer: Dispatches from the Edge of Life\n Author: Chris Haughton\n Published: June 2022 "

        elif value == "Queen of Our Times" or value == "queen of our times" or value == "queen of our time" or value == "Queen of Our Time":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/queen_of_our_times.png"))
            response = " Book Title: Queen of Our Times The Life of Queen Elizabeth II\n Author: Robert Hardman\n Published: March 2022"

        elif value == "The Book of Minds" or value == "Book of Minds" or value == "book of minds" or value == "Book of Minds":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/book_of_minds.png"))
            response = " Book Title: The Book of Minds: How to Understand Ourselves and Other Beings, From Animals to Aliens\n Author: Philip Ball\n Published: June 2022"

        elif value == "Scary Smart" or value == "scary smart":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/scary_smart.png"))
            response = " Book Title: Scary Smart: The Future of Artificial Intelligence and How You Can Save Our World \n Author: Mo Gawdat\n Published: 2021"

        elif value == "The Diary of a Young Girl" or value == "the diary of a young girl" or value == "Diary of a Young Girl" or value == "diary of a young girl":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/diary_of_young_girl.png"))
            response = " Book Title: The Diary of a Young Girl\n Author: Anne Frank\n Published: June 25, 1947"

        elif value == "Quiet" or value == "quiet":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/quiet.png"))
            response = " Book Title: Quiet: The Power of Introverts in a World that Can't Stop Talking\n Author: Susan Cain\n Published: January 24, 2012"

        elif value == "A Room of One's Own" or value == "Room of One's Own" or value == "a room of one's own" or value == "room of one's own":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/room_of_ones_own.png"))
            response = " Book Title: A Room of One's Own\n Author: Virginia Woolf\n Published: September 1929"

        elif value == "Atomic Habits" or value == "atomic habits":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/atomic_habits.png"))
            response = " Book Title: Atomic Habits: An Easy & Proven Way to Build Good Habits & Break\n Author: James Clear\n Published: October 16, 2018"

        elif value == "Educated" or value == "educated":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/educated.png"))
            response = " Book Title: Educated\n Author: Tara Westover \n Published: February 18, 2018"

        elif value == "The Colour of Madness" or value == "the colour of madness" or value == "Colour of Madness" or value == "colour of madness":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/non_fiction/colour_of_madness.png"))
            response = " Book Title: The Colour of Madness: Exploring BAME mental health in the UK\n Author: Samara Linton \n Published: September 2018"

        # Academic

        elif value == "A Brief History of Time" or value == "brief history of time" or value == "history of time":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: A Brief History of Time\n Author: Stephen Hawking\n Published: September 1, 1998"

        elif value == "On the Origins of Species" or value == "the origins of species" or value == "origin of species":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: On the Origins of Species\n Author: Charles Darwin\n Published: November 24, 1859"

        elif value == "The Uses of Literacy" or value == "uses of literacy" or value == "literacy":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: The Uses of Literacy\n Author: Richard Hoggart\n Published: February 28, 1998"

        elif value == "The Meaning of Relativity" or value == "meaning of relativity" or value == "relativity":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: The Meaning of Relativity\n Author: Albert Einstein\n Published: July 1, 1997 "

        elif value == "How to Write a Lot" or value == "how to write a lot" or value == "write a lot" or value == "lot":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: How to Write a Lot\n Author:  Paul J. Silvia\n Published: March 27, 2009"

        elif value == "Writing for Social Scientists" or value == "writing for social scientists" or value == "social scientists" or value == "scientists":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: Writing for Social Scientists\n Author: Howard S. Becker, Pamela Richards \n Published: December 15, 2007"

        elif value == "Introduction to Academic Writing, Third Edition " or value == "introduction to academic writing" or value == "academic writing ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: Introduction to Academic Writing, Third Edition\n Author: Alice Oshima, Ann Hogue \n Published: January 1, 1983 "

        elif value == "The Shakespeare Requirement: A Novel " or value == "the shakespeare requirement" or value == "shakespeare":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: The Shakespeare Requirement: A Novel\n Author: Julie Schumacher \n Published: August 14, 2018 "

        elif value == "The Communist Manifesto " or value == "the communist manifesto " or value == "communist " or value == "manifesto ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title: The Communist Manifesto\n Author: Karl Marx\n Published: February 21, 1848"

        elif value == "Beyond Good and Evil " or value == "beyond good and evil " or value == "good " or value == "evil ":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="images/academic/MBY.png"))
            response = f" Book Title:Beyond Good and Evil\n Author: Friedrich Nietzsche \n Published: January 1, 1886 "

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