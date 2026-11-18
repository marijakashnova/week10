import random

fileHeroes = "heroes.txt"
fileVillians = "villians.txt"
fileWeapons = "weapons.txt"

def load_data(filename):
    with open(filename, "r", encoding= "utf-8") as file:
       data = file.readlines()
    return random.choice(data).strip()

def calculate_attack(character, weapon):
    return 10 + random.randint(0, len(character) + len(weapon))

randomHero = load_data(fileHeroes)
randomVillian = load_data(fileVillians)

heroWeapon = load_data(fileWeapons)
villianWeapon = load_data(fileWeapons)

hero_attack = calculate_attack(randomHero, heroWeapon)
villian_attack = calculate_attack(randomVillian, villianWeapon)

print(f"{randomHero} fights {randomVillian}!")
print(f"{randomHero} uses {heroWeapon}.")
print(f"{randomVillian} uses {villianWeapon}.")

print(f"{randomHero} hits {hero_attack}.")
print(f"{randomVillian} hits {villian_attack}.")

if hero_attack > villian_attack:
    print(f"{randomHero} saves the day!")
elif hero_attack < villian_attack:
    print("The dark side wins!")
else:
    print("It's a draw!")
