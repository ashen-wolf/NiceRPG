"""Ash Thom RPG Combat Demo
This file plays the beginnings of what will be the combat system for my final project.
 It is a turn-based combat against the computer."""


import pygame, sys, random, time
from pygame.locals import *

forest = pygame.image.load('Background Image.jpg')
hell = pygame.image.load("Background Hell.jpg")
enemy_crow = pygame.image.load("crow.png")
player_bird = pygame.image.load("the green bird.png")

window_length = 1280
window_height = 800

display_window = pygame.display.set_mode((window_length, window_height), 0, 32)

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.init()


class Background:
    # The class used to draw the background
    def __init__(self, scene):

        pygame.display.set_caption("Nice RPG")
        self.scene = scene

    def draw_background(self):

        if self.scene == "forest":
            # Calls the background planned for level 1
            display_window.blit(forest, (0, 0))

        elif self.scene == "hell":
            # Calls the scene planned for level 2
            display_window.blit(hell, (0, 0))

        # The functions to draw the characters on screen
        display_window.blit(player_bird, (window_length / 6, window_height / 4))
        display_window.blit(enemy_crow, ((window_length / 4) * 2, window_height / 4))
        health_display(red, player)
        health_display(red, comp)
        # Function to draw the box for text to appear in
        pygame.draw.rect(display_window, black, (0, (window_height / 6) * 5, window_length, (window_height / 6) + 1))
        # Re-draws the screen
        pygame.display.update()
        # does something important idk all the tutorials had it
        clock.tick(60)


class Character:
    # Parent class to be used in making future classes
    def __init__(self, health: int, damage: int, name):
        self.health = health
        self.damage = damage
        self.name = name
        self.dodge = False

    def deal_damage(self, target):

        # Has character attack enemy and reduce their hp
        # target parameter must be manually set each attack
        # because I couldn't figure out the syntax to make it work otherwise

        message_display(str(self.name) + " attacks wildly!")

        current_attack = self.damage + random.randint(0, 20)
        if not target.dodge:
            target.health = target.health - current_attack

            if target.health < 0:
                target.health = 0

            message_display(str(target.name) + ' is left with ' + str(target.health) + ' hp!')

        else:
            message_display(str(target.name) + ' dodged gracefully')
            target.dodge = False

    def heal_damage(self):
        # Has character heal wounds
        if self.health != 0:
            message_display(str(self.name) + "bandages their wounds")
            current_heal = 15 + random.randint(0, 10)
            self.health = current_heal + self.health
            if self.health > 200:
                self.health = 200
            message_display(str(self.name) + ' managed to heal for ' + str(current_heal) + 'hp')

    def dodge_damage(self):
        # Has the character roll the dice to avoid damage entirely
        message_display(str(self.name) + ' attempts to dodge the next attack')
        dodge_success = random.randint(0, 3)
        if dodge_success == 0:
            self.dodge = True
            message_display(str(self.name) + ' feels ready for anything.')
        else:
            self.dodge = False
            message_display(str(self.name) + """ trips over a rock clumsily """)
            message_display('...')
            message_display('A flying rock')
            level1.draw_background()


def text_objects(text, font, color=white):
    textSurface = font.render(text, False, color)
    return textSurface, textSurface.get_rect()


def health_display(color, instance):
    health = str(instance.health) + 'hp'
    font = pygame.font.Font('freesansbold.ttf', 50)
    HealthSurf, HealthRect = text_objects(health, font, color)
    if instance == player:
        HealthRect.center = ((window_length/6), (window_height/4))
    else:
        HealthRect.center = ((window_length/6)*5, (window_height/4))
    display_window.blit(HealthSurf, HealthRect)


def message_display(text, delay=1.5, color=white):
    message = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, message, color)
    TextRect.center = ((window_length / 2), (window_height / 9) * 8)
    display_window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(delay)
    level1.draw_background()


player = Character(200, 25, 'Good Bird ')
comp = Character(200, 25, "Mean Crow ")
level1 = Background('forest')


def main():

    # This decides who goes first. Will likely be changed in the future to be more predictable.
    close = False
    turn = random.randint(0, 1)
    if turn == 0:
        playerturn = True
    else:
        playerturn = False
    level1.draw_background()
    while not close:
        # This is the main combat loop. It persists until either side has won.
        level1.draw_background()
        if playerturn:
            player_move = None
            message_display('It is your turn!', 1)
            message_display('a to attack, s to heal, d to dodge, q to quit', 1.5)
            for event in pygame.event.get():
                # This is the event handler. It decides what happens when the user gives input.
                if event == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == ord("a"):
                        player_move = '1'
                    elif event.key == ord("s"):
                        player_move = '2'
                    elif event.key == ord("d"):
                        player_move = '3'
                    elif event.key == ord("q"):
                        message_display('Goodbye!')
                        pygame.quit()
                        sys.exit()

                    else:

                        continue

            if player_move == '1':
                player.deal_damage(comp)
            elif player_move == '2':
                player.heal_damage()
            elif player_move == '3':
                player.dodge_damage()
            else:
                continue

            playerturn = False
            continue
        if not playerturn:
            message_display("It is your enemy's turn!")

            if 0 < comp.health > 50:
                tempvar = random.randint(0, 4)
                if tempvar == 0:
                    comp.dodge_damage()
                else:
                    comp.heal_damage()
            elif comp.health >= 50 and comp.health < 100:
                comp.deal_damage(player)
            elif comp.health >= 100 and comp.health < 175:
                tempvar2 = random.randint(0, 1)
                if tempvar2 == 0:
                    comp.deal_damage(player)
                else:
                    comp.dodge_damage()

            elif comp.health >= 175:
                comp.deal_damage(player)
            else:
                comp.heal_damage()

            playerturn = True
        if comp.health == 0:
            if level1.scene == 'forest':
                level1.scene = 'hell'
                message_display('You Won! On to level 2')
                comp.health = 200
                player.health = 200
                main()
            else:
                message_display('You beat the game! Congrats u nerd')
                pygame.quit()
                sys.exit()
        elif player.health <= 0:
            if level1.scene == 'forest':
                message_display('You feel faint and fall into the trees below')


main()