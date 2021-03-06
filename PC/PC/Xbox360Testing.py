#!/usr/bin/env python
# Written by alex@nyrpnz.com March 14 2012
"Event echoer in Pygame."
 
import pygame
from pygame.locals import *
 
def main():
        "Opens a window and prints events to the terminal. Closes on ESC or QUIT."
        pygame.init()
        screen = pygame.display.set_mode((40, 40))
        pygame.display.set_caption("JOYTEST")
        clock = pygame.time.Clock()
        joysticks = []
        for i in range(0, pygame.joystick.get_count()):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[-1].init()
                print ("Detected joystick '",joysticks[-1].get_name(),"'")
        while 1:
                clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                print ("Received event 'Quit', exiting.")
                                pygame.display.quit()
                                return
                        elif event.type == KEYDOWN and event.key == K_ESCAPE:
                                print ("Escape key pressed, exiting.")
                                pygame.display.quit()
                                return
                        elif event.type == KEYDOWN:
                                print ("Keydown,",event.key)
                        elif event.type == KEYUP:
                                print ("Keyup,",event.key)
                        #elif event.type == MOUSEMOTION:
                         #       print "Mouse movement detected."
                        elif event.type == MOUSEBUTTONDOWN:
                                print ("Mouse button",event.button,"down at",pygame.mouse.get_pos())
                        elif event.type == MOUSEBUTTONUP:
                                print ("Mouse button",event.button,"up at",pygame.mouse.get_pos())
                        elif event.type == JOYAXISMOTION:
                                
                                print ("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")
                                print ("direction", ("%.3f" % event.value ))
                        elif event.type == JOYBUTTONDOWN:
                                print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")
                        elif event.type == JOYBUTTONUP:
                                print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"up.")
                        elif event.type == JOYHATMOTION:
                                print ("Joystick '",joysticks[event.joy].get_name(),"' hat",event.hat," moved.")
                                if event.value == (1,0):
                                        print ("right (1,0)")
                                if event.value == (-1,0):
                                        print ("left (-1,0)")
                                if event.value == (0,-1):
                                        print ("down (0,-1)")
                                if event.value == (0,1):
                                        print ("up (0,1)")
if __name__ == "__main__":
        main()
