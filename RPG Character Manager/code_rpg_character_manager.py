# WH, SW, JQ, BH 2nd
#Matplotlib
#Pandas
#Faker
from skills_lvs import edit_skills
from skills_lvs import edit_level
from perfun import choice
import sys
import time as t 
from classes import *
from menu_response_functions import *
        
skills_library = {  
    "wizard": {  
        1: {"arcana", "spellcasting"},  
        3: {"ritual casting"},  
        5: {"fireball"},  
        7: {"counterspell"},  
        10: {"teleport"},  
        15: {"meteor swarm"},  
        20: {"wish"}  
    },  
    "rogue": {  
        1: {"stealth", "thieves' tools"},  
        3: {"sneak attack"},  
        5: {"evasion"},  
        7: {"uncanny dodge"},  
        10: {"blindsense"},  
        15: {"slippery mind"},  
        20: {"stroke of luck"}  
    },  
    "fighter": {  
        1: {"athletics", "second wind"},  
        3: {"action surge"},  
        5: {"extra attack"},  
        7: {"indomitable"},  
        10: {"leadership"},  
        15: {"survivor"},  
        20: {"champion"}  
    }  
}  

characters = dict()

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

weapons={ #weapons that character has

}
inventory={ #items that player has

}
spells={ #spells and their descriptions

}

equipment={
    "hand_1":'',
    "hand_2":'',
    "armour":'',
}
def main_menu():
    while True:
        match input("Do you want to (as a number).\n1: Make a character \n2: Edit a character \n3: Compare a character \n4: Search for a character \n5: Display Character Stats \n6: Compare Characters \n7: Exit\n").strip():
            case "1":
                handle_create_character(races,classes,characters,skills_library)
            case "2":
                handle_edit_character(characters)
            case "3":
                handle_compare_characters(characters)
            case "4":
                handle_search_characters(characters)
            case "5":
                handle_display_character_stats()
            case "6":
                pass
            case "7":
                break
            case _:
                print("not a input.")
main_menu()
