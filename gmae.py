

map = [
    [('house',[6,8]),('bridge',[4,7])],
    [('lake',[2,3])]
]

def find_room(x,y):
    try:
        return map[y][x]
    except IndexError:
        return False

def create_rooms(map):
    loc_y = 0
    loc_x = 0
    for y in map:
        for x in y:
            Room(x[0],x[1],(loc_x,loc_y))
            loc_x += 1
        loc_x = 0
        loc_y += 1
        
        
class Room(object):
    lookup = {}
    def __init__(self,name,exits,loc):
        self.name = name
        self.exits = exits
        self.loc = loc
        Room.lookup[name] = self
        

    
class Mob(object):
    def __init__(self,health,i,loc):
        self.health = health
        self.i = i
        self.status = 'healthy'
        self.attack_rating = 0
        

    def take_damage(self,damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.status = 'dead'

#    def move(self,direction):
        
#create_rooms(map)

create_rooms(map)

for room in Room.lookup:
    print(room)

print(Room.lookup['lake'].loc)
