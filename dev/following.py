import mcpi.minecraft as minecraft
import mcpi.block as block
import time

from mob2 import Mob

world = minecraft.Minecraft.create()
time.sleep(5)

world.postToChat("Mob spawning")
coordinates = world.player.getPos()
mob = Mob(world, coordinates, 3)

time.sleep(5)
world.postToChat("Mob searching")

# this is our version of the game loop
while True:
  mob.look()
  time.sleep(0.5)

