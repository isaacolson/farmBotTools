#!/usr/bin/env python
"""Seeding Path Farmware"""
#Import libraries
#from farmware_tools import device, get_config_value, app

# Load inputs from Farmware page widget specified in manifest file
pos_x = get_config_value('Seeding Path', 'start_x')#Starting X position of Pathway
pos_y = get_config_value('Seeding Path', 'start_y')#Starting Y position of Pathway
pos_z = get_config_value('Seeding Path', 'start_z')
plantLength = get_config_value('Seeding Path', 'Plant-to-Plant Delta X\nFor current waffer use 40mm') #Distance between one center of a plant to another X dimention
plantWidth = get_config_value('Seeding Path', 'Plant-to-Plant Delta Y\nFor current waffer use 30mm') #Distance between one center of a plant to another Y dimention
plantCountLong = get_config_value('Seeding Path', '# of Plants Long') #How many plants are in a column
plantCountWide= get_config_value('Seeding Path', '# of Plants Wide') #How many plans are in a row
# Define plant location arrays
plant_pos_x, plant_pos_x_get = [], [] #X dimention of plant in array at corelating index values of plant_pos_y, redundancy included
plant_pos_y, plant_pos_y_get = [], [] #Y dimention of plant in array at corelating index values of plant_pos_x, redundancy

#Define functions
sense = 1#'sense' is my way of telling the program to go left or right. Sense = 1 Counts UP from ZERO
for i in range(plantCountLong): # for loop for every plant long
	plant_pos_x.append(plantWidth*i+pos_x) # place the plant position in an array
	if sense:
		for j in range(plantCountWide):
			plant_pos_y.append(plantWidth*j+pos_y)
			device.moveAbs(plant_pos_x[i],plant_pos_y[j],pos_z)
                        device.wait(1000)
                        #new_plant = app.add_plant(x = x,y = y)
		    sense = 0
	else:
		for j in range(plantCountWide-1,-1,-1):
			plant_pos_y.append(-1*plantWidth*j+pos_y)
                        device.moveAbs(plant_pos_x[i],plant_pos_y[j],pos_z)
                        device.wait(1000)
                        #new_plant = app.add_plant(x = x,y = y)
                    sense = 1

def moveAbs(x, y, z):
    device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
    device.move_absolute(
        {
            'kind': 'coordinate',
            'args': {'x': x, 'y': y, 'z': z}
        },
        100,
        {
            'kind': 'coordinate',
            'args': {'x': 0, 'y': 0, 'z': 0}
        }
    )

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'

