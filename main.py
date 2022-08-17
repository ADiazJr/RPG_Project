hercules_hp = 100
hercules_ap = 25
enemy_hp = 100
enemy_ap = 15
attack_names = ['Sword Slash', 'Shield Bash', "Lunge", "Slide"]
print("""You are Hercules a hero that is being monitored by a highly powerful organization, you have no choice but to obey every living second.
That is until you don't, you are then captured and in route to be killed. You manage to escape and realize you're inside the enemy base,
face to face with the leader of the orgazination""")
def prompt():
    print(f'You are at {hercules_hp} Health and have an attack power of {hercules_ap}')
    for attack in range(len(attack_names)):
        print(f'Please type {attack} if you would like to {attack_names[attack]}')

prompt()