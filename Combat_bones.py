"""Ash Thom RPG Combat Demo
This file plays the beginnings of what will be the combat system for my final project.
 It is a turn-based combat against the computer."""


import pygame, sys
from pygame.locals import *
import random


def main():

    class Character:
        # Parent class to be used in making future classes
        def __init__(self, health: int, damage: int, name):
            self.health = health
            self.damage = damage
            self.name = name
            self.dodge = False

        def deal_damage(self,target):

            # Has character attack enemy and reduce their hp
            # target parameter must be manually set each attack
            # because I couldn't figure out the syntax to make it work otherwise

            print(str(self.name)+" attacks wildly!")

            current_attack = self.damage + random.randint(0, 10)
            if target.dodge == False:
                target.health = target.health - current_attack

                print(str(self.name) + ' attacks for ' + str(current_attack) + '!')

                print(str(target.name) + ' is left with ' + str(target.health) + ' hp!')
            else:
                print(str(target.name) + ' dodged gracefully, like a scared raccoon.')
                target.dodge = False

        def heal_damage(self):
            # Has character heal wounds
            print(str(self.name)+ "bandages their wounds")
            current_heal = 15 + random.randint(0,10)
            self.health = current_heal + self.health
            if self.health > 200:
                self.health = 200
            print(str(self.name)+' managed to heal for ' + str(current_heal) + 'hp and now has ' + str(self.health) + ' Health!')

        def dodge_damage(self):
            # Has the character roll the dice to avoid damage entirely
            print(str(self.name)+ ' attempts to dodge the next attack')
            dodge_success = random.randint(0,1)
            if dodge_success == 0:
                self.dodge = True
                print(str(self.name) + ' feels ready for whatever your opponent tries.')
            else:
                self.dodge = False
                print(str(self.name) + ' trips over their shoelaces and lands on their face while trying to look cool.')

    player = Character(200, 25, input("Enter your name: "))
    comp = Character(200, 25, "Enemy" )
    # This decides who goes first. Will likely be changed in the future to be more predictable.
    turn = random.randint(0, 1)
    if turn == 0:
        player_turn = True
    elif turn == 1:
        player_turn = False
    while player.health > 0 and comp.health > 0:
        # This is the main combat loop. It persists until either side has won.

        if player_turn == True:

            print('It is your turn! Enter 1 to attack, 2 to heal, or 3 to dodge!')
            player_move = input("Enter action:")
            if player_move == '1':
                player.deal_damage(comp)
            elif player_move == '2':
                player.heal_damage()
            elif player_move == '3':
                player.dodge_damage()
            else:
                print('Please enter one of the options')
                continue
            player_turn = False
            continue
        if player_turn == False:
            print("it is your enemy's turn!")
            if comp.health <50 and comp.health > 0:
                temp_var = random.randint(0,4)
                if temp_var == 0:
                    comp.dodge_damage()
                else:
                    comp.heal_damage()

            elif comp.health >= 50 and comp.health < 100:
                comp.deal_damage(player)
            elif comp.health >= 100 and comp.health < 175:
                temp_var2 = random.randint(0,1)
                if temp_var2 == 0:
                    comp.deal_damage(player)
                else:
                    comp.dodge_damage()
            elif comp.health >=175:
                comp.deal_damage(player)
            player_turn = True


main()