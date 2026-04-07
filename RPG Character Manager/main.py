# WH, SW, JQ, BH 2nd
#imports
from classes import *
from menu_response_functions import *
#charcters list, where all characters are stored
characters = []
#races and classes setup
races = {
    "Human": (1,1,1,1,1,1),
    "Aquatic": (1,2,5,6,3,1),
    "Avian": (2,3,6,74,8,69)
    
}
classes = {
    "wizard": (1,1,1,1,1,1),
    "rogue": (1,1,1,1,1,1),
    "fighter": (1,1,1,1,1,1),
}
#MAIN MENU
def main_menu():
    while True:
        match input("Do you want to (as a number).\n1: Create a character \n2: Edit a character \n3: Compare characters \n4: View characters \n5: Attribute display \n6. Exit\n").strip():
            case "1":
                handle_create_character(races,classes,characters)
            case "2":
                handle_edit_character(characters)
            case "3":
                handle_compare_characters(characters)
            case "4":
                handle_view_characters(characters)
            case "5":
                handle_attribute_display(characters)
            case "6":
                break
            case _:
                print("Not an input.")
main_menu()
