"""
Just another approach to Al Sweigart's fantastic Ducklings example.
June 2022, Felix Werthschulte.

"""

from textwrap import wrap
from random import choice
import time

LANE_WIDTH = 5

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
        self.shape = [
            choice(duck[direction][chubbyness]['head']),
            choice(duck[direction][chubbyness]['body']),
            choice(duck[direction][chubbyness]['feet']),
            # add some padding under the duck
            ' ' * LANE_WIDTH
        ]

    def get_shape_row(self):
        # get every row of the "shape" list by popping it out
        return self.shape.pop(0) if self.shape else None

    def get_height(self):
        return len(self.shape)


while True:
    duckling = Duckling()
    for _ in range(duckling.get_height()):
        print(duckling.get_shape_row())
    time.sleep(2)
