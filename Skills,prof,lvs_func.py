#define class_skills as a dictionary  
class_skills = {  
    "wizard": {  
        1: ["arcana", "spellcasting"],  
        3: ["ritual casting"],  
        5: ["fireball"],  
        7: ["counterspell"],  
        10: ["teleport"],  
        15: ["meteor swarm"],  
        20: ["wish"]  
    },  
    "rogue": {  
        1: ["stealth", "thieves’ tools"],  
        3: ["sneak attack"],  
        5: ["evasion"],  
        7: ["uncanny dodge"],  
        10: ["blindsense"],  
        15: ["slippery mind"],  
        20: ["stroke of luck"]  
    },  
    "fighter": {  
        1: ["athletics", "second wind"],  
        3: ["action surge"],  
        5: ["extra attack"],  
        7: ["indomitable"],  
        10: ["leadership"],  
        15: ["survivor"],  
        20: ["champion"]  
    }  
}  
#define class_proficiencies as a dictionary  
#   wizard to: ["arcana", "history", "insight", "investigation"]  
#   rogue to: ["stealth", "acrobatics", "sleight of hand", "deception", "perception"]  
#   fighter to: ["athletics", "intimidation", "survival", "perception"]  
  
#define function get_class_features(character_class, level)  
#   create empty set called skills  
#   for each key lv in class_skills[character_class], in increasing order:  
#       if level greater than or equal to lv:  
#           for each skill in class_skills[character_class][lv]:  
#               add skill to skills  
#   set proficiencies to set of class_proficiencies[character_class]  
#   return skills, proficiencies  
  
#define function show_class_info_and_choose(skills, proficiencies, character_class, character_level)  
#   loop forever:  
#       display "do you want to view skills, proficiencies, or levels for a class? type 'add skill', 'add proficiency', or 'continue' to proceed:"  
#       get user input as choice  
#         
#       if choice equal to "skills":  
#           display "which class? (wizard, rogue, fighter):"  
#           get user input as class_choice  
#           for each level in class_skills[class_choice], in order:  
#               display "level {level}: {class_skills[class_choice][level]}"  
#         
#       else if choice equal to "proficiencies":  
#           display "which class? (wizard, rogue, fighter):"  
#           get user input as class_choice  
#           display "proficiencies for {class_choice}: {class_proficiencies[class_choice]}"  
#         
#       else if choice equal to "levels":  
#           display "which class? (wizard, rogue, fighter):"  
#           get user input as class_choice  
#           display "for {class_choice}, you get:"  
#           for each level in class_skills[class_choice], in order:  
#               display "level {level}: {class_skills[class_choice][level]}"  
#         
#       else if choice equal to "add skill":  
#           create empty set called available_skills  
#           for each level in class_skills[character_class], in order:  
#               if level less than or equal to character_level:  
#                   for each skill in class_skills[character_class][level]:  
#                       if skill not in skills:  
#                           add skill to available_skills  
#           if available_skills is empty:  
#               display "no new skills available to add."  
#           else:  
#               display "available skills to add: {available_skills}"  
#               display "enter the skill you want to add (or type 'cancel' to go back):"  
#               get user input as chosen_skill  
#               if chosen_skill in available_skills:  
#                   add chosen_skill to skills  
#                   display "added {chosen_skill} to your skills. Current skills: {skills}"  
#               else if chosen_skill equal to "cancel":  
#                   continue  
#               else:  
#                   display "not a valid choice"  
#         
#       else if choice equal to "add proficiency":  
#           create empty set called available_proficiencies  
#           for each proficiency in class_proficiencies[character_class]:  
#               if proficiency not in proficiencies:  
#                   add proficiency to available_proficiencies  
#           if available_proficiencies is empty:  
#               display "no new proficiencies available to add."  
#           else:  
#               display "available proficiencies to add: {available_proficiencies}"  
#               display "enter the proficiency you want to add (or type 'cancel' to go back):"  
#               get user input as chosen_prof  
#               if chosen_prof in available_proficiencies:  
#                   add chosen_prof to proficiencies  
#                   display "added {chosen_prof} to your proficiencies. Current proficiencies: {proficiencies}"  
#               else if chosen_prof equal to "cancel":  
#                   continue  
#               else:  
#                   display "not a valid choice"  
#         
#       else if choice equal to "continue":  
#           break  
#         
#       else:  
#           display "not a valid choice"  
  
#define function lv(current_level, skills, proficiencies, character_class, dex, con, int_stat, cha, str_stat, wis)  
#   call show_class_info_and_choose(skills, proficiencies, character_class, current_level)  
#   display user: "what do you want your new level to be?" and store as new_level  
#   if user enters a non-number, print "invalid input" and return  
#   set level_difference to new_level minus current_level  
#   set stat_points to absolute value of level_difference multiplied by 2  
#   if level_difference equal to 0:  
#       print "no level change"  
#       return  
#   if level_difference greater than 0:      # Level Up  
#       print "you need to add {stat_points} stat points"  
#       while stat_points greater than 0:  
#           prompt user: "where do you want to add points? (wis, str, dex, con, cha, int)"  
#           store input as stat  
#           prompt user: "how many points to add to {stat}? (remaining: {stat_points})"  
#           store input as num_stat  
#           if num_stat greater than stat_points or num_stat less than 0:  
#               print "invalid number of points"  
#               continue loop  
#           if stat equal to "wis":  
#               wis = wis + num_stat  
#           else if stat equal to "str":  
#               str_stat = str_stat + num_stat  
#           else if stat equal to "dex":  
#               dex = dex + num_stat  
#           else if stat equal to "con":  
#               con = con + num_stat  
#           else if stat equal to "cha":  
#               cha = cha + num_stat  
#           else if stat equal to "int":  
#               int_stat = int_stat + num_stat  
#           else:  
#               print "invalid stat name"  
#               continue loop  
#           stat_points = stat_points minus num_stat  
#   else:      # Level Down  
#       print "you need to remove {stat_points} stat points"  
#       while stat_points greater than 0:  
#           prompt user: "where do you want to remove points? (wis, str, dex, con, cha, int)"  
#           store input as stat  
#           prompt user: "how many points to remove from {stat}? (remaining: {stat_points})"  
#           store input as num_stat  
#           if num_stat greater than stat_points or num_stat less than 0:  
#               print "invalid number of points"  
#               continue loop  
#           if stat equal to "wis":  
#               wis = wis - num_stat  
#           else if stat equal to "str":  
#               str_stat = str_stat - num_stat  
#           else if stat equal to "dex":  
#               dex = dex - num_stat  
#           else if stat equal to "con":  
#               con = con - num_stat  
#           else if stat equal to "cha":  
#               cha = cha - num_stat  
#           else if stat equal to "int":  
#               int_stat = int_stat - num_stat  
#           else:  
#               print "invalid stat name"  
#               continue loop  
#           stat_points = stat_points minus num_stat  
#   # update skills and proficiencies for new level  
#   call get_class_features(character_class, new_level)  
#   store result as new_skills, new_proficiencies  
#   set skills to the union of skills and new_skills    # skills is a set here  
#   set proficiencies to the union of proficiencies and new_proficiencies    # proficiencies is a set here  
#   print "updated skills: {skills}"  
#   print "updated proficiencies: {proficiencies}"  
#   return a dictionary with:  
#       "level": new_level  
#       "stats": dictionary containing dex, con, int_stat, cha, str_stat, wis  
#       "skills": skills  
#       "proficiencies": proficiencies  
