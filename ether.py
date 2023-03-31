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
        #Drills: makes mining easier
    "bronze_drill":0,
    "copper_drill":0,
        #magic circle: multiplies the resource
    "bronze_magic_circle":0,
    "copper_magic_circle":0,
    
    #mine
    "mine": "quarry",
    "mine": "ether",

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
    print("Version 1.2")
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
                print("Mine Materials: \"mine\"")
                print("Shop: \"shop\"")
                print("Current Mine: \"cmine\"")
                print("Check Resources: \"cr\"")
                print("Different Resources: \"r\"")
                
            elif user == "mine":
                temp_bronze, temp_copper = variables["bronze"], variables["copper"]
                lowestbronze = 5 + variables["bronze_magic_circle"] * 2
                highestbronze = 8 + variables["bronze_magic_circle"] * 2
                lowestcopper = 5 + variables["copper_magic_circle"] * 2
                highestcopper = 8 + variables["copper_magic_circle"] * 2
                variables["bronze"] += random.randint(lowestbronze, highestbronze)
                variables["copper"] += random.randint(lowestcopper, highestcopper)
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
                print("1) machine: improves the efficiency of mining")
                print("2) scrolls: to different places we go!")
                usershopchoice = ""
                while usershopchoice != "back":
                    usershopchoice = input("Choice:")
                    if usershopchoice == "back":
                        break
                    elif usershopchoice == "1":
                        print("Options:")
                        bronzedrillprice = 8+((variables["bronze_drill"]+1)*2)
                        copperdrillprice = 10+((variables["copper_drill"]+1)*2)
                        bronzemagicprice = 15+((variables["bronze_magic_circle"]+1)*2)
                        coppermagicprice = 18+((variables["copper_magic_circle"]+1)*2)
                        print("1)Bronze Drill: Reduce the amount of time to mine in the quarry\nPrice:", bronzedrillprice,"\n")
                        print("2)Copper Drill: Reduce the amount of time to mine in the quarry\nPrice:", copperdrillprice,"\n")
                        print("3)Bronze Magic Circle: increase the amount of bronze mined per mining session.\nPrice:", bronzemagicprice,"\n")
                        print("4)Copper Magic Circle: Increases the amount of copper mined per mining session.\nPrice:", coppermagicprice)
                        userbuymachine = ""
                        time.sleep(1)
                        while userbuymachine.lower() != "back" or userbuymachine != "no":
                            userbuymachine = input("Buy anything? Back to exit")
                            if userbuymachine == "1":
                                howmany = int(input("How many?"))
                                price = 0
                                temp_bronzedrill = variables["bronze_drill"]
                                for i in range(howmany):
                                    price += bronzedrillprice
                                    variables["bronze_drill"] += 1
                                variables["bronze_drill"] = temp_bronzedrill
                                print("Price:", price, "bronze")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["bronze"] >= price:
                                            variables["bronze_drill"] += howmany
                                            variables["bronze"] -= bronzedrillprice
                                            price = 0
                                            print("you have bought", howmany, "bronze drills!")
                                            howmany = 0
                                            break
                                        else:
                                            print("You don't have enough! You need", bronzedrillprice - variables["bronze"], "more bronze!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "2":
                                howmany = int(input("How many? Please put in an integer!"))
                                price = 0
                                temp_copperdrill = variables["copper_drill"]
                                for i in range(howmany):
                                    price += copperdrillprice
                                    variables["copper_drill"] += 1
                                variables["copper_drill"] = temp_copperdrill
                                print("Price:", price, "copper")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["copper"] >= price:
                                            variables["copper_drill"] += howmany
                                            variables["copper"] -= copperdrillprice
                                            price = 0
                                            print("you have bought", howmany, "copper drills!")
                                            howmany = 0
                                            break    
                                        else:
                                            print("You don't have enough! You need", copperdrillprice - variables["copper"], "more copper!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "3":
                                howmany = int(input("How many?"))
                                price = 0
                                temp_bronzemagic = variables["bronze_magic_circle"]
                                for i in range(howmany):
                                    price += bronzemagicprice
                                    variables["bronze_magic_circle"] += 1
                                variables["bronze_magic_circle"] = temp_bronzemagic
                                print("Price:", price, "bronze")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["bronze"] >= price:
                                            variables["bronze_magic_circle"] += howmany
                                            variables["bronze"] -= bronzemagicprice
                                            price = 0
                                            print("you have bought", howmany, "bronze magic circle!")
                                            howmany = 0
                                            break    
                                        else:
                                            print("You don't have enough! You need", bronzemagicprice - variables["bronze"], "more bronze!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "4":
                                howmany = int(input("How many?"))
                                price = 0
                                temp_coppermagic = variables["copper_magic_circle"]
                                for i in range(howmany):
                                    price += coppermagicprice
                                    variables["copper_magic_circle"] += 1
                                variables["copper_magic_circle"] = temp_coppermagic
                                print("Price:", price, "copper")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["copper"] >= price:
                                            variables["copper_magic_circle"] += howmany
                                            variables["copper"] -= coppermagicprice
                                            price = 0
                                            print("you have bought", howmany, "copper magic circle!")
                                            howmany = 0
                                            break    
                                        else:
                                            print("You don't have enough! You need", coppermagicprice - variables["copper"], "more copper!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "back":
                                break
                            else:
                                print("Input the number corresponding to the item! eg. 1 = bronze drill because 1)Bronze Drill")
                    elif usershopchoice == "2":
                        print("options")
                        print("1)Scroll to the caverns")
                        print("Would you like to buy this? (y/n) price: 1000 bronze and 1000 copper")
                        userbuyscroll = ""
                        while userbuyscroll.lower() != "n":
                            if userbuyscroll == "y":
                                if variables["bronze"] >= 1000 and variables["copper"] >= 1000 and variables["scroll_caverns"] != 1:
                                    print("Successfully bought!")
                                    variables["scroll_caverns"] = 1
                                    variables["bronze"] - 1000
                                    variables["copper"] - 1000
                                elif variables["scroll_caverns"] == 1:
                                    print("You already have bought the max amount (1) of this!")
                                elif variables["bronze"] < 1000 and variables["copper"] >= 1000:
                                    print("Not enought bronze! You need", 1000 - variables["bronze"], "more bronze!")
                                elif variables["bronze"] >= 1000 and variables["copper"] < 1000:
                                    print("Not enough copper! You need", 1000 - variables["copper"], "more copper!")
                                else:
                                    print("Not enough bronze and copper! You need", 1000 - variables["bronze"], "more bronze and", 1000 - variables["copper"], "more copper!")
                            elif userbuyscroll.lower() != "n":
                                break
                    else:
                        print("Not a command! Please try again!")
            elif user == "q":
                print("Bye")
                break
            elif user == "cmine":
                print("The Quarry")
            elif user == "cr":
                print("Amount of bronze:", variables["bronze"])
                print("Amount of copper:", variables["copper"])
                print("Amount of bronze drills:", variables["bronze_drill"])
                print("Amount of copper drills:", variables["copper_drill"])
                print("Amount of bronze magic circles:", variables["bronze_magic_circle"])
                print("Amount of copper magic circles:", variables["copper_magic_circle"])
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
            with open('data.pkl', 'wb') as fp:
                pickle.dump(variables, fp)


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
            with open('data.pkl', 'wb') as fp:
                pickle.dump(variables, fp)      
    break

with open('data.pkl', 'rb') as fp:
    variables = pickle.load(fp)

#if played before

while playbefore.lower() == "second":
    print("Welcome Back!")
    print("Version 1.2")
    while user.lower() != "q":
        while variables["mine"].lower() == "quarry":
            time.sleep(0.25)
            user = input("What do you want to do next?(h for help, q to quit):")
            if user == "h":
                print("Mine Materials: \"mine\"")
                print("Shop: \"shop\"")
                print("Current Mine: \"cmine\"")
                print("Check Resources: \"cr\"")
                print("Different Resources: \"r\"")
                
            elif user == "mine":
                temp_bronze, temp_copper = variables["bronze"], variables["copper"]
                lowestbronze = 5 + variables["bronze_magic_circle"] * 2
                highestbronze = 8 + variables["bronze_magic_circle"] * 2
                lowestcopper = 5 + variables["copper_magic_circle"] * 2
                highestcopper = 8 + variables["copper_magic_circle"] * 2
                variables["bronze"] += random.randint(lowestbronze, highestbronze)
                variables["copper"] += random.randint(lowestcopper, highestcopper)
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
                print("1) machine: improves the efficiency of mining")
                print("2) scrolls: to different places we go!")
                usershopchoice = ""
                while usershopchoice != "back":
                    usershopchoice = input("Choice:")
                    if usershopchoice == "back":
                        break
                    elif usershopchoice == "1":
                        print("Options:")
                        bronzedrillprice = 8+((variables["bronze_drill"]+1)*2)
                        copperdrillprice = 10+((variables["copper_drill"]+1)*2)
                        bronzemagicprice = 15+((variables["bronze_magic_circle"]+1)*2)
                        coppermagicprice = 18+((variables["copper_magic_circle"]+1)*2)
                        print("1)Bronze Drill: Reduce the amount of time to mine in the quarry\nPrice:", bronzedrillprice,"\n")
                        print("2)Copper Drill: Reduce the amount of time to mine in the quarry\nPrice:", copperdrillprice,"\n")
                        print("3)Bronze Magic Circle: increase the amount of bronze mined per mining session.\nPrice:", bronzemagicprice,"\n")
                        print("4)Copper Magic Circle: Increases the amount of copper mined per mining session.\nPrice:", coppermagicprice)
                        userbuymachine = ""
                        time.sleep(1)
                        while userbuymachine.lower() != "back" or userbuymachine != "no":
                            userbuymachine = input("Buy anything? Back to exit")
                            if userbuymachine == "1":
                                howmany = int(input("How many?"))
                                price = 0
                                temp_bronzedrill = variables["bronze_drill"]
                                for i in range(howmany):
                                    price += bronzedrillprice
                                    variables["bronze_drill"] += 1
                                variables["bronze_drill"] = temp_bronzedrill
                                print("Price:", price, "bronze")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["bronze"] >= price:
                                            variables["bronze_drill"] += howmany
                                            variables["bronze"] -= bronzedrillprice
                                            price = 0
                                            print("you have bought", howmany, "bronze drills!")
                                            howmany = 0
                                            break
                                        else:
                                            print("You don't have enough! You need", bronzedrillprice - variables["bronze"], "more bronze!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "2":
                                howmany = int(input("How many? Please put in an integer!"))
                                price = 0
                                temp_copperdrill = variables["copper_drill"]
                                for i in range(howmany):
                                    price += copperdrillprice
                                    variables["copper_drill"] += 1
                                variables["copper_drill"] = temp_copperdrill
                                print("Price:", price, "copper")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["copper"] >= price:
                                            variables["copper_drill"] += howmany
                                            variables["copper"] -= copperdrillprice
                                            price = 0
                                            print("you have bought", howmany, "copper drills!")
                                            howmany = 0
                                            break    
                                        else:
                                            print("You don't have enough! You need", copperdrillprice - variables["copper"], "more copper!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "3":
                                howmany = int(input("How many?"))
                                price = 0
                                temp_bronzemagic = variables["bronze_magic_circle"]
                                for i in range(howmany):
                                    price += bronzemagicprice
                                    variables["bronze_magic_circle"] += 1
                                variables["bronze_magic_circle"] = temp_bronzemagic
                                print("Price:", price, "bronze")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["bronze"] >= price:
                                            variables["bronze_magic_circle"] += howmany
                                            variables["bronze"] -= bronzemagicprice
                                            price = 0
                                            print("you have bought", howmany, "bronze magic circle!")
                                            howmany = 0
                                            break    
                                        else:
                                            print("You don't have enough! You need", bronzemagicprice - variables["bronze"], "more bronze!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "4":
                                howmany = int(input("How many?"))
                                price = 0
                                temp_coppermagic = variables["copper_magic_circle"]
                                for i in range(howmany):
                                    price += coppermagicprice
                                    variables["copper_magic_circle"] += 1
                                variables["copper_magic_circle"] = temp_coppermagic
                                print("Price:", price, "copper")
                                choice = ""
                                while choice.lower() != "n":
                                    choice = input("Are you sure you want to buy this? (y/n)")
                                    if choice == "y":
                                        if variables["copper"] >= price:
                                            variables["copper_magic_circle"] += howmany
                                            variables["copper"] -= coppermagicprice
                                            price = 0
                                            print("you have bought", howmany, "copper magic circle!")
                                            howmany = 0
                                            break    
                                        else:
                                            print("You don't have enough! You need", coppermagicprice - variables["copper"], "more copper!")
                                            price = 0
                                            howmany = 0
                                            break
                                    elif choice == "n":
                                        break
                            elif userbuymachine == "back":
                                break
                            else:
                                print("Input the number corresponding to the item! eg. 1 = bronze drill because 1)Bronze Drill")
                    elif usershopchoice == "2":
                        print("options")
                        print("1)Scroll to the caverns")
                        print("Would you like to buy this? (y/n) price: 1000 bronze and 1000 copper")
                        userbuyscroll = ""
                        while userbuyscroll.lower() != "n":
                            if userbuyscroll == "y":
                                if variables["bronze"] >= 1000 and variables["copper"] >= 1000 and variables["scroll_caverns"] != 1:
                                    print("Successfully bought!")
                                    variables["scroll_caverns"] = 1
                                    variables["bronze"] - 1000
                                    variables["copper"] - 1000
                                elif variables["scroll_caverns"] == 1:
                                    print("You already have bought the max amount (1) of this!")
                                elif variables["bronze"] < 1000 and variables["copper"] >= 1000:
                                    print("Not enought bronze! You need", 1000 - variables["bronze"], "more bronze!")
                                elif variables["bronze"] >= 1000 and variables["copper"] < 1000:
                                    print("Not enough copper! You need", 1000 - variables["copper"], "more copper!")
                                else:
                                    print("Not enough bronze and copper! You need", 1000 - variables["bronze"], "more bronze and", 1000 - variables["copper"], "more copper!")
                            elif userbuyscroll.lower() != "n":
                                break
                    else:
                        print("Not a command! Please try again!")
            elif user == "q":
                print("Bye")
                break
            elif user == "cmine":
                print("The Quarry")
            elif user == "cr":
                print("Amount of bronze:", variables["bronze"])
                print("Amount of copper:", variables["copper"])
                print("Amount of bronze drills:", variables["bronze_drill"])
                print("Amount of copper drills:", variables["copper_drill"])
                print("Amount of bronze magic circles:", variables["bronze_magic_circle"])
                print("Amount of copper magic circles:", variables["copper_magic_circle"])
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
            with open('data.pkl', 'wb') as fp:
                pickle.dump(variables, fp)


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
            with open('data.pkl', 'wb') as fp:
                pickle.dump(variables, fp)      
    break