import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# the code was getting hard to read, so we 
# move the mob class to another file.
from mob import Mob

# Run the code

world = minecraft.Minecraft.create()
time.sleep(5)

coordinates = world.player.getPos()

mob = Mob(world, coordinates, 3)
time.sleep(5)
mob.scan()

