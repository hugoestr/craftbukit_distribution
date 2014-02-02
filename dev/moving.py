# Creating a column that will start moving
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# the following are methods
def draw(world, coordinates, material):
  [x,y,z] = coordinates
  height = 3

  for level in range(0, height):
    world.setBlock( x, y + level, z, material) 

def update(coordinates, distance):
  [x, y, z] = coordinates
  x = x + distance
  z = z + distance
  coordinates = [x, y, z]

  return coordinates

def clear(world, coordinates):
 draw(world, coordinates, block.AIR) 

def wander(world, coordinates, material):
  world.postToChat("wandering")
  
  for i in range(0, 100):
    clear(world, coordinates)
    coordinates = update(coordinates, 1)
    draw(world, coordinates, material)
    
    time.sleep(0.2)

# the set up code
world = minecraft.Minecraft.create()

coordinates = world.player.getPos()
material = block.STONE
distance = 3

coordinates = update(coordinates, distance)
draw(world, coordinates, material)

time.sleep(5)

# We start using our method here
wander(world, coordinates, material)
