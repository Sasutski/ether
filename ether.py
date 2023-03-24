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
                variables["bronze"] = variables.get("bronze", 0) + random.randint(1, 10)
                variables["copper"] = variables.get("copper", 0) + random.randint(1, 10)
                print("Mining...")
                time.sleep(3)
                print("Finished mining. You have", variables["bronze"], "bronze and", variables["copper"],"copper now.")
                print(variables["bronze"])
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
                print("Mining...")
                time.sleep(3)
                print("Finished mining. You mined", variables["bronze"] - temp_bronze, "bronze and", variables["copper"] - temp_copper,"copper.")
                print("You now have", variables["bronze"], "bronze and", variables["copper"],"copper now.")
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
        with open('data.pkl', 'wb') as fp:
            pickle.dump(variables, fp)
            break
    break
