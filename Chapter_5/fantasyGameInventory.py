stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += int(v)
    print(f"Total number of items: {item_total}")

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item,0)
        inventory[item] += 1

    return inventory

displayInventory(stuff)
displayInventory(addToInventory(stuff, dragonLoot))