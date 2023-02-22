import pyglet as pg
from pyglet import shapes
from pyglet.window import key
import math

# I'm using a global variable because if i didn't I would have to pass variables through around 3-4 functions
global camera_x
global camera_y
global player_x
global player_y
global pressed_keys
global enemy_x
global enemy_y

camera_x = 5
camera_y = 5
player_x = 3
player_y = 3
enemy_x = 3
enemy_y = 3
pressed_keys = {
  key.UP: False,
  key.DOWN: False,
  key.LEFT: False,
  key.RIGHT: False
}


# 0 = grey (wall)
# 1 = blue
# 2 = green
# 3 = red
# 4 = pink
map = [
  [3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 3]
]

test_map = [
  [3, 1, 1, 3, 1, 1, 3, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 2, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 2, 1, 1, 2, 1, 1, 3],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [3, 1, 1, 3, 1, 1, 3, 1, 1, 3]
]

# the map that is seen
on_screen = []


# def wall_collision(x, y, movement, direction, ratio):
#   next_block = None
#   try:
#     if direction == "UP":
#       next_block = test_map[math.floor(y) - 1][math.floor(x) - 1]

#     elif direction == "DOWN":
#       next_block = test_map[math.floor(y) + 1][math.floor(x)]

#     elif direction == "LEFT":
#       next_block = test_map[math.floor(y)][math.floor(x) - 1]
    
#     elif direction == "RIGHT":
#       next_block = test_map[math.floor(y)][math.floor(x) + 1]
#   except IndexError:
#     pass
#   if next_block == 0:
#     return True 

# creates a square object on the x/y coordinates, color_type determines the color
def draw_square(x, y, color_type, size=50):
  if color_type == 0: #grey
    color = (200, 200, 200)
  elif color_type == 1: #blue
    color = (55, 55, 255)
  elif color_type == 2: #green
    color = (55, 255, 55)
  elif color_type == 3: #red
    color = (255, 55, 55)
  elif color_type == 4: #pink
    color = (255, 50, 255)

  return shapes.Rectangle(x, y, size, size, color=color, batch=batch)

# renders the map based off of the camera x/y coordinates and the fov of the camera
def load_map(center_x, center_y, diameter, map, ratio):
  radius = int((diameter - 1) / 2) + 1
  center_x_after_decimal = center_x - math.floor(center_x)
  center_y_after_decimal = center_y - math.floor(center_y)
  starting_x = math.floor(center_x) - radius
  starting_y = math.floor(center_y) - radius
  ending_x = starting_x + diameter + 1
  ending_y = starting_y + diameter + 1
  
  # this is the rendering loop
  for y in range(starting_y + 1, ending_y + 1):
    for x in range(starting_x + 1, ending_x + 1):
      ratio = HEIGHT / diameter
      x_cor = (x - 1 - starting_x - center_x_after_decimal) * ratio
      y_cor = HEIGHT - ((y - starting_y - center_y_after_decimal) * ratio)
      try:
        temp = draw_square(x_cor, y_cor, map[y][x], size=ratio)
      except IndexError:
        temp = draw_square(x_cor, y_cor, 1, size=ratio)
      on_screen.append(temp)
  return starting_x, starting_y, ending_x, ending_y


#diameter must be odd
def render_screen(center_x, center_y, diameter, map):
  ratio = HEIGHT/diameter
  starting_x, starting_y, ending_x, ending_y = load_map(center_x, center_y, diameter, map, ratio)
  # if enemy_x > starting_x and enemy_x < ending_x and enemy_y > starting_y and enemy_y < ending_y:
  #   enemy = draw_enemy(center_x, center_y, diameter)
  #   on_screen.append(enemy)
  player = draw_player((player_x + 0.5) * ratio, HEIGHT - ((player_y + 0.5) * ratio))
  on_screen.append(player)

#draws the player 
def draw_player(x, y):
  return shapes.Circle(x, y, 12.5, color=(255, 255, 255), batch=batch)


def draw_enemy(center_x, center_y, diameter):
  ratio = HEIGHT / diameter
  relative_x = enemy_x - center_x + 3
  relative_y = enemy_y - center_y + 3
  x = relative_x * ratio
  y = HEIGHT - (relative_y * ratio)
  return shapes.Circle(x, y, 25, color=(255, 55, 55), batch=batch)



#player must be loaded after the map
#enemy must be loaded after the map
WIDTH, HEIGHT = 500, 500
window = pg.window.Window(width=WIDTH, height=HEIGHT)
batch = pg.graphics.Batch()
DIAMETER = 7

for y in range(len(map)):
  for x in range(len(map[y])):
    if map[y][x] == 4:
      camera_x, camera_y = x, y
      break

render_screen(camera_x, camera_y, DIAMETER, map)

def up_logic(camera_y, player_y, movement, radius, ratio):
  #checks to see if the fov is at the top end
  if camera_y - radius > 0.1 and player_y <= 3:
    player_y = 3
    camera_y -= movement
  elif player_y > 0:
    player_y -= movement
  return camera_y, player_y

def down_logic(camera_y, player_y, movement, radius, ratio):
  #checks to see if the fov is at the bottom end
  if camera_y + radius + movement < len(map) - 1 and player_y >= 3:
    player_y = 3
    camera_y += movement
  elif player_y + movement < DIAMETER - 0.7:
    player_y += movement
  return camera_y, player_y

def left_logic(camera_x, player_x, movement, radius, ratio):
  #checks to see if the fov is at the left end
  if camera_x - radius > 0.1 and player_x <= 3:
    player_x = 3
    camera_x -= movement
  elif player_x > 0:
    player_x -= movement
  return camera_x, player_x

def right_logic(camera_x, player_x, movement, radius, ratio):
  #checks to see if the fov is at the right end
  if camera_x + radius + movement < len(map[0]) - 1 and player_x >= 3:
    player_x = 3
    camera_x += movement
  elif player_x + movement < DIAMETER - 0.7:
    player_x += movement
  return camera_x, player_x

#movement logic
@window.event
def on_text_motion(motion):
  global camera_x
  global camera_y
  global player_x
  global player_y
  global pressed_keys
  radius = int((DIAMETER - 1) / 2)
  movement = 0.05
  pressed_keys[motion] = True
  ratio = HEIGHT/DIAMETER
  for motion in pressed_keys:
    if pressed_keys[key.UP]:
      camera_y, player_y = up_logic(camera_y, player_y, movement, radius, ratio)

    if pressed_keys[key.DOWN]:
      camera_y, player_y = down_logic(camera_y, player_y, movement, radius, ratio)
      
    if pressed_keys[key.LEFT]:
      camera_x, player_x = left_logic(camera_x, player_x, movement, radius, ratio)

    if pressed_keys[key.RIGHT]:
      camera_x, player_x = right_logic(camera_x, player_x, movement, radius, ratio)

  window.clear()
  render_screen(camera_x, camera_y, DIAMETER, map)

@window.event
def on_key_release(symbol, modifiers):
  global pressed_keys
  pressed_keys[symbol] = False

@window.event
def on_draw():
  window.clear()
  batch.draw()
  on_screen = []

pg.app.run()