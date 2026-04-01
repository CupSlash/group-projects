#BH 2nd RPG character manager
# COMPARE
import sys
import time as t
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
    print() 
def compare(characters):
    compare_first_character = input(f"{characters}, Select your first character.\n")
    while compare_first_character not in characters:
        sprint("Try again. That character doesn't exit yet. :")
        compare_first_character = input(f"{characters}, Select your first character.\n")       
    compare_second_character = input(f"{characters} "elect your second character.\n")
    while compare_second_character not in characters:
        sprint("Try again. That character doesn't exit yet. :")
        compare_second_character = input(f"{characters}, Select your first character.\n")  



# SEARCH
def search_char(characters):
    stat_to_search_by = input("What stat would you like to search by, race, class, level, str, dex, cha, int, or name?\n").strip().lower()
    if stat_to_search_by == "race":
        search_race = input("What is their race?\n").strip()
        sprint(f"{characters.get(search_race)}")
    elif stat_to_search_by == "class":
        search_class= input("What is their class?\n").strip()
        sprint(f"{characters.get(search_class)}")
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
        if (f"{characters[{search_str}]}") == False:
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
        if (f"{characters[{search_cha}]}") == False:
            print("No characters found.")
        else:
            print(f"{characters[search_cha]}")
    elif stat_to_search_by == "int":
        search_int = input("What is their intelligence?\n").strip()
        if (f"{characters[{search_int}]}") == False:
            print("No characters found.")
        else:
            print(f"{characters[search_int]}")
    elif stat_to_search_by == "name":
        search_name = input("What is their name?\n").strip()
        sprint(f"{characters.get(search_name)}")
    else:
         sprint("That isn't a stat.")
