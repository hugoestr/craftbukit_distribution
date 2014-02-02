# Our scanning version of the mob
# Our code got so big that it was hard to see what was 
# happening clearly, so now we create a seperate class

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

class Mob():
  def __init__(self, world, coordinates, distance):
    self.world = world
    self.coordinates = coordinates
    self.material = block.STONE
    self.scan_range = 3

    self.update(distance)
    self.draw(self.coordinates, self.material)

  def draw(self, coordinates, material):
    [x,y,z] = coordinates
    height = 3
    distance = 3

    for level in range(0, height):
      self.world.setBlock( x, y + level, z, material) 

  def update(self, distance):
    [x, y, z] = self.coordinates
    x = x + distance
    z = z + distance
    self.coordinates = [x, y, z]
  
  def clear(self):
   self.draw(self.coordinates, block.AIR) 

  def wander(self):
    self.world.postToChat("wandering")
    for i in range(0, 100 ):
      self.clear()
      self.update(1)
      self.draw(self.coordinates, self.material)
      time.sleep(0.2)

  # here is the new scan method
  def scan(self):
    [x, y, z] = self.world.player.getPos()

    if self.within_range(self.coordinates, x, z):
      self.world.postToChat("I see you... ")
    else:
      self.world.postToChat("Come out come out wherever you are!")

  # this method let us know if the method is within looking range
  def within_range(self, coordinates, player_x, player_z):
    result = False
    [x, y, z] = coordinates 
    if player_x > (x - self.scan_range) and player_x < (x + self.scan_range):
      result = True

    if player_z > (z - self.scan_range) and player_z < (z + self.scan_range):
      result = True

    return result

