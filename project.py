import re
import argparse
import random
from classes import Player, Bandit, Owlbear

def main():
    #use argparser to make the argument for number of monsters.
    #create monsters based on what the argument is
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="type of monster", type=str)
    parser.add_argument("number", help="number of monsters", type=int)
    args = parser.parse_args()
    enemies = []
    i = 0
    while i < args.number:
        match args.type:
            case "bandit"|"Bandit":
                enemies.append(Bandit())
            case "owlbear"|"Owlbear":
                enemies.append(Owlbear())
        i+=1
    battle_sim(enemies, generate_players())

def generate_players():
    players = []

    while True:
        try:
            player = Player.get()
        except ValueError:
            print("The required format is \"name armor_class hp\"")
        except EOFError:
            print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
        else:
            players.append(player)

    return players




def death_saves(player):
    print(f"{player.name} is going into death saves!")
    saves = ""
    fails = ""
    counter = 0
    i = 0
    while i < 3:
        roll = int(input("roll: "))
        if roll > 20 or roll < 1:
            print("roll must be between 1 and 20")
            continue
        if roll > 10:
            saves += "🟢"
            counter += 1
            i+=1
            print(saves + fails)
        elif roll <= 10:
            fails += "🔴"
            i+=1
            print(saves + fails)
    return counter

def save_outcome(player, counter):
    if counter >=2:
        health = player.heal()
        print(f"{player.name} has been healed to {health} hit points")
        print("")
        return 0
    else:
        print(f"{player.name} is dead :(")
        print("")
        player.is_alive = False
        return player.is_alive


def battle_sim(enemy_list: list[Bandit], player_list: list[Player]):
    #while enemy_list not empty keep doing this
    while enemy_list:
        for enemy in enemy_list:
            if not enemy.is_alive:
                enemy_list[:] = [enemy for enemy in enemy_list if not enemy.hp <= 0]
            else:
                player_choice = random.choice(player_list)
                enemy.attack(player_choice)
                if player_choice.hp <= 0:
                    save_outcome(player_choice, death_saves(player_choice))
                    if not player_choice.is_alive:
                        player_list[:] = [player for player in player_list if not player.hp <= 0]
        print("")
        for player in player_list:
            for count, enemy in enumerate(enemy_list, 1):
                print (count, enemy)
            print(f"")
            while True:
                try:
                    enemy_index = int(input(f"Which enemy would {player.name} like to attack? "))
                    enemy_choice = enemy_list[enemy_index-1]
                except (IndexError, ValueError):
                    pass
                else:
                    break
            player.attack(enemy_choice)
            if not enemy_choice.is_alive:
                enemy_list[:] = [enemy for enemy in enemy_list if not enemy.hp <= 0]
            print("")





if __name__ == "__main__":
    main()

