#BH 2nd menu_response_functions.py
import math as m
from skills_lvs import *
from classes import *
from perfun import *

def handle_create_character(races, classes ,characters,skills = dict):
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
    attributes = ["strength","dexterity","wisdom","charisma","intelligence","constitution"]
    for attribute in attributes:
        new_character[attribute] = help_isint_input(f"What is {character_name}'s {attribute}?\n")
        new_character[f"{attribute}_history"] = []
    new_character["skills"] = edit_skills(set(),new_character["class"],new_character["level"])
    new_character["backstory"] = random_generator.create_backstory(character_name)
    new_character["side_quest"] = random_generator.create_side_quest()
    new_character["equipment"] = random_generator.create_equipment()
    new_character["level_history"] = []
    characters.append(new_character)

def handle_edit_character(characters):
    while True:
        if characters == []:
            print("no characters.")
            break
        else:
            character = select_a_character(characters, "Select a character to edit.\n")
            match input("Do you want to (as a number).\n1: Edit Character Inventory \n2: Edit character Level \n3: Edit character Skills \n4: Exit\n").strip():
                case "1":
                    choice(character)
                    break
                case "2":
                    edit_level(character)
                    break
                case "3":
                    edit_skills(character["current_skills"],character["class"],character["level"])
                    break
                case "4":
                    break
                case _:
                    print("not a input.")

def handle_compare_characters(characters):
    if len(characters) < 2:
        print("Not enough characters to compare. Please create more characters first.")
        return None, None
    print_numbered_characters(characters)
    character1 = select_a_character(characters, "Select your first character.\n")
    print_numbered_characters(characters)       
    character2 = select_a_character(characters, "Select your second character.\n")
    visualization = DataVisualization()
    visualization.display_character_comparison(character1, character2)

def handle_search_characters(characters):
    stat_to_search_by = input("What stat would you like to search by, race, class, str, dex, cha, int, or name?\n").strip().lower()
    if stat_to_search_by == "race":
        search_race = input("What is their race?\n").strip()
        filtered_characters = filter(lambda char: char["race"] == search_race, characters)
    elif stat_to_search_by == "class":
        search_class= input("What is their class?\n").strip()
        filtered_characters = filter(lambda char: char["class"] == search_class, characters)
    elif stat_to_search_by == "str":
        search_str = input("What is their strength?\n").strip()
        filtered_characters = filter(lambda char: char["strength"] == int(search_str), characters)
    elif stat_to_search_by == "dex":
        search_dex = input("What is their dexterity?\n").strip()
        filtered_characters = filter(lambda char: char["dexterity"] == int(search_dex), characters)
    elif stat_to_search_by == "cha":
        search_cha = input("What is their charisma?\n").strip()
        filtered_characters = filter(lambda char: char["charisma"] == int(search_cha), characters)
    elif stat_to_search_by == "int":
        search_int = input("What is their intelligence?\n").strip()
        filtered_characters = filter(lambda char: char["intelligence"] == int(search_int), characters)
    elif stat_to_search_by == "name":
        search_name = input("What is their name?\n").strip()
        filtered_characters = filter(lambda char: char["name"] == search_name, characters)
    else:
         print("That isn't a stat.")

    if (filtered_characters and len(list(filtered_characters)) > 0):
        for character in filtered_characters:
            print(f"{character['name']}\n")
    else:
        print("No characters found.")

def handle_display_character_stats(characters):
    if len(characters) == 0:
        print("No characters to display. Please create a character first.")
        return
    character = select_a_character(characters, "Select a character to display its stats.\n")
    visualization = DataVisualization()
    visualization.display_character_stats(character)

def handle_display_character_progression(characters):
    if len(characters) == 0:
        print("No characters to display. Please create a character first.")
        return
    character = select_a_character(characters, "Select a character to display its progression.\n")
    visualization = DataVisualization()
    visualization.display_character_progression(character)

def handle_statistical_analysis(characters):
    if len(characters) == 0:
        print("No characters to analyze. Please create a character first.")
        return
    analyzer = StatisticalAnalyzer()
    statistics = analyzer.calculate_statistics(characters)
    for key, value in statistics.items():
        print(f"{key}: mean={round(value['mean'], 2)}, median={value['median']}, max={value['max']}, min={value['min']}")
        
def handle_level_up_character(characters):
    if len(characters) == 0:
        print("No characters to level up. Please create a character first.")
        return
    selected_character = select_a_character(characters, "Select a character to level up.\n")
    # edit_level(selected_character["level"],selected_character["dexterity"],selected_character["constitution"],selected_character["intelligence"],selected_character["charisma"],selected_character["strength"],selected_character["wisdom"])
    # edit_skills(selected_character["current_skills"],selected_character["class"],selected_character["level"])

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

def select_a_character(characters, prompt):
    while True:
        print_numbered_characters(characters)
        selected_character_input = input(prompt)
        if selected_character_input.isdigit() and int(selected_character_input) > 0 and int(selected_character_input) <= len(characters):
            return characters[int(selected_character_input)-1]
        else:
            print("Invalid input.")

def print_numbered_characters(characters):
    for i, character in enumerate(characters):
        print(f"{i+1}: {character['name']}")