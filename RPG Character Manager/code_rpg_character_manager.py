# WH, SW, JQ, BH 2nd
from classes import *
from menu_response_functions import *

characters = []

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

def main_menu():
    while True:
        match input("Do you want to (as a number).\n1: Make a character \n2: Edit a character \n3: Compare characters \n4: Search for a character \n5: Display Character Stats \n6: Display Character Progression \n7: View Statistical Analysis \n8. Exit\n").strip():
            case "1":
                handle_create_character(races,classes,characters)
            case "2":
                handle_edit_character(characters)
            case "3":
                handle_compare_characters(characters)
            case "4":
                handle_search_characters(characters)
            case "5":
                handle_display_character_stats(characters)
            case "6":
                handle_display_character_progression(characters)
            case "7":
                handle_statistical_analysis(characters)
            case "8":
                break
            case _:
                print("not a input.")
main_menu()
