import requests


class Graph:

    def __init__(self):
        self.vertices = {}

    def __str_(self):
        return self.vertices

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def opposite_direction(self, direction):
        exits = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        return exits[direction]

    def bft(self, start):
        visited = set()
        q = Queue()
        q.put(start)
        while q.qsize > 0:
            v = q.get()
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    q.put(neighbor)

    def bfs(self, start):
        q = Queue()
        q.put([start])
        visited = set()

        while q.qsize() > 0:
            path = q.get()
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)

                for neighbor in self.vertices[vertex]:
                    if self.vertices[vertex][neighbor] == '?':
                        return path

                for direction in self.vertices[vertex]:
                    neighbor_room = self.vertices[vertex][direction]
                    new_path = path.copy()
                    new_path.append(neighbor_room)
                    q.put(new_path)
        return None

    def dft(self, start):
        visited = set()
        s = LifoQueue()
        s.put(start)
        while s.qsize > 0:
            v = s.get()
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    s.put(neighbor)


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    def travel(self, direction, showRooms=False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")

#   self.rooms[room] = Room(
#                 f"Room {room}", 
#                 f"({roomGraph[room][0]['x']},
#                 {roomGraph[room][0]['y']})", 
#                 room, 
#                 roomGraph[room][0]['x'], 
#                 roomGraph[room][0]['y'])


class Room:
    def __init__(self, name, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"

    def printRoomDescription(self, player):
        print(str(self))

    def getExits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits

    def getExitsString(self):
        return f"Exits: [{', '.join(self.getExits())}]"

    def connectRooms(self, direction, connectingRoom):
        if direction == "n":
            self.n_to = connectingRoom
            connectingRoom.s_to = self
        elif direction == "s":
            self.s_to = connectingRoom
            connectingRoom.n_to = self
        elif direction == "e":
            self.e_to = connectingRoom
            connectingRoom.w_to = self
        elif direction == "w":
            self.w_to = connectingRoom
            connectingRoom.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def getCoords(self):
        return [self.x, self.y]
