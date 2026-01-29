# WH 2nd 

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
        want = input("(1: yes/ 2: no)\n").strip()
        while True:
            if want == "1" or want == "yes":
                return class_race
            elif want == "1" or want == "no":
                break
            else:
                print("not an option.")

def character_creator(races, classes ,characters = dict):
    character_name = input("What is the new character's name?\n")
    new_character = dict()
    new_character["race"] = modifier_selector("race",races)
    new_character["class"] = modifier_selector("class",classes)
    text = ["level","strength","dexterity","wisdom","charisma","intelligence","constitution"]
    for item in text:
        new_character[item] = help_isint_input(f"What is {character_name}'s {item}?\n")
    characters[character_name] = new_character
    return characters
