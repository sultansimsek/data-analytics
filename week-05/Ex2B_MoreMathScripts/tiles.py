print("""You are going to tile a room whose dimensions are length by width feet. There are
twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
can only buy full boxes, not a partial box.
You also want to buy at least 10% more tiles than you need in order to handle chips,
breakage, and mess-ups. How many total boxes will you buy?""")
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
area = length * width
tiles_needed = area
boxes_needed = tiles_needed / 12
boxes_needed_with_extra = boxes_needed * 1.10
print(f"You need {format(boxes_needed, '.2f')} boxes of tiles to cover the room.")
print(f"With an extra 10% for breakage, you will need {format(boxes_needed_with_extra, '.2f')} boxes of tiles.")

