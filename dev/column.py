# Creating a column
import mcpi.minecraft as minecraft
import mcpi.block as block

world = minecraft.Minecraft.create()

# Get the player's current position and store the coordinates
[x,y,z] = world.player.getPos()
height = 3
distance = 3

for level in range(0, height):
  world.setBlock( x+distance, y + level, z+distance, block.STONE)

