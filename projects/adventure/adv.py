from room import Room
from player import Player
from world import World
from util import Queue,Stack
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Store entire map as graph dictionary
map_graph = {}


def player_travel_direction(direction):
    return player.travel(direction)


# create basic dictionary for each room when visited
def current_room_vertex():
    room = {}
    for exit in player.current_room.get_exits():
        room[exit] = "?"
        map_graph[player.current_room.id] = room
    
# Algorithm to find random exit that hasn't been explored yet
def current_room_unexplored_exit():
    # Track the unexplored exits
    unexplored = []
    # find the exits in a current room
    for exit in player.current_room.get_exits():
        # Check whether given exits is has '?" for being unexplored
        if map_graph[player.current_room.id][exit] == "?":
            unexplored.append(exit)

    # Randomize the choice from unexplored exits and return as a string
    return random.choice(unexplored)

# BFT function to find nearest '?' unexplored exit
# Returns a list of room ids needed to get to first room with unexplored exits


def find_nearest_unexplored_exit(room_id):
    visited = set()
    q = Queue()
    q.enqueue([room_id])

    while q.size() > 0:
        path = q.dequeue()
        current_room = path[-1]
        # Check first after dequeue whether this room has unexplored exits, return path immediately
        if list(map_graph[current_room].values()).count('?') != 0:
            return path
        if current_room not in visited:
            visited.add(current_room)
            # After current room added to visted, we need queue up rooms that needs to check for unexplored exits
            for new_room in map_graph[current_room].values():
                new_path = path.copy()
                new_path.append(new_room)
                q.enqueue(new_path)








# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
