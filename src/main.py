import serial
import keyboard
import time
import pygame
import sys

#&&&&&&&&&&&&&&&&& Arduino Code &&&&&&&&&&&&&&&&&&&&
x_value = 0 #? ranges from -100 to 100
y_value = 0 #? ranges from -94 to 100
button_pressed = False
x_button = 0
square_button = 0
triangle_button = 0
circle_button = 0
serial_port = 'COM7'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
values_list = []

# while True:
#     line = ser.readline().decode("utf-8").strip() #? Gets the data
#     if line:
#         values = line.split(":")
#         number_values = int(values[1].strip())
#         values_list.append(number_values)
#         if len(values_list) == 7:
#             x_value = values_list[0]
#             y_value = values_list[1]
#             button_pressed = values_list[2]
#             x_button = values_list[3]
#             square_button = values_list[4]
#             triangle_button = values_list[5]
#             circle_button = values_list[6]
#             values_list = []
        
#         # time.sleep(.5)
        
        
#     #~ # Exit the loop by pressing the space key
#     if keyboard.is_pressed("space"):
#         print("Space key pressed. Exiting the loop.")
#         break


#&&&&&&&&&&&&&&&&& Pygame &&&&&&&&&&&&&&&&&&&&
screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong with Arduino")

character = pygame.image.load("images/character.png")
character_width = 50
character_height = 50
character = pygame.transform.scale(character, (character_width, character_height))
character_rect = character.get_rect()
character_rect.center = (screen_width // 2, screen_height // 2)



movement_speed = 25
running = True
while running:
    
    line = ser.readline().decode("utf-8").strip() #? Gets the data
    if line:
        values = line.split(":")
        number_values = float(values[1].strip())
        values_list.append(number_values)
        if len(values_list) == 7:
            x_value = values_list[0]
            y_value = values_list[1]
            button_pressed = values_list[2]
            x_button = values_list[3]
            square_button = values_list[4]
            triangle_button = values_list[5]
            circle_button = values_list[6]
            values_list = []
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    x_movement = float(x_value * movement_speed)/screen_width
    y_movement = float(y_value * movement_speed)/screen_height
    
    # character_rect.x += x_value//screen_width
    # character_rect.y += y_value//screen_height
    
    character_rect.x += x_movement
    character_rect.y += y_movement
    
    # Keep the character within the screen bounds
    character_rect.x = max(0, min(character_rect.x, screen_width - character_width))
    character_rect.y = max(0, min(character_rect.y, screen_height - character_height))
        
    screen.fill((255, 255, 255))
    screen.blit(character, character_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
