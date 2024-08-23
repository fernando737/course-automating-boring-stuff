stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory")
    item_total = sum(inventory.values())
    for k, v in inventory.items():
        print(f"{v} {k}")
    print(f"Total number of items: {item_total}")

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

displayInventory(stuff)
displayInventory(addToInventory(stuff, dragonLoot))
