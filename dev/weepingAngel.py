# We are using inheritance to reduce the amount of code displayed 
# we are telling the computer to use everything 
# we already wrote for the Mob object

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from mob2 import Mob

class WeepingAngel(Mob):
  def __init__(self, world, coordinates, distance):
    super(WeepingAngel, self).__init__(world, coordinates, distance)

  # the collision detection entry point
  # it implements mob2's collision_detection()
  def collision_detection(self):
    #self.our_blocks()
    self.with_player()
    #self.world.postToChat("Collision detection")

  def with_player(self):
    player = self.world.player.getPos()
    if self.overlap(player):
      self.teleport_player()
 
  # overlap the actual code that check if there is an overlap
  def overlap(self, coordinates):
    result = False
    [x, y, z] = self.coordinates 
    [player_x, player_y, player_z] = coordinates

    if (int(player_x) == int(x) ) and (int(player_z) == int(z)) and  (self.in_range(int(y), 3, int(player_y)) or self.in_range(int(y), 3, int(player_y))) :
      result = True

    return result

  def in_range(self, lower, upperOffset, value):
    result = False

    if lower <= value and value <= (lower + upperOffset):
      result = True

    return result
 
  # teleporting the player
  def teleport_player(self):
    [x_change, y_change, z_change] = self.teleporting_coordinates()
    [x, y, z] = self.world.player.getPos()
    
    new_position = [x + x_change, y + y_change, z + z_change ]
    self.world.player.setPos(new_position)
    
    self.world.postToChat("Teleporting player")
 
  def teleport_self(self):
    [x_change, y_change, z_change] = self.teleporting_coordinates()
    self.coordinates = [x + x_change, y + y_change, z + z_change ]
    
    self.world.postToChat("Teleporting mob")
 
  def teleporting_coordinates(self):
    offset = 30
    height_range = 10
   
    x = random.randint(-1 * offset, offset) 
    y = random.randint(0, height_range) 
    z = random.randint(-1 * offset, offset) 

    return [x, y, z]


  def our_blocks(self):
   blocks = self.world.events.pollBlockHits()

   self.world.postToChat("checking being hit")
   
   for block in blocks:

     if self.got_hit(block):
       self.world.postToChat("hit by player")
       self.teleport_self()

  def got_hit(self, block):
    result = False

    if block.pos == self.coordinates:
      result = True

    return result
