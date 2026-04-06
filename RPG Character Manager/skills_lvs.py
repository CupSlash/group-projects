
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

def edit_level(character):  
    try:  
        new_level = int(input("Enter your new level: "))  
    except ValueError:  
        print("Invalid input.")
        return
    lv_diff = new_level - character["level"]  
    if lv_diff == 0:  
        print("Level unchanged.")  
        return
    character["level_history"].append(character["level"])
    character["level"] = new_level
    for attribute in ["dexterity", "constitution", "intelligence", "charisma", "strength", "wisdom"]:
        character[f"{attribute}_history"].append(character[attribute])
    points = abs(lv_diff) * 2  
    print(f"You {'gain' if lv_diff > 0 else 'lose'} {points} stat points.")  

    while points > 0:  
        print(f"Current attributes: dexterity={character['dexterity']}, constitution={character['constitution']}, intelligence={character['intelligence']}, charisma={character['charisma']}, strength={character['strength']}, wisdom={character['wisdom']}")  
        attribute = input("Which attribute would you like to modify with points? (dexterity, constitution, intelligence, charisma, strength, wisdom): ").strip()  
        if attribute not in ["dexterity", "constitution", "intelligence", "charisma", "strength", "wisdom"]:  
            print("Invalid attribute name.")  
            continue
        try:  
            change = int(input(f"How many points would you like to {'add to' if lv_diff > 0 else 'remove from'} {attribute}? (Remaining: {points}): "))  
        except ValueError:  
            print("Invalid input.")  
            continue  
        if change <= 0 or change > points:  
            print("Invalid number of points.")  
            continue  
        if lv_diff > 0:  #logic
            character[attribute] += change  
        else:  
            character[attribute] -= change  
        points -= change  
    
    print(f"Level updated to {new_level}. Attributes: dexterity={character['dexterity']}, constitution={character['constitution']}, intelligence={character['intelligence']}, charisma={character['charisma']}, strength={character['strength']}, wisdom={character['wisdom']}")  
def edit_skills(current_skills, character_class, level):  
    available = set()  
    for lv, skills in skills_library[character_class].items():  
        if lv >= level:  #logic
            available.update(skills)  
    to_add = available - current_skills  
    if not to_add:  
        print("No new skills available to add.")  
        return current_skills  
    print(f"Available skills to add: {', '.join(sorted(to_add))}")
    chosen = input("Enter one skill to add (or 'cancel' to skip): ").strip()  
    if chosen in to_add:  
        current_skills.add(chosen)  
        print(f"Added {chosen}. Your skills: {current_skills}")  
    elif chosen == 'cancel':  
        print("Skill addition cancelled.")  
    else:  
        print("Invalid choice.")  
    return current_skills  
