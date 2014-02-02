# Creating a block
import mcpi.minecraft as minecraft
import mcpi.block as block

world = minecraft.Minecraft.create()

# Get the player's current position and store the coordinates
[x,y,z] = world.player.getPos()

world.setBlock( x+1, y, z+1, block.STONE)

