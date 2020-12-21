# import 

import json
import requests

# input

money = int(input("argent? default (5000000)") or "5000000")
objectToBuild = str(input("objet? (default T6_MAIN_SWORD)") or "T6_MAIN_SWORD")
objectLevel = int(input("Level ? (default 1)") or "1")

# variables
apiDataItems = 'https://gameinfo.albiononline.com/api/gameinfo/items/' + objectToBuild + '/data'

# récupère les infos de l'item

item = requests.get(apiDataItems)
itemToJson = item.json()
enchantmentsList = itemToJson["enchantments"]["enchantments"]

itemDico = []
for enchantment in enchantmentsList:
    if objectLevel == enchantment["enchantmentLevel"]:
        for craftResource in enchantment["craftingRequirements"]["craftResourceList"]:
            itemName = craftResource["uniqueName"]
            itemPrice = int(input("Prix de " + itemName + " ? (default 3000)") or "3000")
            itemDico += [{"item": itemName, "price": itemPrice, "count": craftResource["count"]}]

# résumé

for item in itemDico:
    print ("il faut " + item["item"] + " qui coute " + str(item["price"]) + " et il en faut " + str(item["count"]))

# nombre d'objets créé


itemTotalNumber = money / ((itemDico[0]["price"] * itemDico[0]["count"]) + (itemDico[0]["price"] * itemDico[0]["count"]))
print(itemTotalNumber)