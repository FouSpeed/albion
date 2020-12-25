# import 

import json
import requests

# input

money =         int(input("argent? default (5000000)                                            : ") or "5000000")
objectToBuild = str(input("objet? (default T6_MAIN_SWORD)                                       : ") or "T6_MAIN_SWORD")
objectLevel =   int(input("Level ? (default 1)                                                  : ") or "1")
premium =      bool(input("premium (True/False)                                                 : ") or "True" )
shoptTaxe =     int(input("Taxe de l'endroit où vous craftez? default 5                         : ") or "5")                                       
returnRate =  float(input("return rate de l'endroit où vous craftez ? default 15.2 (24.8, 36.7) : ") or "24.8")
ItemValue =     int(input("qu'elle est la valeur de l'objet (item value) ? (default 200)        : ") or "200")
itemPrice =     int(input("prix de l'objet ? default 50000                                      : ") or "50000")

# variables

apiDataItems = 'https://gameinfo.albiononline.com/api/gameinfo/items/' + objectToBuild + '/data'
moneyTest = 0 
craftNumber = 0
numberElement = 0
sellTax = 0

# récupère les infos de l'item10

item = requests.get(apiDataItems)
itemToJson = item.json()
enchantmentsList = itemToJson["enchantments"]["enchantments"]

itemDico = []
for enchantment in enchantmentsList:
    if objectLevel == enchantment["enchantmentLevel"]:
        for craftResource in enchantment["craftingRequirements"]["craftResourceList"]:
            itemName = craftResource["uniqueName"]
            materalPrice =     int(input("Prix de " + itemName + " ? (default 3000)                     : ") or "3000")
            itemDico += [{"item": itemName, "price": materalPrice, "count": craftResource["count"], "bought": 0}]

# résumé

for item in itemDico:
    print ("il faut " + item["item"] + " qui coute " + str(item["price"]) + " et il en faut " + str(item["count"]))

# taxe

premiumTax = 0.03
unpremiumTax = 0.06
setupFee = 0.015
if premium:
    tax = premiumTax
else:
    tax = unpremiumTax

# nombre d'objets créé [compter: le nombre de taxes, le nombre de matériaux acheter, les livres] pour enlever : del

while money > moneyTest:
    moneyTest -= sellTax
    for materal in itemDico:
        moneyTest += (materal["count"] * materal["price"])  # on sait le nombre de matériaux
        for number in range (len(itemDico)):
            itemDico[number]["bought"] += itemDico[number]["count"]
         # on sait le nombre d'élément par matériaux revoir juste pour le premiere élément 
    numberElement += itemDico[0]["count"]
    # savoir le nombre quel'on peut creer
    while numberElement >  itemDico[0]["count"]:
        craftNumber += numberElement / itemDico[0]["count"]
        numberElement = numberElement * returnRate / 100
    # ajouter les taxes
    moneyTest += ItemValue / 20 * returnRate / 100 * craftNumber # vend
    sellTax = (int(craftNumber) * itemPrice) * (tax + setupFee) #créé
    moneyTest += sellTax 

# livres ou pas

registreUse = str(input("voulez-vous utilisez des registres (o/n)? (default n)") or "no")
if registreUse == "o":
    fprice = int(input("coût des livres vides defaut 8400 : ") or "8400")
    sprice = int(input("coût des livres pleins defaut 22 000 : ") or "22000")
    fameJournal = int(input("fame pour remplir un livre : ") or "4800" )
    famecraft = int(input("fame par craft : ") or "7887")
    totalMoneyJournal = ((craftNumber * famecraft) / fameJournal) * (sprice - fprice)
    benefice += totalMoneyJournal

# bénéfice

benefice = (int(craftNumber) * itemPrice) - moneyTest

#print

for i in range (len(itemDico)):
    print("il faut acheter " + str(itemDico[i]["bought"]) + " éléments")
print(benefice, craftNumber, itemPrice)
