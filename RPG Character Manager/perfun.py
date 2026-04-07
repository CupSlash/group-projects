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
#tuples
dictionaries=(weapons,inventory,spells) #tuple of the dictionary names
#number ensure function (make sure user input is a number)
def validate_is_int():
    while True:
        num=input()
        if f"{num}".isnumeric() and  int(num):
            return int(num)
        else:
                print("Please enter a valid input")
#number ensure function (make sure user input is a number(with parameters)
def validate_is_int_in_range(l,h):
    while True:
        num=input()
        if l and h:
            if f"{num}".isnumeric() and  int(num) in range(l,h):
                return int(num)
            else:
                print("Please enter a valid input")
        else:
            if f"{num}".isnumeric():
                return int(num)
            else:
                print("Please enter a valid input")
#epuip function for equiping equipment
def equip(equipment,cls):
    while True:
        print(f"Hand 1:{equipment['hand_1']}\nHand 2:{equipment['hand_2']}\nArmour:{equipment['armour']}")
        print("Would you like to edit\n1:hands\n2:armour")
        inp=input()
        match inp:
            case "1":
                print("are you\n1:equiping\n2:stowing")
                inp=input()
                match inp:
                    case '1':
                        print("is the item 2 handed?\n1:yes\n2:no")
                        inp=input()
                        match inp:
                            case '1':
                                print("what are you equiping?")
                                inp=input()
                                if equipment["hand_1"] =="" and equipment["hand_2"] =="":
                                    equipment["hand_1"],equipment["hand_2"] =f"{inp}",f"{inp}"
                                else:print("your hands are too full")
                            case '2':
                                print("what are you equiping")
                                inp=input()
                                if equipment["hand_1"] =="":
                                    equipment["hand_1"] =f"{inp}"
                                elif equipment["hand_2"] =="":
                                    equipment["hand_2"] =f"{inp}"
                                else:print("your hands are too full")
                            case _:
                                print("please use a valid input")
                    case "2":
                        print(f"What are you stowing\n1:{equipment['hand_1']}\n2:{equipment['hand_2']}")
                        inp=input()
                        match inp:
                            case "1":
                                equipment["hand_1"]=''
                            case '2':
                                equipment["hand_2"]=''
                            case _:
                                print("please use a valid input")
                    case _:
                        print("please use a valid input")
                return equipment
            case "2":
                print("are you\n1:equiping\n2:dequiping")
                inp=input()
                match inp:
                    case "1":
                        print("How heavy is the armour?\n1:light\n2:medium\n3:Heavy")
                        inp=input()
                        if (cls =='rouge' and (inp=="2" or inp=='3')) or cls=='wizard':
                            print("You do not have training in this kind of armour")
                        else:
                            print("what armour are you equiping?")
                            inp=input()
                            if equipment['armour']=='':
                                equipment['armour']=f'{inp}'
                            else:
                                print("you are already wearing armour")
                    case '2':
                        equipment['armour']=''
                    case _:
                        print("please use a valid input")
                return equipment
            case _:
                print("please use a valid input")
#view function (sprints dictionary contents name and info)
def view(dictionary,dictname):
    for key in dictionary:
        if dictname=="weapons" or dictname=="inventory":
            print(f"{key}:{dictionary[key][0]}, value:{dictionary[key][1]}, weight:{dictionary[key][2]}")
        elif dictname=="spells":
            print(f"{key}:{dictionary[key][0]}, level:{dictionary[key][1]}, casting:{dictionary[key][2]}")
#Add function (asks user for Weapon name, asks user for Weapon info, adds them to a dictionary)
def plus(dictionary,dictname):
    name=input(f"What is the name of the item you would like to add to your inventory?\n")
    info=input(f"What is information you would like to give {name}?\n")
    match dictname:
        case "weapons":
            print(f"What is the value of {name}?")
            value=validate_is_int()
            print(f"What is the weight of {name}?")
            weight=validate_is_int()
            dictionary[name]=[info,value,weight]
            print(f"{name} added to inventory")
        case "inventory":
            print(f"What is the value of {name}?")
            value=validate_is_int()
            print(f"What is the weight of {name}?")
            weight=validate_is_int()
            dictionary[name]=[info,value,weight]
            print(f"{name} added to inventory")
        case "spells":
            print(f"What level of spell is {name}?")
            spellev=validate_is_int()
            time=input(f"What is the casting time of {name}?\n")
            dictionary[name]=[info,spellev,time]
            print(f"{name} added to inventory")
    return dictionary
#Remove function (sprint dictionary, asks user for number Weapon that they want to remove,removes them to a dictionary)
def minus(dictionary):
    print("Note: If you remove it you will have to manually add it back!")
    name=input(f"Which item would you like to remove from your inventory?\n")
    if name in dictionary:
        del dictionary[name]
        print(f'{name} has been removed')
    else:
        print(f"{name} wasn't found in inventory")
    return dictionary
#Search (ask what they want to search by (effect or name) and sprint any weapons that fulfil the requirements)
def search_dict(dictionary):
    key=list(dict(dictionary).keys())
    print("How would you like to search your inventory\n1. name\n2. feature")
    bol=validate_is_int_in_range(1,3)
    inp=input("What are you searching for?\n")
    if bol==1:
        if inp in dictionary:
            print(f"{inp}:{dictionary[inp][0]}, value:{dictionary[inp][1]}, weight:{dictionary[inp][2]} ")
        else:
            print(f"{inp} not in inventory")
    if bol==2:
        for i in range(0,len(key)):
            if f'{inp}' in dictionary[key[i]][0]:
                print(f"{key[i]}:{dictionary[key[i]][0]}, value:{dictionary[key[i]][1]}, weight:{dictionary[key[i]][2]}")
            else:
                continue
#main function for selection how you are editing the dictionary
def edit(dictionary,dictname):
    while True:
        print(f"1:View your {dictname}\n2:add to {dictname}\n3:remove a {dictname}\n4:search {dictname} for specific name/attribute\n5:Exit editor\nWhich option do you want to use?")
        inp=validate_is_int_in_range(1,6)
        if inp==1:
            view(dictionary,dictname)
        elif inp==2:
            plus(dictionary,dictname)
        elif inp==3:
            minus(dictionary)
        elif inp==4:
            search_dict(dictionary)
        elif inp==5:
            break
    return dictionary
#User input for choosing dictionary to edit
def edit_person(character):
    if character['class']=="wizard":
        dictionaries=(weapons,inventory,spells) #tuple of the dictionary names
    else:
        dictionaries=(weapons,inventory)
    print(f"What would you like to edit?\n1:weapons\n2:inventory\n3:equipment")
    if character["class"] =="wizard":
        print("4:spells")
    inp=validate_is_int_in_range(0,len(dictionaries)+1)
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