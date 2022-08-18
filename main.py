import random


def RunGame():
    hercules_hp = 100
    hercules_ap = 25
    enemy_hp = 100
    enemy_ap = 15
    user_input = prompt()
    if user_input == "1" or "2" or "3" or "0":
        enemy_dead = False
        print("You attack the Raid Boss!")
        current_enemy_hp = attack(enemy_hp)
        print(f'they enemy attacks you back with {random.choice(attack_names)}')
        your_current_hp = attackback(hercules_hp)
        while enemy_dead == False:
            print(f'Raid Boss Health:{current_enemy_hp}')
            if current_enemy_hp != 0:
             current_enemy_hp = attack(current_enemy_hp)
             print(f'they enemy attacks you back with {random.choice(attack_names)}')
             your_current_hp = attackback(your_current_hp)
             print(f'Your Health:{your_current_hp}')
            else:
             print("you have killed the enemy")
             enemy_dead = True
            
attack_names = ['Sword Slash', 'Shield Bash', "Lunge", "Slide"]
print("""You are Hercules a hero that is being monitored by a highly powerful organization, you have no choice but to obey every living second.
That is until you don't, you are then captured and in route to be killed. You manage to escape and realize you're inside the enemy base,
face to face with the leader of the orgazination""")
def prompt(hercules_hp, hercules_ap):
    print(f'You are at {hercules_hp} Health and have an attack power of {hercules_ap}')
    for attack in range(len(attack_names)):
        print(f'Please type {attack} if you would like to {attack_names[attack]}')
    selection = input("Please type your selection here:")
    return selection
def attack(enemy_hp,hercules_ap,):
    print(f"The enemy is at {enemy_hp} health and you hit him for {hercules_ap} damage")
    current_enemy_hp = enemy_hp - hercules_ap
    print(f" The enemy is now at {current_enemy_hp} health")
    return current_enemy_hp
def attackback(hercules_hp,enemy_ap):
    your_current_hp = hercules_hp - enemy_ap
    return your_current_hp
    
        
RunGame()