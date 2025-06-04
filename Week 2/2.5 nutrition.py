def main():
    fruit = input("Item: ")
    fruit = fruit.title() #All the fruits in dictionary are in title form
    calories(fruit)

def calories(x):
    A = {"Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapes": "90",
    "Grapefruit": "60",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Mango": "70",
    "Nectarine": "60",
    "Orange": "80",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plum": "70",
    "Strawberries": "50",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80"}
    if x in A.keys():
        print(f"Calories: {A[x]}")

main()
