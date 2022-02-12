#from cmath import atan
#from curses.ascii import SP
import random
player_life = 100
player_sp = 50

enemy_power = 50

enemies = []


number_of_enemies = int(input("Type the number of enemies you want: "))

for i in range(number_of_enemies):
    enemies.append([i+1, enemy_power])


game = True

while game:
    print('******* ATACK OR CURE ******')
    print('Player_life = {}'.format(player_life))
    print('SP = {}'.format(player_sp))

    attack = int(input('An enemy just found you. Do you want to attack(1) or Cure (2): '))

    if attack == 1:
        selected = random.choice(enemies)

        dano = random.randint(10, 15)

        print('You have caused {} of damage to the enemy {}'.format(dano, selected[0]))

        selected[1] -= dano
    
        if selected[1] <= 0:
            print('The enemy {} have died'.format(selected[0]))

            enemies.remove(selected)

    else:
        #voce escolheu se curar

        if player_sp >= 10:
            cure = random.randint(10, 15)

            print('You just received {} of life'.format(cure))

            player_life += cure
        else:
            print('SP insufficient')
    

    #vez dos inimigos


    for enemy in enemies:
        acertou = bool(random.choice([1, 1, 1, 0]))


        if acertou:
            enemy_damage = random.randint(5, 10)

            print('Enemy {} has caused {} of damage'.format(enemy[0], enemy_damage))

            player_life -= enemy_damage

        else:
            print('O inimigo {} errou'.format(enemy[0]))

    if player_life < 100:
        player_life += 3

    
    if player_life > 100:
        player_life = 100

    if player_life <= 0:
        print('Player has died')
        game = False

        
        





