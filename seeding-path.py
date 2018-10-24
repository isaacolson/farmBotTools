#!/usr/bin/env python
"""Move Rectangle Farmware"""
#Import libraries
from farmware_tools import device, get_config_value, app

#so far only path of seeding starting at
# Load inputs from Farmware page widget specified in manifest file
pos_x = get_current_position('Seeding Path', 'start_x')
pos_y = get_current_position('Seeding Path', 'start_y')
pos_z = get_current_position('Seeding Path', 'start_z')#later
plantLength_x = get_config_value('Seeding Path', 'distance between plants x')
plantWidth_y = get_config_value('Seeding Path', 'distance between plants y')

#Define functions
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

for i in range(cellCountX):
	plantX = w*i+w/2
	if sense:
		for j in range(cellCountY):
			y = l*j+l/2
			print('cords',x,y)
			
			#new_plant = app.add_plant(x = x,y = y)
		sense = 0
	else:
		for j in range(-1*cellCountY,0):
			y = abs(l*j+l/2)
			print('cords',x,y)
		sense = 1

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
