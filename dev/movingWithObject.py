import mcpi.minecraft as minecraft
import mcpi.block as block
import time

world = minecraft.Minecraft.create()

# we create a mob class to create mob objects 
class Mob():
  # this is the method that creates the Mob object
  def __init__(self, coordinates, distance):
    self.coordinates = coordinates
    self.material = block.STONE

    self.update(distance)
    self.draw(self.coordinates, self.material)

  # the rest of the methods looks similar. Notice self as the first argument
  def draw(self, coordinates, material):
    [x,y,z] = coordinates
    height = 3
    distance = 3

    for level in range(0, height):
      world.setBlock( x, y + level, z, material) 

  def update(self, distance):
    [x, y, z] = self.coordinates
    x = x + distance
    z = z + distance
    self.coordinates = [x, y, z]
  
  def clear(self):
   self.draw(self.coordinates, block.AIR) 

  def wander(self):
    world.postToChat("wandering")
    for i in range(0, 100 ):
      self.clear()
      self.update(1)
      self.draw(self.coordinates, self.material)
      time.sleep(0.2)

# Actual code
time.sleep(5)
coordinates = world.player.getPos()
mob = Mob(coordinates, 3)

mob.wander()

