
def turn_clockwise(direction, cardinal):
    try:
        index = cardinal.index(direction)
        mod = (index + 1) % 4
        print(direction + " turned clockwise is " + cardinal[mod])
    except:
        print(direction + " is not a direction")
        
def turn_counter_clockwise(direction, cardinal):
    try:
        index = cardinal.index(direction)
        mod = (index - 1) % 4
        print(direction + " turned counter clockwise is " + cardinal[mod])
    except:
        print(direction + " is not a direction")
    

cardinal = ['N', 'E', 'S', 'W']
turn_clockwise('W', cardinal)
turn_clockwise('E', cardinal)
turn_clockwise('S', cardinal)
turn_clockwise('N', cardinal)
turn_clockwise('cheese', cardinal)

turn_counter_clockwise('W', cardinal)
turn_counter_clockwise('E', cardinal)
turn_counter_clockwise('S', cardinal)
turn_counter_clockwise('N', cardinal)
turn_counter_clockwise('cheese', cardinal)
