import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

class Mob(object):
  def __init__(self, world, coordinates, distance):
    self.world = world
    [x, y, z] = coordinates
    self.coordinates = [x + distance, y, z + distance]
    self.material = block.STONE
    self.scan_range = 5

    random.seed()
    self.draw(self.coordinates, self.material)
  
  def clear(self):
   self.draw(self.coordinates, block.AIR) 

  def collision_detection(self):
    return None
  
  def draw(self, coordinates, material):
    [x,y,z] = coordinates
    height = 3
    distance = 3

    for level in range(0, height):
      self.world.setBlock( x, y + level, z, material) 

  def follow(self, coordinates):
    self.world.postToChat("Following")
    self.go_to(coordinates) 

  def get_sign(self, number):
    result = 1

    if number < 0:
      result = -1

    return result

  def go_to(self, coordinates):
    [x, y, z] = self.coordinates
    [dest_x, dest_y, dest_z] = coordinates 
  
    self.world.postToChat("x: " + str(dest_x) + " z:" + str(dest_z))
    self.move("x", int(dest_x - x)) 

    [x, y, z] = self.coordinates
    self.move("z", int(dest_z - z)) 

  # the method that will look for the player
  def look(self):
    [found, player] = self.scan()
    if found:
      self.follow(player)
    else:
      self.wander()
 
  def move(self, direction, steps):
    sign = self.get_sign(steps)

    for i in range(0, abs(steps)):
      self.turn(direction, sign)
    
  def turn(self, direction, sign):
      self.clear()
      self.update(direction, (sign * 1))
      self.draw(self.coordinates, self.material)
      self.collision_detection() 
      time.sleep(0.2)

  def random_position(self):
    [x, y, z] = self.coordinates
    destination_x = random.randint(int(x - self.scan_range), int(x + self.scan_range)) 
    destination_z = random.randint(int(z - self.scan_range), int(z + self.scan_range)) 

    return [destination_x, y, destination_z]

  def scan(self):
    found = False
    coordinates = []
    [x, y, z] = self.world.player.getPos()

    if self.within_range(x, z):
      found = True
      coordinates = [x, y, z]

    return [found, coordinates]

  def update(self, direction, step):
    [x, y, z] = self.coordinates
    position = [] 
    
    #self.world.postToChat("step is : " + str(step) )
    if direction == "x":
       position = [x + step, y, z] 
    elif direction == "z":
       position = [x, y, z + step] 

    self.coordinates = position
  
  def wander(self):
    self.world.postToChat("Wandering")
    destination = self.random_position()
    self.go_to(destination) 
 
  # there was a bug in the previous version
  # this version fixes the bug
  def within_range(self, player_x, player_z):
    result = False
    [x, y, z] = self.coordinates 
    if (player_x > (x - self.scan_range) and player_x < (x + self.scan_range)) and  (player_z > (z - self.scan_range) and player_z < (z + self.scan_range)):
      result = True

    return result
