import json
import requests

itemName = "T6_MAIN_SWORD"

item = requests.get('https://gameinfo.albiononline.com/api/gameinfo/items/' + itemName + '/data')
#print(r.text)
# avec l'api on veut savoir:
# ex https://gameinfo.albiononline.com/api/gameinfo/items/T6_SHOES_CLOTH_SET1/data
#les matériaux utiliser dans craftResourceList
#savoir si premium ou pas avec l'id de la personne
#item value
# fame donner lors de la fabrication    
# photo objet https://gameinfo.albiononline.com/api/gameinfo/items/T6_SHOES_CLOTH_SET1/
#temps de craft dans craftingrequirment
itemToJson = item.json()
enchantmentsList = itemToJson["enchantments"]["enchantments"]

print(enchantmentsList)

for enchantment in enchantmentsList:
    print("enchantmentLevel " + str(enchantment["enchantmentLevel"]))
    # print("itemPower " + str(enchantment["itemPower"]))
    # print("durability " + str(enchantment["durability"]))
    # print("Time of craftingRequirements " + str(enchantment["craftingRequirements"]["time"]))
    # print("Silver of craftingRequirements " + str(enchantment["craftingRequirements"]["silver"]))
    # print("CraftingFocus of craftingRequirements " + str(enchantment["craftingRequirements"]["craftingFocus"]))

    for craftResource in enchantment["craftingRequirements"]["craftResourceList"]:
        print (craftResource["uniqueName"])
        print (craftResource["count"])
