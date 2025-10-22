class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        self.inventory = {}
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase)<20 and new_catchphrase.replace(' ', '').isalpha():
            self.catchphrase=new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")
    
    def add_item(self, item_name):
        item_validate = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
    
        if item_name in item_validate:
            self.furniture.append(item_name)
    
    def print_inventory(self):
        # Implement the method here
        output = ""
        if not self.furniture:
            return "Inventory empty"

        for item in self.furniture:
            if item in self.inventory:
                self.inventory[item] += 1
            else:
                self.inventory[item] = 1
        invent_list=[]
        for item, count in self.inventory.items():
            invent_list.append(f"{item}: {count}")
        
        print(", ".join(invent_list))

#Custom Formatting with f-strings or str.join():
#For more control over the output format, you can iterate through the dictionary items and construct a custom string.
'''my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using f-strings
formatted_string_f = ", ".join(f"{k}: {v}" for k, v in my_dict.items())
print(formatted_string_f)
# Output: name: Alice, age: 30, city: New York

# Using str.join() with a loop
parts = []
for key, value in my_dict.items():
    parts.append(f"{key}: {value}")
formatted_string_join = " | ".join(parts)
print(formatted_string_join)
# Output: name: Alice | age: 30 | city: New York'''

apollo = Villager("Apollo","Eagle","pah")
bones = Villager("Bones", "Dog", "yip yip")
bones.catchphrase = "ruff it up"

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

print(bones.greet_player("Apollo"))


alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()