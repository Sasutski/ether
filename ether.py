import random, time
import pickle, os, os.path
variables = {
    # metals
    "bronze": 0,
    "iron": 0,
    "copper": 0,
    "steel": 0,
    "gold": 0,
    "diamond": 0,
    "platinum": 0,
    "titanium": 0,
    "tungsten": 0,
    "damascus": 0,

    # materials
    "bronze": 0, #mined
    "bismuth": 0, #mined
    "wood": 0, #forage
    "stone": 0, #mined

    #machines
    "bronze_drill":0,
    "copper_drill":0,
    
    #mine
    "mine": "quarry",

    #scrolls
    "scroll_caverns":0,
    "scroll_ether":0,
}

#if no play game

user = ""
playbefore = input("have you played before? y/n \n")
if playbefore.lower() == "y":
    playbefore = "second"
elif playbefore.lower() == "n":
    time.sleep(1)
    print("Welcome to the ether.")
    time.sleep(1)
    print("The story:")
    time.sleep(1)
    print("you are in a universe #278BBUC where everyone has equal rights to mines, as mines are now able to regenerate at a incredible pace. Thus, ores are infinite and society prospers. You are a healthy miner as well as adventurer, and you start off your journey at the starter mine, \"The Quarry\".\n")
    print("Start by trying out the command h or mine to mine for materials.")
    playbefore = "first"
while playbefore.lower() == "first":
    while user.lower() != "q":
        while variables["mine"].lower() == "quarry":
            time.sleep(0.25)
            user = input("What do you want to do next?(h for help, q to quit):")
            if user == "h":
                print("Current Mine: \"cmine\"")
                print("Different Resources: \"r\"")
            elif user == "mine":
                temp_bronze, temp_copper = variables["bronze"], variables["copper"]
                variables["bronze"] += random.randint(1, 10)
                variables["copper"] += random.randint(1, 10)
                print("Mining...\n")
                if variables["bronze_drill"] == 0 and variables["copper_drill"]:
                    time.sleep(3)
                elif variables["bronze_drill"] >= 1 and variables["copper_drill"] == 0:
                    timesleep = (1.5 - (variables["bronze_drill"] * 0.01)) + 1.5
                    time.sleep(timesleep)
                elif variables["bronze_drill"] == 0 and variables["copper_drill"] >= 1:
                    timesleep = (1.5 - (variables["copper_drill"] * 0.01)) + 1.5
                    time.sleep(timesleep)
                else:
                    timesleep = (1.5 - (variables["bronze_drill"] * 0.01)) + (1.5 - (variables["bronze_drill"] * 0.01))
                    time.sleep(timesleep)
               
                print("Finished mining. You mined", variables["bronze"] - temp_bronze, "bronze and", variables["copper"] - temp_copper,"copper.\n")
                print("You now have", variables["bronze"], "bronze and", variables["copper"],"copper now.")
            elif user == "shop":
                print("category?")
                print("machines: improves the efficiency of mining")
                usershopchoice = ""
                while usershopchoice.lower() != "back":
                    usershopchoice = input("Choice:")
                    if usershopchoice == "back":
                        break
                    elif usershopchoice == "machine":
                        print("Options:")
                        bronzedrillprice = 8+((variables["bronze_drill"]+1)*2)
                        print("Bronze Drill: Reduce the amount of time to mine\nPrice:", bronzedrillprice)
                        userbuymachine = ""
                        while userbuymachine.lower() != "back" or userbuymachine != "no":
                            userbuymachine = input("Buy anything?")
                            if userbuymachine == "bronze drill":
                                howmany = int(input("How many?"))
                                price = 0
                                for i in range(howmany):
                                    price += bronzedrillprice
                                    variables["bronze_drill"] += 1
                                variables["bronze_drill"] = 0
                                if variables["bronze"] >= price:
                                    variables["bronze_drill"] += howmany
                                    variables["bronze"] -= bronzedrillprice
                                else:
                                    print("You don't have enough! You need", bronzedrillprice - variables["bronze"], "more bronze!")
                            elif userbuymachine == "back":
                                break

            elif user == "q":
                print("Bye")
                break
            elif user == "cmine":
                print("The Quarry")
            elif user == "r":
                materials = ""
                while materials.lower != "back":
                    materials = input("Which material do you want to know about?\nBronze\nIron\nCopper\nSteel\nGold\nDiamond\nTitanium\nTungsten\nDamascus\nCarbon\nBismuth\nWood\nStone\n")
                    if materials == "back":
                        print("Alright!")
                        break
                    elif materials == "bronze":
                        print("Bronze:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "iron":
                        print("Iron:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "copper":
                        print("Copper:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "steel":
                        print("Steel:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "gold":
                        print("Gold:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "diamond":
                        print("Diamond:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "titanium":
                        print("Titanium:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "tungsten":
                        print("Tungsten:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "damascus":
                        print("Damascus:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "carbon":
                        print("Carbon:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "bismuth":
                        print("Bismuth:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "wood":
                        print("Wood:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "Stone":
                        print("Stone:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    else:
                        print("Not A Command! Please Retry!")
                        time.sleep(1.5)
            elif user == "warp":
                print("You can warp to:")
                print("Quarry(Currently Here)")
                if variables["scroll_caverns"] == 1:
                    print("Caverns")
                if variables["scroll_ether"] == 1:
                    print("Ether")
                warpto = ""
                while warpto.lower() != "back":
                    warpto = input("Where do you want to warp to?(Back to quit)")
                    if warpto == "caverns" and variables["scroll_caverns"] == 1:
                        variables["mine"] = "caverns"
                        print("You have warped to the caverns")
                        break
            else:
                print("Error! Not a command! type \"h\" for help!")
            
            #caverns
        while variables["mine"].lower() == "caverns":
            user = input("What do you want to do next?(h for help, q to quit):")
            if user == "h":
                print("Current Mine: \"cmine\"")
                print("Different Resources: \"r\"")
            elif user == "q":
                print("bye")
                break
            elif user == "cmine":
                print("The Caverns")
            elif user == "r":
                materials = ""
                while materials.lower != "back":
                    materials = input("Which material do you want to know about?\nBronze\nIron\nCopper\nSteel\nGold\nDiamond\nTitanium\nTungsten\nDamascus\nCarbon\nBismuth\nWood\nStone\n")
                    if materials == "back":
                        print("Alright!")
                        break
                    elif materials == "bronze":
                        print("Bronze:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "iron":
                        print("Iron:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "copper":
                        print("Copper:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "steel":
                        print("Steel:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "gold":
                        print("Gold:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "diamond":
                        print("Diamond:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "titanium":
                        print("Titanium:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "tungsten":
                        print("Tungsten:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "damascus":
                        print("Damascus:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "carbon":
                        print("Carbon:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "bismuth":
                        print("Bismuth:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "wood":
                        print("Wood:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "Stone":
                        print("Stone:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    else:
                        print("Not A Command! Please Retry!")
                        time.sleep(1.5)
            elif user == "warp":
                print("You can warp to:")
                print("Cavers(Currently Here)")
                print("Quarry")
                if variables["scroll_ether"] == 1:
                    print("Ether")
                warpto = ""
                while warpto.lower() != "back":
                    warpto = input("Where do you want to warp to?(Back to quit)")
                    if warpto == "quarry":
                        variables["mine"] = "quarry"
                        print("You have warped to the caverns")
                        break
                    break
                break
            break
    with open('data.pkl', 'wb') as fp:
        pickle.dump(variables, fp)
    break
with open('data.pkl', 'rb') as fp:
    variables = pickle.load(fp)

#if played before

while playbefore.lower() == "second":
    while user.lower() != "q":
        while variables["mine"].lower() == "quarry":
            time.sleep(0.25)
            user = input("What do you want to do next?(h for help, q to quit):")
            if user == "h":
                print("Current Mine: \"cmine\"")
                print("Different Resources: \"r\"")
            elif user == "mine":
                temp_bronze, temp_copper = variables["bronze"], variables["copper"]
                variables["bronze"] = variables.get("bronze", 0) + random.randint(1, 10)
                variables["copper"] = variables.get("copper", 0) + random.randint(1, 10)
                print("Mining...\n")
                time.sleep(3)
                print("Finished mining. You mined", variables["bronze"] - temp_bronze, "bronze and", variables["copper"] - temp_copper,"copper.\n")
                print("You now have", variables["bronze"], "bronze and", variables["copper"],"copper now.")
            elif user == "q":
                print("Bye")
                break
            elif user == "shop":
                print("category?")
                print("machines: improves the efficiency of mining")
                usershopchoice = ""
                while usershopchoice.lower() != "back":
                    usershopchoice = input("Choice:")
                    if usershopchoice == "back":
                        break
                    elif usershopchoice == "machine":
                        print("Options:")
                        bronzedrillprice = 8+((variables["bronze_drill"]+1)*2)
                        print("Bronze Drill: Reduce the amount of time to mine\nPrice:", bronzedrillprice)
                        userbuymachine = ""
                        while userbuymachine.lower() != "back" or userbuymachine != "no":
                            userbuymachine = input("Buy anything?")
                            if userbuymachine == "bronze drill":
                                howmany = int(input("How many?"))
                                price = 0
                                for i in range(howmany):
                                    price += bronzedrillprice
                                    variables["bronze_drill"] += 1
                                variables["bronze_drill"] = 0
                                print(variables["bronze_drill"])
                                if variables["bronze"] >= price:
                                    variables["bronze_drill"] += howmany
                                    variables["bronze"] -= bronzedrillprice
                                    print(variables["bronze_drill"])
                                else:
                                    print("You don't have enough! You need", bronzedrillprice - variables["bronze"], "more bronze!")
                            elif userbuymachine == "back":
                                break
            elif user == "cmine":
                print("The Quarry")
            elif user == "r":
                materials = ""
                while materials.lower != "back":
                    materials = input("Which material do you want to know about?\nBronze\nIron\nCopper\nSteel\nGold\nDiamond\nTitanium\nTungsten\nDamascus\nCarbon\nBismuth\nWood\nStone\n")
                    if materials == "back":
                        print("Alright!")
                        break
                    elif materials == "bronze":
                        print("Bronze:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "iron":
                        print("Iron:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "copper":
                        print("Copper:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "steel":
                        print("Steel:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "gold":
                        print("Gold:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "diamond":
                        print("Diamond:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "titanium":
                        print("Titanium:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "tungsten":
                        print("Tungsten:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "damascus":
                        print("Damascus:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "carbon":
                        print("Carbon:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "bismuth":
                        print("Bismuth:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "wood":
                        print("Wood:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "Stone":
                        print("Stone:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    else:
                        print("Not A Command! Please Retry!")
                        time.sleep(1.5)
            elif user == "warp":
                print("You can warp to:")
                print("Quarry(Currently Here)")
                if variables["scroll_caverns"] == 1:
                    print("Caverns")
                if variables["scroll_ether"] == 1:
                    print("Ether")
                warpto = ""
                while warpto.lower() != "back":
                    warpto = input("Where do you want to warp to?(Back to quit)")
                    if warpto == "caverns" and variables["scroll_caverns"] == 1:
                        variables["mine"] = "caverns"
                        print("You have warped to the caverns")
                        break
            else:
                print("Error! Not a command! type \"h\" for help!")

#caverns
        while variables["mine"].lower() == "caverns":
            user = input("What do you want to do next?(h for help, q to quit):")
            if user == "h":
                print("Current Mine: \"cmine\"")
                print("Different Resources: \"r\"")
            elif user == "q":
                print("bye")
                break
            elif user == "cmine":
                print("The Caverns")
            elif user == "r":
                materials = ""
                while materials.lower != "back":
                    materials = input("Which material do you want to know about?\nBronze\nIron\nCopper\nSteel\nGold\nDiamond\nTitanium\nTungsten\nDamascus\nCarbon\nBismuth\nWood\nStone\n")
                    if materials == "back":
                        print("Alright!")
                        break
                    elif materials == "bronze":
                        print("Bronze:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "iron":
                        print("Iron:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "copper":
                        print("Copper:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "steel":
                        print("Steel:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "gold":
                        print("Gold:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "diamond":
                        print("Diamond:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "titanium":
                        print("Titanium:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "tungsten":
                        print("Tungsten:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "damascus":
                        print("Damascus:\nDurability:\nHardness:\nCorrosion Resistance:\n")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "carbon":
                        print("Carbon:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "bismuth":
                        print("Bismuth:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "wood":
                        print("Wood:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    elif materials == "Stone":
                        print("Stone:\nA material used in crafting and building")
                        time.sleep(1.5)
                        print("Anything Else? If not, type back.")
                    else:
                        print("Not A Command! Please Retry!")
                        time.sleep(1.5)
            elif user == "warp":
                print("You can warp to:")
                print("Cavers(Currently Here)")
                print("Quarry")
                if variables["scroll_ether"] == 1:
                    print("Ether")
                warpto = ""
                while warpto.lower() != "back":
                    warpto = input("Where do you want to warp to?(Back to quit)")
                    if warpto == "quarry":
                        variables["mine"] = "quarry"
                        print("You have warped to the caverns")
                        break
        with open('data.pkl', 'wb') as fp:
            pickle.dump(variables, fp)
            break
    break
