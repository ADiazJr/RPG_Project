import random

def RunGame():
    # Initialize Character Stats
    hercules_hp = 40
    hercules_ap = 25
    enemy_hp = 40
    enemy_ap = 15
    attack_names = ['Sword Slash', 'Shield Bash', "Lunge", "Slide"]
    continue_battle = False

    #Welcome Message to Player
    print("""You are Hercules, a hero that is being monitored by a highly powerful organization. You have no choice but to obey every living second.
    That is until you don't. You are captured and en route to be killed. You manage to escape and realize you're inside the enemy base,
    face to face with one of your arch rivals, HADES! You ready for battle.\n""")

    #Linear Battle Path
    hercules_hp, hercules_ap, hercules_win = Battle(enemy_hp, enemy_ap, hercules_ap, hercules_hp, attack_names, enemy_name="Hades")
    if hercules_win:
        print("Congratulations! You won the battle\n")
        hercules_ap = Uprgade(hercules_ap)
        print(f"Your new attack power is {hercules_ap}\n")
        continue_battle = True
    else:
        print("Game Over. Better luck next time!")
    
    if continue_battle:
        hercules_hp, hercules_ap, hercules_win = Battle(enemy_hp, enemy_ap, hercules_ap, hercules_hp, attack_names, enemy_name="Hydra")
        if hercules_win:
            print('Congratulations, you have Defeated your Rivals! You are the Ultimate Champion!')
        else:
             print("Game Over. Better luck next time!")



#Attack Prompt
def prompt(hercules_hp, hercules_ap, attack_names, enemy_name, enemy_hp, enemy_ap):
    print(f'You are at {hercules_hp} Health and have an attack power of {hercules_ap}')
    print(f'{enemy_name} is at {enemy_hp} Health and has an attack power of {enemy_ap}\n')
    for i in range(len(attack_names)):
        print(f'Please type {i} if you would like to use {attack_names[i]}')
    selection = input("Please type your selection here: \n")
    return selection

#Player Attack Function
def attack(enemy_hp, hercules_ap, enemy_name):
    print(f"{enemy_name} is at {enemy_hp} health and you hit him for {hercules_ap} damage.\n")
    current_enemy_hp = max(0, enemy_hp - hercules_ap)
    print(f"{enemy_name} is now at {current_enemy_hp} health.\n")
    return current_enemy_hp

#Enemy Attack Function
def attackback(hercules_hp, enemy_ap, enemy_name):
    print(f"{enemy_name} hits you for {enemy_ap} damage.\n")
    your_current_hp = max(0, hercules_hp - enemy_ap)
    return your_current_hp

#Upgrade Function
def Uprgade(hercules_ap):
    print('After defeating your enemy, you feel a charge of light fill your body, roll the dice to see your fate.\n' )
    input('type Roll to Roll:')
    dice_roll = random.randint(0, 10) 
    print(f'You rolled a {dice_roll}')
    if dice_roll <5: print("no updgrade see ya next time!\n")
    if dice_roll >5: print("your attack has been increased!\n")
    if dice_roll >5: hercules_ap = hercules_ap* (1 + random.uniform(0, 0.5))
    return hercules_ap

#Battle Function
def Battle(enemy_hp, enemy_ap, hercules_ap, hercules_hp, attack_names, enemy_name):
        hercules_win = False
        enemy_win = False
        while enemy_hp > 0 and hercules_hp > 0:
            user_input = prompt(hercules_hp, hercules_ap, attack_names, enemy_name, enemy_hp, enemy_ap)
            
            if user_input in ["0", "1", "2", "3"]:
                print(f"You attack {enemy_name}!\n")
                enemy_hp = attack(enemy_hp, hercules_ap, enemy_name)
                
                if enemy_hp <= 0:
                    print(f"You have killed {enemy_name}!\n")
                    return hercules_hp, hercules_ap, True
                
                print(f'{enemy_name} attacks you back with {random.choice(attack_names)}\n')
                hercules_hp = attackback(hercules_hp, enemy_ap, enemy_name)
                
                if hercules_hp <= 0:
                    print("You have been defeated!")
                    return False
                
                print(f'Your Health: {hercules_hp}\n')
                print(f'{enemy_name} Health: {enemy_hp}\n')
            else:
                print("Invalid input. Please try again.")
    
RunGame()