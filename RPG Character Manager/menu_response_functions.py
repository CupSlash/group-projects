#BH 2nd menu_response_functions.py
import math as m

from numpy import character
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
    add_attributes(new_character, character_name)
    new_character["skills"] = edit_skills(set(),new_character["class"],new_character["level"])
    new_character["backstory"] = random_generator.create_backstory(character_name)
    new_character["side_quest"] = random_generator.create_side_quest()
    new_character["equipment"] = random_generator.create_equipment()
    new_character["level_history"] = []
    print(f"{new_character['backstory']}\nSide quest: {new_character['side_quest']}\nEquipment:{new_character['equipment']}")
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
                    edit_skills(character["skills"],character["class"],character["level"])
                    break
                case "4":
                    break
                case _:
                    print("not a input.")

def handle_compare_characters(characters):
    if len(characters) < 2:
        print("Not enough characters to compare. Please create more characters first.")
        return None, None
    character1 = select_a_character(characters, "Select your first character.\n")
    character2 = select_a_character(characters, "Select your second character.\n")
    visualization = DataVisualization()
    visualization.display_character_comparison(character1, character2)

def handle_view_characters(characters):
    if len(characters) == 0:
        print("No characters to view. Please create a character first.")
        return
    choice = input("Do you want to (as a number).\n1: View all characters \n2: Filter characters \n3: Sort characters \n4: Exit\n").strip()
    if choice == "1":
        for character in characters:
            print(f"Name: {character['name']}, Class: {character['class']}, Race: {character['race']}, Strength: {character['strength']}, Dexterity: {character['dexterity']}, Wisdom: {character['wisdom']}, Charisma: {character['charisma']}, Intelligence: {character['intelligence']}, Constitution: {character['constitution']}")
    elif choice == "2":
        handle_filter_characters(characters)
    elif choice == "3":
        handle_sort_characters(characters)
    elif choice == "4":
        return
    else:
        print("Not a choice.")

def handle_filter_characters(characters):
    stat_to_filter_by = input("What stat would you like to filter by: race, class, str, dex, wis, cha, int, con, or name?\n").strip().lower()
    if stat_to_filter_by == "race":
        search_race = input("What is their race?\n").strip()
        filtered_characters = filter(lambda char: char["race"] == search_race, characters)
    elif stat_to_filter_by == "class":
        search_class= input("What is their class?\n").strip()
        filtered_characters = filter(lambda char: char["class"] == search_class, characters)
    elif stat_to_filter_by == "str":
        search_str = input("What is their strength?\n").strip()
        filtered_characters = filter(lambda char: char["strength"] == int(search_str), characters)
    elif stat_to_filter_by == "dex":
        search_dex = input("What is their dexterity?\n").strip()
        filtered_characters = filter(lambda char: char["dexterity"] == int(search_dex), characters)
    elif stat_to_filter_by == "wis":
        search_wis = input("What is their wisdom?\n").strip()
        filtered_characters = filter(lambda char: char["wisdom"] == int(search_wis), characters)
    elif stat_to_filter_by == "cha":
        search_cha = input("What is their charisma?\n").strip()
        filtered_characters = filter(lambda char: char["charisma"] == int(search_cha), characters)
    elif stat_to_filter_by == "int":
        search_int = input("What is their intelligence?\n").strip()
        filtered_characters = filter(lambda char: char["intelligence"] == int(search_int), characters)
    elif stat_to_filter_by == "con":
        search_con = input("What is their constitution?\n").strip()
        filtered_characters = filter(lambda char: char["constitution"] == int(search_con), characters)
    elif stat_to_filter_by == "name":
        search_name = input("What is their name?\n").strip()
        filtered_characters = filter(lambda char: char["name"] == search_name, characters)
    else:
         print("That isn't a stat.")

    if (filtered_characters and len(list(filtered_characters)) > 0):
        for character in filtered_characters:
            print(f"Name: {character['name']}, Class: {character['class']}, Race: {character['race']}, Strength: {character['strength']}, Dexterity: {character['dexterity']}, Wisdom: {character['wisdom']}, Charisma: {character['charisma']}, Intelligence: {character['intelligence']}, Constitution: {character['constitution']}")
    else:
        print("No characters found.")

def handle_sort_characters(characters):
    stat_to_sort_by = input("What stat would you like to sort by: race, class, strength, dexterity, wisdom, charisma, intelligence, constitution, or name?\n").strip().lower()
    if stat_to_sort_by not in ["race", "class", "strength", "dexterity", "wisdom", "charisma", "intelligence", "constitution", "name"]:
        print("That isn't a stat.")
        return
    sorted_characters = sorted(characters, key=lambda char: char[stat_to_sort_by])
    for character in sorted_characters:
        print(f"Name: {character['name']}, Class: {character['class']}, Race: {character['race']}, Strength: {character['strength']}, Dexterity: {character['dexterity']}, Wisdom: {character['wisdom']}, Charisma: {character['charisma']}, Intelligence: {character['intelligence']}, Constitution: {character['constitution']}")

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
        return class_race

def add_attributes(new_character, character_name):
    attributes = ["strength","dexterity","wisdom","charisma","intelligence","constitution"]
    choice = input("Which attribute template would you like to use?\n 1. Medic\n 2. Heavy \n 3. Long-range \n 4. Scientist \n 5. Rizzler \n 6. Balanced \n 7. Custom\n")
    if choice == "1":
        new_character["strength"] = 8
        new_character["dexterity"] = 10
        new_character["wisdom"] = 13
        new_character["charisma"] = 16
        new_character["intelligence"] = 15
        new_character["constitution"] = 38
    elif choice == "2":
        new_character["strength"] = 40
        new_character["dexterity"] = 9
        new_character["wisdom"] = 4
        new_character["charisma"] = 10
        new_character["intelligence"] = 3
        new_character["constitution"] = 30
    elif choice == "3":
        new_character["strength"] = 10
        new_character["dexterity"] = 40
        new_character["wisdom"] = 15
        new_character["charisma"] = 0
        new_character["intelligence"] = 20
        new_character["constitution"] = 5
    elif choice == "4":
        new_character["strength"] = 3
        new_character["dexterity"] = 10
        new_character["wisdom"] = 20
        new_character["charisma"] = 3
        new_character["intelligence"] = 40
        new_character["constitution"] = 6
    elif choice == "5":
        new_character["strength"] = 4
        new_character["dexterity"] = 19
        new_character["wisdom"] = 3
        new_character["charisma"] = 41
        new_character["intelligence"] = 4
        new_character["constitution"] = 12
    elif choice == "6":
        new_character["strength"] = 15
        new_character["dexterity"] = 15
        new_character["wisdom"] = 15
        new_character["charisma"] = 15
        new_character["intelligence"] = 15
        new_character["constitution"] = 15
    elif choice == "7":
        for attribute in attributes:
            new_character[attribute] = help_isint_input(f"What is {character_name}'s {attribute}?\n")
    else:
        print("Not a choice. Defaulting to balanced.")
        new_character["strength"] = 15
        new_character["dexterity"] = 15
        new_character["wisdom"] = 15
        new_character["charisma"] = 15
        new_character["intelligence"] = 15
        new_character["constitution"] = 15
    for attribute in attributes:
        new_character[f"{attribute}_history"] = []

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