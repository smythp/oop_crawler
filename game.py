
map = [
    [('house',[6,8]),('bridge',[4,7])],
    [('lake',[2,3])]
]

def return_room_mobs(room_name):
    output = []
    for item in room_lookup(room_name).mobs:
        output.append(item.name)
    return output

def find_room(loc):
    if loc[0] < 0 or loc[1] < 0:
        return False
    try:
        return map[loc[1]][loc[0]]
    except IndexError:
        return False

def room_lookup(room_name):
    try:
        return Room.lookup[room_name]
    except KeyError:
        return False

def north_of(loc):
    new_loc = (loc[0],loc[1] - 1)
    return find_room(new_loc)
def south_of(loc):
    new_loc = (loc[0],loc[1] + 1)
    return find_room(new_loc)
def east_of(loc):
    new_loc = (loc[0] + 1,loc[1])
    return find_room(new_loc)
def west_of(loc):
    new_loc = (loc[0] - 1
               ,loc[1])
    return find_room(new_loc)


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
        self.mobs = []
        self.contents = []

            
class Mob(object):
    def __init__(self,name,health,i,loc_name):
        self.name = name
        self.health = health
        self.i = i
        self.status = 'healthy'
        self.loc = room_lookup(loc_name)
        room_lookup(loc_name).mobs.append(self)
        self.attack_rating = 0
        
    def move(self,direction):
        pass

    def take_damage(self,damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.status = 'dead'

class Player(Mob):
    def __init__(self,name,health,i,loc_name):
        self.name = name
        self.health = health
        self.i = i
        self.status = 'healthy'
        self.loc = room_lookup(loc_name)
        room_lookup(loc_name).mobs.append(self)
        self.attack_rating = 0

    def look(self):
        mob_names = []
        for mob in self.loc.mobs:
            mob_names.append(mob.name)
        return "you are at the %s. You see %s here." % (self.loc.name,make_tidy_list(mob_names))

def make_tidy_list(list):
    if len(list) == 0:
        return False
    if len(list) == 1:
        return list[0]
    out = ''
    for item in list[:-1]:
        out = out + "%s, " % item
    out = out + "and %s" % list[-1]
    return out
    

    out = ""
    for item in list:
        out = out + "%s, " % item

        
#    def move(self,direction):
        
create_rooms(map)

# create_rooms(map)

# patterns
# for room in Room.lookup:
#     print(room)

# print(Room.lookup['lake'].loc)

Patrick = Player('Patrick',50,[],'house')
Ann = Mob('Ann',50,[],'house')

# print(Patrick)
# print(Patrick.loc)
# print(room_lookup('house').mobs)
# print(return_room_mobs('house'))

print(make_tidy_list(['hat','coat','chair']))

