## Lexicon for parser

import game

tokens = {
    'DIRECTIONS':[
        'NORTH',
        'SOUTH',
        'EAST',
        'WEST',
        'NORTHWEST',
        'NORTHEAST',
        'SOUTHEAST',
        'SOUTHWEST',
        'UP',
        'DOWN',
        'IN',
        'OUT',
        'EXIT',
        'N',
        'S',
        'E',
        'W',
        'U',
        'D',
        'NW',
        'NE',
        'SE',
        'NW',
        ],
    'VERBS':[
        'QUIT',
        'GO',
        'EXAMINE',
        'L',
        'LOOK',
        'RUN',
        'WALK',
        'EAT',
        'KILL',
        ],
    'NOUNS':
     [
        'BEAR',
        'PRINCESS',
        ],
    'FILLER':[
        'THE',
        'OF',
        'A',
        'AN',],
    }

for noun in game.Mob.lookup:
    tokens['NOUNS'].append(noun.upper())




