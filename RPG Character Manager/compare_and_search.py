#BH 2nd RPG character manager
# COMPARE
def compare(characters):
    compare_first_character = input(f"{characters}, Select your first character.\n")
    while compare_first_character not in characters:
        print("Try again. That character doesn't exit yet. :")
        compare_first_character = input(f"{characters}, Select your first character.\n")       
    compare_second_character = input(characters, "Select your second character.\n")
    while compare_second_character not in characters:
        print("Try again. That character doesn't exit yet. :")
        compare_second_character = input(f"{characters}, Select your first character.\n")  



# SEARCH
def search():
    stat_to_search_by = input("What stat would you like to search by, race, class, level, str, dex, cha, int, or name?\n").strip().lower()
    if stat_to_search_by == "race":
        search_race = input("What is their race?\n").strip()
    elif stat_to_search_by == "class":
        search_class= input("What is their class?\n").strip()
    elif stat_to_search_by == "level":
        search_level= input("What is their level?\n").strip()
    elif stat_to_search_by == "str":
        search_str = input("What is their strength?\n").strip()
    elif stat_to_search_by == "dex":
        search_dex = input("What is their dexterity?\n").strip()
    elif stat_to_search_by == "cha":
        search_cha = input("What is their charisma?\n").strip()
    elif stat_to_search_by == "int":
        search_int = input("What is their intelligence?\n").strip()
    elif stat_to_search_by == "name":
        search_name = input("What is their name?\n").strip()
    else:
         print("That isn't a stat.")
