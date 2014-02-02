# The block will now tag us 
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

from weepingAngel import WeepingAngel


world = minecraft.Minecraft.create()
time.sleep(5)

world.postToChat("Mob spawning")
coordinates = world.player.getPos()
mob = WeepingAngel(world, coordinates, 3)

time.sleep(5)
world.postToChat("Mob searching")

while True:
  mob.look()
  time.sleep(0.5)

