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
        print("Invalid input.")  
        return level, dex, con, int_stat, cha, str_stat, wis  
  
    lv_diff = new_level - level  
    if lv_diff == 0:  
        print("Level unchanged.")  
        return level, dex, con, int_stat, cha, str_stat, wis  
  
    points = abs(lv_diff) * 2  
    print(f"You {'gain' if lv_diff > 0 else 'lose'} {points} stat points.")  
  
    stats = {'dex': dex, 'con': con, 'int': int_stat, 'cha': cha, 'str': str_stat, 'wis': wis}  
  
    while points >= 0:  
        print(f"Current stats: {stats}")  
        stat = input("Which stat? (dex, con, int, cha, str, wis): ").strip()  
        if stat not in stats:  
            print("Invalid stat name.")  
            continue  
        try:  
            change = int(input(f"How many points to {'add to' if lv_diff > 0 else 'remove from'} {stat}? (Remaining: {points}): "))  
        except ValueError:  
            print("Invalid input.")  
            continue  
        if change <= 0 or change > points:  
            print("Invalid number of points.")  
            continue  
        if lv_diff > 0:  #logic
            stats[stat] += change  
        else:  
            stats[stat] -= change  
        points -= change  
  
    print(f"Level updated to {new_level}. Stats: {stats}")  
    return new_level, stats['dex'], stats['con'], stats['int'], stats['cha'], stats['str'], stats['wis']  
def edit_skills(current_skills, character_class, level):  
    available = set()  
    for lv, skills in skills_library[character_class].items():  
        if lv >= level:  #logic
            available.update(skills)  
    to_add = available - current_skills  
    if not to_add:  
        print("No new skills available to add.")  
        return current_skills  
    print("Available skills to add:", ", ".join(sorted(to_add)))  
    chosen = input("Enter one skill to add (or 'cancel' to skip): ").strip()  
    if chosen in to_add:  
        current_skills.add(chosen)  
        print(f"Added {chosen}. Your skills: {current_skills}")  
    elif chosen == 'cancel':  
        print("Skill addition cancelled.")  
    else:  
        print("Invalid choice.")  
    return current_skills  
