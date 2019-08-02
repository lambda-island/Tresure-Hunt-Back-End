from graph import Room
import random
import math


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.roomGrid = []
        self.gridSize = 0

    def loadGraph(self, roomGraph):
        numRooms = len(roomGraph)
        rooms = [None] * numRooms
        gridSize = 1
        for room in roomGraph:
            x = roomGraph[room][0]['x']
            gridSize = max(gridSize, roomGraph[room][0]['x'], roomGraph[room][0]['y'])
            self.rooms[room] = Room(
                f"Room {room}", f"({roomGraph[room][0]['x']},{roomGraph[room][0]['y']})", room, roomGraph[room][0]['x'], roomGraph[room][0]['y'])
        self.roomGrid = []
        gridSize += 1
        self.gridSize = gridSize
        for room in range(0, gridSize):
            self.roomGrid.append([None] * gridSize)
        for roomID in roomGraph:
            room = self.rooms[roomID]
            self.roomGrid[room.x][room.y] = room
            if 'n' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    'n', self.rooms[roomGraph[roomID][1]['n']])
            if 's' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    's', self.rooms[roomGraph[roomID][1]['s']])
            if 'e' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    'e', self.rooms[roomGraph[roomID][1]['e']])
            if 'w' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    'w', self.rooms[roomGraph[roomID][1]['w']])
        self.startingRoom = self.rooms[0]

    def printRooms(self):
        rotatedRoomGrid = []
        for room in range(0, len(self.roomGrid)):
            rotatedRoomGrid.append([None] * len(self.roomGrid))
        for room in range(len(self.roomGrid)):
            for j in range(len(self.roomGrid[0])):
                rotatedRoomGrid[len(self.roomGrid[0]) -
                                j - 1][room] = self.roomGrid[room][j]
        f = open("map.txt", "w")
        f.write("#####")
        print("#####")
        str = ""
        for row in rotatedRoomGrid:
            allNull = True
            for room in row:
                if room is not None:
                    allNull = False
                    break
            if allNull:
                continue
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        f.write(str)
        f.write("#####")
        f.close()
        print(str)
        print("#####")
