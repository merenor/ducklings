"""
Just another approach to Al Sweigart's fantastic Ducklings example.
June 2022, Felix Werthschulte.

"""

from textwrap import wrap
from random import choice, random
from shutil import get_terminal_size
import sys
import time

LANE_WIDTH = 5
TERMINAL_WIDTH, _ = get_terminal_size()
TERMINAL_WIDTH -= 1
EMPTY_LANE = ' ' * LANE_WIDTH
COLORS = [
    "\033[0;31m", # red
    "\033[0;33m", # brown
    "\033[0;37m", # light grey
    "\033[1;30m", # dark grey
    "\033[1;33m", # yellow
    "\033[0;93m", # yellow
    "\033[1;93m", # yellow
    "\033[1;37m", # light white
]

def get_heads(heads: str, head_size: int):
    # cut out the heads and transform it into a list, according to the size
    head_list = wrap(heads, head_size)
    padding = LANE_WIDTH - head_size
    # left heads
    if ')' in heads:
        return [head + ' ' * padding for head in head_list]
    # right heads
    if '(' in heads:
        return [' ' + head + ' ' * (padding-1) for head in head_list]

def turn_around(heads):
    return heads[::-1].translate(str.maketrans('´>)', '`<('))

# create the heads of the very chubby ones
chubby_heads_left = """='')=00)=**)=^^)=´´)=" )"""

# create the heads of the chubby ones
slim_heads_left = """=")=%)=8)=&)=')"""

# add the ones with mouth open
chubby_heads_left += chubby_heads_left.replace('=', '>')
slim_heads_left += slim_heads_left.replace('=', '>')

# turn around and replace certain characters (wings etc.)
chubby_heads_right = turn_around(chubby_heads_left)
slim_heads_right = turn_around(slim_heads_left)

# structure for a duck
duck = {
    'left': {
        'very chubby': {
            'head': get_heads(chubby_heads_left, head_size=4),
            'body': ['(  v)', '(  >)'],
            'feet': [' ^ ^ ', ' l l ', ' 7 7 ']
        },
        'chubby': {
            'head': get_heads(slim_heads_left, head_size=3),
            'body': ['( v) ', '( >) '],
            'feet': [' ^^  ', ' ll  ', ' 77  ']
        }
    },
    'right': {
        'very chubby': {
            'head': get_heads(chubby_heads_right, head_size=4),
            'body': ['(v  )', '(<  )'],
            'feet': [' ^ ^ ', ' l l ', ' \\ \\ ']
        },
        'chubby':{
            'head': get_heads(slim_heads_right, head_size=3),
            'body': ['( v) ', '( >) '],
            'feet': [' ^^  ', ' ll  ', ' \\\\  ']
        }
    }
}


class Duckling:
    def __init__(self):
        direction = choice(['left', 'right'])
        chubbyness = choice(['chubby', 'very chubby'])
        self.color = choice(COLORS)
        self.shape = [
            choice(duck[direction][chubbyness]['head']),
            choice(duck[direction][chubbyness]['body']),
            choice(duck[direction][chubbyness]['feet']),
        ]

    def get_shape_row(self):
        # get every row of the "shape" list by popping it out
        return self.color + self.shape.pop(0) if self.shape else None


def main():
    print("Ducklings Screensaver, by Al Sweigart")
    print("Optimized version by Felix Werthschulte, June/July 2022")
    print()
    time.sleep(2)

    lanes = [None] * (TERMINAL_WIDTH // LANE_WIDTH)
    density = 0.05
    speed = 1.0

    if len(sys.argv) > 1:
        try:
            density = float(sys.argv[1])
        except:
            pass
        try:
            speed = float(sys.argv[2])
        except:
            pass

    while True:
        for lane_num, lane in enumerate(lanes):
            duck_part = ''
            if lane == None:
                if random() <= density:
                    # random decides there shall be a duckling
                    duck = Duckling()
                    lanes[lane_num] = duck
                    # get first part of the duckling
                    duck_part = lanes[lane_num].get_shape_row()
                else:
                    # random decides there shall be no duckling,
                    # so print an empty space
                    duck_part = EMPTY_LANE
            else:
                # there is a duckling object, get its next part
                duck_part = lane.get_shape_row()
                if duck_part == None:
                    # if it's finished, clear the lane
                    duck_part = EMPTY_LANE
                    # clear the lane
                    lanes[lane_num] = None
            print(duck_part, end='')
        print()
        sys.stdout.flush()
        time.sleep(speed)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
