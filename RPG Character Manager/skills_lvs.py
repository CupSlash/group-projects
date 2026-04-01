
import sys
import time as t
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
    sprint() 
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

def edit_level(level, dex, con, int_stat, cha, str_stat, wis):  
    try:  
        new_level = int(input("Enter your new level: "))  
    except ValueError:  
        sprint("Invalid input.")  
        return level, dex, con, int_stat, cha, str_stat, wis  
  
    lv_diff = new_level - level  
    if lv_diff == 0:  
        sprint("Level unchanged.")  
        return level, dex, con, int_stat, cha, str_stat, wis  
  
    points = abs(lv_diff) * 2  
    sprint(f"You {'gain' if lv_diff > 0 else 'lose'} {points} stat points.")  
  
    stats = {'dex': dex, 'con': con, 'int': int_stat, 'cha': cha, 'str': str_stat, 'wis': wis}  
  
    while points >= 0:  
        sprint(f"Current stats: {stats}")  
        stat = input("Which stat? (dex, con, int, cha, str, wis): ").strip()  
        if stat not in stats:  
            sprint("Invalid stat name.")  
            continue  
        try:  
            change = int(input(f"How many points to {'add to' if lv_diff > 0 else 'remove from'} {stat}? (Remaining: {points}): "))  
        except ValueError:  
            sprint("Invalid input.")  
            continue  
        if change <= 0 or change > points:  
            sprint("Invalid number of points.")  
            continue  
        if lv_diff > 0:  #logic
            stats[stat] += change  
        else:  
            stats[stat] -= change  
        points -= change  
  
    sprint(f"Level updated to {new_level}. Stats: {stats}")  
    return new_level, stats['dex'], stats['con'], stats['int'], stats['cha'], stats['str'], stats['wis']  
def edit_skills(current_skills, character_class, level):  
    available = set()  
    for lv, skills in skills_library[character_class].items():  
        if lv >= level:  #logic
            available.update(skills)  
    to_add = available - current_skills  
    if not to_add:  
        sprint("No new skills available to add.")  
        return current_skills  
    sprint("Available skills to add:", ", ".join(sorted(to_add)))  #Problem I think
    chosen = input("Enter one skill to add (or 'cancel' to skip): ").strip()  
    if chosen in to_add:  
        current_skills.add(chosen)  
        sprint(f"Added {chosen}. Your skills: {current_skills}")  
    elif chosen == 'cancel':  
        sprint("Skill addition cancelled.")  
    else:  
        sprint("Invalid choice.")  
    return current_skills  
