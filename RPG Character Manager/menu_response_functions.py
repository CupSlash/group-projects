#BH 2nd menu_response_functions.py
import math as m
from skills_lvs import *
from classes import *
from perfun import *

def handle_create_character(races, classes ,characters = dict,skills = dict):
    random_generator = RandomGenerator()
    character_name = input("What is the new character's name? Or press r for random.\n")
    new_character = dict()
    if character_name.strip().lower() == "r":
        character_name = random_generator.create_name()
    new_character["name"] = character_name
    new_character["race"] = modifier_selector("race",races)
    new_character["class"] = modifier_selector("class",classes)
    while True:
        new_character["level"] = m.floor(help_isint_input(f"What is {character_name}'s level (1-20)? \n"))
        if new_character["level"] > 0 and new_character["level"] <= 20:
            break
        else:
            print("Too big or small.")
    text = ["strength","dexterity","wisdom","charisma","intelligence","constitution"]
    for item in text:
        new_character[item] = help_isint_input(f"What is {character_name}'s {item}?\n")
    characters[character_name] = new_character
    new_character["skills"] = edit_skills(set(),new_character["class"],new_character["level"])
    new_character["backstory"] = random_generator.create_backstory(character_name)
    new_character["side_quest"] = random_generator.create_side_quest()
    new_character["equipment"] = random_generator.create_equipment()
    return characters

def handle_edit_character(characters):
    while True:
        if characters == {}:
            print("no characters.")
            break
        else:
            while True:
                new_character_list =print_numbered_characters(characters)
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

def handle_compare_characters(characters):
    if len(characters) < 2:
        print("Not enough characters to compare. Please create more characters first.")
        return None, None
    print_numbered_characters(characters)
    character1 = input(f"Select your first character.\n")
    while character1 not in characters:
        print("Try again. That character doesn't exit yet. :")
        character1 = input(f"Select your first character.\n")
    print_numbered_characters(characters)       
    character2 = input(f"Select your second character.\n")
    while character2 not in characters:
        print("Try again. That character doesn't exit yet. :")
        character2 = input(f"Select your second character.\n")
    visualization = DataVisualization()
    visualization.display_character_comparison(character1, character2)

def handle_search_characters(characters):
    stat_to_search_by = input("What stat would you like to search by, race, class, level, str, dex, cha, int, or name?\n").strip().lower()
    if stat_to_search_by == "race":
        search_race = input("What is their race?\n").strip()
        print(f"{characters.get(search_race)}")
    elif stat_to_search_by == "class":
        search_class= input("What is their class?\n").strip()
        print(f"{characters.get(search_class)}")
    elif stat_to_search_by == "level":
        search_level_str= input("What is their level?\n").strip()
        for i in range(20):
            search_level_var == 0
            if search_level_str == i:
                search_level_var = i
                print(f"{characters[search_level_var]}")
                break
            else:
                search_level_var += 1
            print("No characters found.")
    elif stat_to_search_by == "str":
        search_str = input("What is their strength?\n").strip()
        if (f"{characters[search_str]}") == False:
            print("No characters found.")
        else:
            print(f"{characters[search_str]}")
    elif stat_to_search_by == "dex":
        search_dex = input("What is their dexterity?\n").strip()
        if (f"{characters[{search_dex}]}") == False:
            print("No characters found.")
        else:
            print(f"{characters[search_dex]}")
    elif stat_to_search_by == "cha":
        search_cha = input("What is their charisma?\n").strip()
        if (f"{characters[search_cha]}") == False:
            print("No characters found.")
        else:
            print(f"{characters[search_cha]}")
    elif stat_to_search_by == "int":
        search_int = input("What is their intelligence?\n").strip()
        if (f"{characters[search_int]}") == False:
            print("No characters found.")
        else:
            print(f"{characters[search_int]}")
    elif stat_to_search_by == "name":
        search_name = input("What is their name?\n").strip()
        print(f"{characters.get(search_name)}")
    else:
         print("That isn't a stat.")

def handle_display_character_stats():
    character = {
        "name": "Test Character",
        "strength": 100,
        "dexterity": 80,
        "wisdom": 120,
        "charisma": 90,
        "intelligence": 110,
        "constitution": 95
    }
    visualization = DataVisualization()
    visualization.display_character_stats(character)

def help_isint_input(text):
    while True:
        want = input(text)
        try:
            return int(want)
        except:
            try:
                return float(want)
            except:
                print("Not a number.")
def modifier_selector(text, modifer_list):
    while True:

        while True:
            print(f"what {text} do you want?")
            count = 0
            list_to_modifer = list()
            for class_race in modifer_list.keys():
                list_to_modifer.append(class_race)
                count += 1
                print(f"{count}: {class_race}")
            want = input()

            try:
                class_race = modifer_list[want.strip()]
                class_race = want
                break
            except:
                try:
                    want = int(want)
                    if want > 0:
                        class_race = modifer_list[list_to_modifer[want-1]]
                        class_race = list_to_modifer[int(want)-1]
                        break
                    else:
                        print("Not an option.")

                except:
                    print("Not an option.")
        stats = modifer_list[class_race]
        stats_text = ["strength","dexterity","wisdom","charisma","intelligence","constitution"]
        print("Do you want:")
        for item in range(6):
            c_stat = stats[item]
            c_text = stats_text[item]
            if c_stat > 0:
                print(f"+{c_stat}: {c_text}")
            else:
                print(f"{c_stat}: {c_text}")
        while True:
            want = input("(1: yes/ 2: no)\n").strip()
            if want == "1" or want == "yes":
                return class_race
            elif want == "2" or want == "no":
                break
            else:
                print("not an option.")

def print_numbered_characters(characters):
    count = 0
    new_character_list = []
    for text in characters.keys():
        count += 1
        new_character_list.append(text)
        print(f"{count}: {text}")
    return new_character_list