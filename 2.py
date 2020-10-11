import pygame
from pygame.draw import *
import numpy as np

pygame.init()
#Common comment:
#Everywhere in the work were used multiplication on x_scale(y_scale) for 
#stable picture within changable propotions of the screen
#Original picture was drawn in formats, where length of the screen is 2 times higher than height of the screen 

FPS = 30
length_of_screen = 800
height_of_screen = 400
x_scale = length_of_screen / 800
y_scale = height_of_screen / 400
screen = pygame.display.set_mode((length_of_screen, height_of_screen))

#colors, which was in using
black = (0, 0, 0)
white = (255, 250, 250)
red = (255, 12, 0)
orange = (255, 107, 0)
blue = (4, 220, 254)
sky_color = (0, 254, 255)
grass_color = (0, 220, 12)
tree_green = (0, 145, 23)
purple = (254, 0, 255)#color of the sun

height_of_horizont = int(170 * y_scale)
screen.fill(sky_color)

#drawing of grass
rect(screen, grass_color, (0, height_of_horizont, length_of_screen, height_of_screen - height_of_horizont))

def draw_sun(x, y, x_Radius, y_Radius, number_of_rays):
    angle = np.pi * 2/ number_of_rays
    list_of_coordinates_internal = []
    list_of_coordinates_external = []
    #we are about to make sun by overlay of internal and external polygons
    k = 0
    for count in range(number_of_rays ):
        #searching coordinates for internal polygon
        internal_coordinates = []
        internal_coordinates.append(int(x + x_Radius * (np.cos(angle/ 2 + count * angle))))
                 
        internal_coordinates.append(int(y + y_Radius * (np.sin(angle/ 2 + count * angle))))
        #searching coordinates for external polygon
        external_coordinates = []
        external_coordinates.append(int(x + x_Radius * (np.cos(count * angle))))
        external_coordinates.append(int(y + y_Radius * (np.sin(count * angle))))
        #addition of found coordinates in lists
        list_of_coordinates_internal.append(internal_coordinates)
        list_of_coordinates_external.append(external_coordinates)                                                    
    #drawing internal and external polygons    
    polygon(screen, purple, list_of_coordinates_internal)
    polygon(screen, black, list_of_coordinates_internal, 1)
    
    polygon(screen, purple, list_of_coordinates_external)
    polygon(screen, black, list_of_coordinates_external, 1)                                                                                       
    
def draw_house(width_of_house, height_of_roof_n_house, x, y, width_of_window, height_of_window):
    #x & y are coordinates of the higher left corner of the main part of the house
    #main part of the house
    rect(screen, orange , (x, y, width_of_house, height_of_roof_n_house))

    #black line near main building
    rect(screen, black, (x, y, width_of_house + 1, height_of_roof_n_house + 1), 1)
    
    #window
    x_window = x + int((width_of_house - width_of_window) / 2)
    y_window = int(y + (height_of_roof_n_house - height_of_window)/ 2)
    rect(screen, blue, [x_window, y_window, width_of_window, height_of_window])
    
    #roof
    x_center_of_house = int(x + width_of_house/ 2)
    peak_of_roof = int(y - height_of_roof_n_house/ 2)
    polygon(screen, red, [(x, y), (x_center_of_house, peak_of_roof), (x + width_of_house, y)])
    
    #black line near roof
    polygon(screen, black, [(x,y), (x_center_of_house, peak_of_roof), (x + width_of_house, y)], 1)

def draw_tree(x, y, width_of_tree_trunk, height_of_tree_trunk, x0, y0, Rx, Ry):
    #Rx - x_radius of ellipse, Ry - y_radius of ellipse
    #drawing trunk
    rect(screen, black, [x, y, width_of_tree_trunk, height_of_tree_trunk])
    
    #drawing foliage
    number_of_ellipses = 5
    angle_beetwen_ellipses = 2 * np.pi / number_of_ellipses
    count = 0
    #x_ellipse & y_ellipse are for coordinates of left high corner of rectangle, where ellipse(branch) is plased 
    for count in range(number_of_ellipses):
        x_ellipse = int(x0 + Rx * (np.cos(count * angle_beetwen_ellipses))) - Rx
        y_ellipse = int(y0 + Ry * (np.sin(angle_beetwen_ellipses/ 2 + count * angle_beetwen_ellipses))) - Ry
        ellipse(screen, tree_green, (x_ellipse, y_ellipse , 2 * Rx, 2 * Ry)) 
        ellipse(screen, black, (x_ellipse - 1, y_ellipse - 1, 2 * Rx + 2, 2 * Ry + 2), 2) 
                   

def draw_clouds(x, y, x_radius_for_cloud, y_radius_for_cloud):
    
    #x & y are coordinates of the left high corner of rectangle where first(from the left) ellipse of the low raw is lying 
    x0 = x #saving given coordinate
    number_of_circle = 0
    
    #drawing low raw with black lines
    count_low = 4 #number of circles in the low raw
    for number_of_circle in range(count_low):
        ellipse(screen, black,(x - 2 , y - 2,  2 * x_radius_for_cloud + 4, 2 * y_radius_for_cloud + 4), 2)
        ellipse(screen, white,(x, y, 2 * x_radius_for_cloud, 2 * y_radius_for_cloud))
        x += x_radius_for_cloud
    
    x = x0
    count_high = 2 #number of circles in the high raw
    #drawing high raw with black lines
    for number_of_circle in range(count_high):
        ellipse(screen, black,(x + x_radius_for_cloud - 2, y - y_radius_for_cloud - 2,  2 * x_radius_for_cloud + 4, 2 * y_radius_for_cloud + 4), 2)
        ellipse(screen, white,(x + x_radius_for_cloud, y - y_radius_for_cloud, 2 * x_radius_for_cloud, 2 * y_radius_for_cloud))
        x += x_radius_for_cloud

#Drawing sun
#x & y coordinates are for center of the sun
x_coordinate_for_the_sun = 80 * x_scale
y_coordinate_for_the_sun = 44 * y_scale
x_radius_of_the_sun = 42 * x_scale
y_radius_of_the_sun = 42 * y_scale
number_of_rays_in_sun = 10 
draw_sun(x_coordinate_for_the_sun, y_coordinate_for_the_sun, x_radius_of_the_sun, y_radius_of_the_sun, number_of_rays_in_sun)

#Drawing house
height_of_main_part_big_house = int(130 * y_scale)
width_of_big_house = int(200 * x_scale)
height_of_window_big_house = int(y_scale * 60)
width_of_window_big_house = int(50 * x_scale)
#Coordinates below are the coordinates of the higher left corner of the main part of the house
x_coordinates_big_house = int(70 * x_scale)
x_coordinates_small_house = int(500 * x_scale)
y_coordinates_big_house = int(180 * y_scale)
y_coordinates_small_house = int(150 * y_scale)
draw_house(width_of_big_house, height_of_main_part_big_house, x_coordinates_big_house, y_coordinates_big_house, width_of_window_big_house, height_of_window_big_house)
draw_house(int(width_of_big_house / 2), int(height_of_main_part_big_house / 2), x_coordinates_small_house, y_coordinates_small_house, int(width_of_window_big_house / 2), int(height_of_window_big_house / 2))

#Drawing trees
#x_trunk & y_trunk are for coordinates of high left corner of the tree's trunk
x_trunk1 = int(380 * x_scale)
x_trunk2 = int(650 * x_scale)
y_trunk1 = int(185 * y_scale)
y_trunk2 = int(160 * y_scale)
width_trunk1 = int(16 * x_scale)
width_trunk2 = int(10 * x_scale)
length_of_trunk1 = int(110 * y_scale)
length_of_trunk2 = int(55 * y_scale)
x_center_of_foliage1 = int(388 * x_scale)
x_center_of_foliage2 = int(655 * x_scale)
y_center_of_foliage1 = int(155 * y_scale)
y_center_of_foliage2 = int(140 * y_scale)
x_Radius_of_branch1 = int(25 * x_scale)
y_Radius_of_branch1 = int(25 * y_scale)
x_Radius_of_branch2 = int(15 * x_scale)
y_Radius_of_branch2 = int(15 * y_scale)
draw_tree(x_trunk1, y_trunk1, width_trunk1, length_of_trunk1, x_center_of_foliage1, y_center_of_foliage1, x_Radius_of_branch1, y_Radius_of_branch1)
draw_tree(x_trunk2, y_trunk2, width_trunk2, length_of_trunk2, x_center_of_foliage2, y_center_of_foliage2, x_Radius_of_branch2, y_Radius_of_branch2)
   

#Drawing clouds
#Coordinates below are coordinates of the left high corner of rectangle where first(from the left) ellipse of the low raw is lying 
x_cloud1 = int(160 * x_scale)
x_cloud2 = int(400 * x_scale)
x_cloud3 = int(600 * x_scale)
y_cloud1 = int(40 * y_scale)
y_cloud2 = int(65 * y_scale)
y_cloud3 = int(35 * y_scale)
#You can put ellipse-based cloudes insted circle-based by changing propotions of x-y radiuses
x_cloud_radius1 = int(30 * x_scale)
x_cloud_radius2 = int(20 * x_scale)
x_cloud_radius3 = int(35 * x_scale)
y_cloud_radius1 = int(30 * y_scale)
y_cloud_radius2 = int(20 * y_scale)
y_cloud_radius3 = int(35 * y_scale)
draw_clouds(x_cloud1, y_cloud1, x_cloud_radius1, y_cloud_radius1)
draw_clouds(x_cloud2, y_cloud2, x_cloud_radius2, y_cloud_radius2)
draw_clouds(x_cloud3, y_cloud3, x_cloud_radius3, y_cloud_radius3) 


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

