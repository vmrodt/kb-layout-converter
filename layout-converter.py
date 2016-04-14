# License: The MIT License (MIT)

import sys
import os

# Check if enough command line arguments were received
if(len(sys.argv) < 2):
	print("Usage: python3", sys.argv[0], 'file_to_convert')
	sys.exit()

# Display the menu to choose between ANSI (104 keys) and ISO (105 keys) keyboard
print('Type the number for the type of keyboard:')
print('1. ANSI (101, 104, or 87 keys keyboard)')
print('2. ISO (102, 105, or 88 keys keyboard)')
kb_type = int(input())
while (kb_type > 2 and kb_type < 1):
	kb_type = int(input())

# the full path to the layouts.txt file in the directory where the script is
path_to_script = os.path.dirname(os.path.realpath(__file__))
if (kb_type == 1):
	layouts_file_name = os.path.join(path_to_script, 'layouts-ansi.txt' )
else:
	layouts_file_name = os.path.join(path_to_script, 'layouts-iso.txt' )

# Read layouts.txt file and get each layout line as an item in a list
f_layouts = open(layouts_file_name, 'r')
layouts = []
for line in f_layouts:	
	layouts.append(line.split())

# Display the menu for the user to choose the layout they're using right now
i = 0	
print('Type the number for the layout you are using right now:')
for layout in layouts:	
    print(str(i) + ')',str(layout[0]) + '.', )
    i = i + 1
print('Current layout: ')
x = int(input())
number_layouts = len(layouts)
while (x > number_layouts and x < 0):
	x = int(input())
cur_layout = layouts[x]

# Display the menu for the user to choose the layout they want to taste
i = 0	
print('Type the number for the layout you want to taste:')
for layout in layouts:	
    print(str(i) + ')',str(layout[0]) + '.', )
    i = i + 1
print('Layout to taste: ')
x = int(input())
number_layouts = len(layouts)
while (x > number_layouts and x < 0):
	x = int(input())
taste_layout = layouts[x]

# the dictionary to convert from layout to test to the current layout
len_kb = len(taste_layout[1])
dict_taste_to_current = {taste_layout[1][i]:cur_layout[1][i] for i in range(len_kb)}


# open the text to convert and convert each character and write to output file
f = open(sys.argv[1], 'r')
output_file_name = os.path.join(path_to_script, 'converted_text.txt')
f_out = open(output_file_name, 'w')
for line in f:
	for char in line:	
		if (char in dict_taste_to_current):
			if (kb_type == 2):
				if (dict_taste_to_current[char] == 'º'):
					f_out.write('▶LSGT◀')				
				elif (dict_taste_to_current[char] == '²'):
					f_out.write('▶SHIFT+LSGT◀') 
				else:
					f_out.write(dict_taste_to_current[char])
			else: 
				f_out.write(dict_taste_to_current[char])
		else:
			f_out.write(char)			
		
print("output was written to ", output_file_name)
# close files			
f.close()
f_out.close()
f_layouts.close()
