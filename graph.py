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


graph = Graph()
player = Player('Dylan', None)

requests.get()

for room in rooms:
    graph.add_vertex(room)

print(graph)
