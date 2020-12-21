# import 

import json
import requests

# input de récup d'information de l'utilisateur et objet

itemName = str(input("nom de l'item (default T6_MAIN_SWORD): ") or "T6_MAIN_SWORD")
craftPrice =         int(input("prix de l'objet au black market (default 30000)     : ") or "30000")     
enchantmentLe = int(input("Le level d'enchantement (défaut 1)?") or "1")
usageFee =     int(input("donner la taxe du magasin  en pourcentage (defaut 10)              : ") or "242")
premium =     bool(input("premium ? (True/False) (defaut False)               : ") or "False")
resourceReturnRate = float(input("resource return rate (default 15.2)              : ")or "15.2")
itemValue =   int(input("Item value (default 180)             : ") or "180")

# récupère les infos de l'item

item = requests.get('https://gameinfo.albiononline.com/api/gameinfo/items/' + itemName + '/data')
itemToJson = item.json()
enchantmentsList = itemToJson["enchantments"]["enchantments"]

# demande le nombre de matériaux que l'utilisateurs a.

materialList = []
materalNumberStayList = []
for enchantment in enchantmentsList:
    if enchantmentLe == enchantment["enchantmentLevel"]:
            
        print("enchantmentLevel " + str(enchantment["enchantmentLevel"]))
        for craftResource in enchantment["craftingRequirements"]["craftResourceList"]:
            print (craftResource["uniqueName"])
            print (craftResource["count"])
            materialNumberBought =    int(input("combien avez-vous acheté de matériaux (defaut 1600) : ") or "1600")
            materialPrice =int(input("qu'elle est le prix du matériel (defaut 3200)       : ") or "3200")
            materialDic = {"name" : craftResource["uniqueName"], "count" : craftResource["count"], "price" : materialPrice, "bought" : materialNumberBought}
            materalNumberStayDic = {materialDic["name"], materialDic["count"]}            
            materalNumberStayList += [materalNumberStayDic]            
            materialList += [materialDic]
            materialNumberToCreate = craftResource["count"]
print(materialList)
print(materalNumberStayList)

 # taxes

premiumTax = 0.03
unpremiumTax = 0.06
setupFee = 0.015
if premium:
    tax = premiumTax
else:
    tax = unpremiumTax

#calcul du nombre d'objet que l'on peut créer

minimumList = 0
for num in range(len(materialList)):
    numberDivi = materialList[num]["bought"] / materialList[num]["count"]
    if numberDivi < minimumList or minimumList == 0:
        minimumList = numberDivi
    
print(minimumList)




















#craftCreated = 0
#craftNumber = 0
#while materalNumberStay > materialNumberToCreate:                                                     
#    craftNumber += 1
#    craftCreated+= materalNumberStay // materialNumberToCreate
#    for MaterialNumber in range(len(materialList)):   
#        if MaterialNumber == 0:
#            MaterialNumberStay =                        
#        materalNumberStay =     * resourceReturnRate / 100
#        print(str(craftNumber) + " craft, vous avez crafté " + str(craftCreated) + " crafts")
'''
print("Il vous reste " + str(int(materalNumberStay)) + " matériaux")

# Calcul du bénéfice

totalCost = int(materialNumberBought) * int(materialPrice)  + craftCreated * (tax + setupFee) 
print(craftCreated, craftPrice, (craftCreated * craftPrice))
totalSell = (craftCreated * craftPrice) - ((itemValue/20) * (usageFee/100) * craftCreated)

print ("Cout  : " + str(totalCost))
print ("vente : " + str(totalSell))
print ("benefice : " + str(totalSell-totalCost))
'''