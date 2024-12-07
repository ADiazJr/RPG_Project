import random

def RunGame():
    hercules_hp = 40
    hercules_ap = 25
    enemy_hp = 40
    enemy_ap = 15
    winround1 = False

    while enemy_hp > 0 and hercules_hp > 0:
        user_input = prompt(hercules_hp, hercules_ap)
        
        if user_input in ["0", "1", "2", "3"]:
            print("You attack the Raid Boss!")
            enemy_hp = attack(enemy_hp, hercules_ap)
            
            if enemy_hp <= 0:
                print("You have killed the enemy!")
                break
            
            print(f'The enemy attacks you back with {random.choice(attack_names)}')
            hercules_hp = attackback(hercules_hp, enemy_ap)
            
            if hercules_hp <= 0:
                print("You have been defeated!")
                winround1 = True
                break
            
            print(f'Your Health: {hercules_hp}')
            print(f'Raid Boss Health: {enemy_hp}')
        else:
            print("Invalid input. Please try again.")
    if winround1 : True 
    Uprgade(hercules_ap)


attack_names = ['Sword Slash', 'Shield Bash', "Lunge", "Slide"]

print("""You are Hercules, a hero that is being monitored by a highly powerful organization. You have no choice but to obey every living second.
That is until you don't. You are captured and en route to be killed. You manage to escape and realize you're inside the enemy base,
face to face with the leader of the organization.""")

def prompt(hercules_hp, hercules_ap):
    print(f'You are at {hercules_hp} Health and have an attack power of {hercules_ap}')
    for i in range(len(attack_names)):
        print(f'Please type {i} if you would like to use {attack_names[i]}')
    selection = input("Please type your selection here: ")
    return selection

def attack(enemy_hp, hercules_ap):
    print(f"The enemy is at {enemy_hp} health and you hit him for {hercules_ap} damage.")
    current_enemy_hp = max(0, enemy_hp - hercules_ap)
    print(f"The enemy is now at {current_enemy_hp} health.")
    return current_enemy_hp

def attackback(hercules_hp, enemy_ap):
    print(f"The enemy hits you for {enemy_ap} damage.")
    your_current_hp = max(0, hercules_hp - enemy_ap)
    return your_current_hp

def Uprgade(hercules_ap):
    print('After defeating your enemy, you feel a charge of light fill your body, roll the dice to see your fate.' )
    input("type Roll to Roll:")
    dice_roll = random.randint(0, 10) 
    print(dice_roll)
    if dice_roll <5: print("no updgrade see ya next time!")
    if dice_roll >5: print("your attack has been increased!")
    if dice_roll >5: hercules_ap *1.5
RunGame()
