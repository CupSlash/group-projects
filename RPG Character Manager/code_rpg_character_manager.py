# WH, SW, JQ, BH 2nd
#Matplotlib
#Pandas
#Faker
from will_code_rpg import character_creator
from compare_and_search import compare
from compare_and_search import search_char
from skills_lvs import edit_skills
from skills_lvs import edit_level
from perfun import choice
import sys
import time as t 
        
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
        1: {"stealth", "thieves’ tools"},  
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
        match input("Do you want to (as a number).\n1: Make a character \n2: Edit a character \n3: Compare a character \n4: Search for a character \n5: Exit\n").strip():
            case "1":
                character_creator(races,classes,characters,skills_library)
            case "2":
                ediding_menu()
            case "3":
                compare(characters)
            case "4":
                search_char(characters)
            case "5":
                break
            case _:
                print("not a input.")

def ediding_menu():
    while True:
        if characters == {}:
            print("no characters.")
            break
        else:
            while True:
                count = 0
                new_character_list = []
                for text in characters.keys():
                    count += 1
                    new_character_list.append(text)
                    print(f"{count}: {text}")
                want = input("what character do you want?\n")
                try:
                    characters[want]
                    character = want
                    break
                except:
                    try:
                        want = int(want)
                        if want > 0:
                            characters[new_character_list[want]]
                            character = new_character_list[want]
                            break
                    except:
                        print("not a character.")
            match input("Do you want to (as a number).\n1: Edit Character Inventory \n2: Edit character Level \n3: Edit character Skills \n4: Exit\n").strip():
                case "1":
                    choice(character)
                    pass
                case "2":
                    edit_level(character["level"],character["dexterity"],character["constitution"],character["intelligence"],character["charisma"],character["strength"],character["wisdom"])
                    pass
                case "3":
                    edit_skills(character["current_skills"],character["class"],character["level"])
                    pass
                case "4":
                    break
                case _:
                    print("not a input.")
main_menu()
