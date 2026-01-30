
#Dictionaries 
import sys
import time as t
def sprint(text, delay=0.015):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay) 
    print()     
weapons={ #weapons that character has

}
inventory={ #items that player has
}
spells={ #spells and their descriptions
}
equipment={
    "hand_1":'',
    "hand_2":'',
    "armour":'',
}

character={'class':'wizard'}
cls="wizard"
#tuples
if cls=="wizard":
    dictionaries=(weapons,inventory,spells) #tuple of the dictionary names
else:
    dictionaries=(weapons,inventory)
#number ensure function (make sure user input is a number)
def insure():
    while True:
        num=input()
        if f"{num}".isnumeric() and  int(num):
            return int(num)
        else:
                sprint("Please enter a valid input")
#number ensure function (make sure user input is a number(with parameters)
def ensure(l,h):
    while True:
        num=input()
        if l and h:
            if f"{num}".isnumeric() and  int(num) in range(l,h):
                return int(num)
            else:
                sprint("Please enter a valid input")
        else:
            if f"{num}".isnumeric():
                return int(num)
            else:
                sprint("Please enter a valid input")

#epuip function for equiping equipment
def equip(equipment,cls):
    while True:
        sprint(f'Hand 1:{equipment['hand_1']}\nHand 2:{equipment['hand_2']}\nArmour:{equipment['armour']}')
        inp=input("Would you like to edit\n1:hands\n2:armour\n")
        match inp:
            case "1":
                inp=input("are you\n1:equiping\n2:stowing\n")
                match inp:
                    case '1':
                        inp=input("is the item 2 handed?\n1:yes\n2:no\n")
                        match inp:
                            case '1':
                                inp=input("what are you equiping?\n")
                                if equipment["hand_1"] =="" and equipment["hand_2"] =="":
                                    equipment["hand_1"],equipment["hand_2"] =f"{inp}",f"{inp}"
                                else:sprint("your hands ar too full")
                            case '2':
                                inp=input("what are you equiping?\n")
                                if equipment["hand_1"] =="":
                                    equipment["hand_1"] =f"{inp}"
                                elif equipment["hand_2"] =="":
                                    equipment["hand_2"] =f"{inp}"
                                else:sprint("your hands ar too full")
                    case "2":
                        inp=input(f"What are you stowing\n1:{equipment['hand_1']}\n2:{equipment['hand_2']}\n")
                        match inp:
                            case "1":
                                equipment["hand_1"]=''
                            case '2':
                                equipment["hand_2"]=''
                            case _:
                                sprint("please use a valid input")
                    case _:
                        sprint("please use a valid input")
                sprint(f'Hand 1:{equipment['hand_1']}\nHand 2:{equipment['hand_2']}\nArmour:{equipment['armour']}')
                return equipment
            case "2":
                inp=input("are you\n1:equiping\n2:dequiping\n")
                match inp:
                    case "1":
                        inp=input("How heavy is the armour?\n1:light\n2:medium\n3:Heavy\n")
                        if (cls =='rouge' and (inp=="2" or inp=='3')) or cls=='wizard':
                            sprint("You do not have training in this kind of armour")
                        else:
                            inp=input("what armour are you equiping?\n")
                            if equipment['armour']=='':
                                equipment['armour']=f'{inp}'
                            else:
                                sprint("you are already wearing armour")
                    case '2':
                        equipment['armour']=''
                    case _:
                        sprint("please use a valid input")
                sprint(f'Hand 1:{equipment['hand_1']}\nHand 2:{equipment['hand_2']}\nArmour:{equipment['armour']}')
                return equipment
#view function (sprints dictionary contents name and info)
def view(dictionary,dictname):
    for key in dictionary:
        if dictname=="weapons"or"inventory":
            sprint(f"{key}:{dictionary[key][0]}, value:{dictionary[key][1]}, weight:{dictionary[key][2]}")
        elif dictname=="spells":
            sprint(f"{key}:{dictionary[key][0]}, level:{dictionary[key][1]}, casting:{dictionary[key][2]}")
#Add function (asks user for Weapon name, asks user for Weapon info, adds them to a dictionary)
def plus(dictionary,dictname):
    name=input(f"What is the name of the item you would like to add to your inventory?\n")
    info=input(f"What is information you would like to give {name}?\n")
    match dictname:
        case "weapons":
            sprint(f"What is the value of {name}?")
            value=insure()
            sprint(f"What is the weight of {name}?")
            weight=insure()
            dictionary[name]=[info,value,weight]
            sprint(f"{name} added to inventory")
        case "inventory":
            sprint(f"What is the value of {name}?")
            value=insure()
            sprint(f"What is the weight of {name}?")
            weight=insure()
            dictionary[name]=[info,value,weight]
            sprint(f"{name} added to inventory")
        case "spells":
            sprint(f"What level of spell is {name}?")
            spellev=insure()
            time=input(f"What is the casting time of {name}?\n")
            dictionary[name]=[info,spellev,time]
            sprint(f"{name} added to inventory")
    return dictionary
#Remove function (sprint dictionary, asks user for number Weapon that they want to remove,removes them to a dictionary)
def minus(dictionary):
    for key in dictionary:
        sprint(key)
    sprint("Note: If you remove it you will have to manually add it back!")
    name=input(f"Which item would you like to remove from your inventory?\n")
    if name in dictionary:
        del dictionary[name]
        sprint(f'{name} has been removed')
    else:
        sprint(f"{name} wasn't found in inventory")
    return dictionary
#Search (ask what they want to search by (effect or name) and sprint any weapons that fulfil the requirements)
def search(dictionary, dictname):
    key=list(dict(dictionary).keys())
    sprint(f"How would you like to search your {dictname}\n1. name\n2. feature")
    bol=ensure(1,3)
    inp=input("What are you searching for?\n")
    if bol==1:
        if inp in dictionary:
            sprint(f"{inp}:{dictionary[inp][0]}, value:{dictionary[inp][1]}, weight:{dictionary[inp][2]} ")
        else:
            sprint(f"{inp} not in inventory")
    if bol==2:
        for i in range(0,len(key)):
            if f'{inp}' in dictionary[key[i]][0]:
                if dictname=="weapons"or"inventory":
                    sprint(f"{key}:{dictionary[key][0]}, value:{dictionary[key][1]}, weight:{dictionary[key][2]}")
                elif dictname=="spells":
                    sprint(f"{key}:{dictionary[key][0]}, level:{dictionary[key][1]}, casting:{dictionary[key][2]}")
            else:
                continue
#main function for selection how you are editing the dictionary
def edit(dictionary,dictname):
    while True:
        sprint(f"1:View your {dictname}\n2:add to {dictname}\n3:remove a {dictname}\n4:search {dictname} for specific name/attribute\n5:Exit editor\nWhich option do you want to use?")
        inp=ensure(1,6)
        if inp==1:
            view(dictionary,dictname)
        elif inp==2:
            plus(dictionary,dictname)
        elif inp==3:
            minus(dictionary)
        elif inp==4:
            search(dictionary,dictname)
        elif inp==5:
            break
    return dictionary
#User input for choosing dictionary to edit
def choice(character):
    while True:
        if character['class']=="wizard":
            dictionaries=(weapons,inventory,spells) #tuple of the dictionary names
        else:
            dictionaries=(weapons,inventory)
        sprint(f"What would you like to edit?\n0:Exit\n1:weapons\n2:inventory\n3:equipment")
        if character["class"] =="wizard":
            sprint("4:spells")
        inp=ensure(0,len(dictionaries)+1)
        if inp==1:
            edit(weapons,"weapons")
            return weapons
        if inp==2:
            edit(inventory,"inventory")
            return inventory
        if inp==3:
            equip(equipment,character["class"])
            return equipment
        if inp==4:
            edit(spells,"spells")
            return spells
        if inp==0:
            break
choice(character)