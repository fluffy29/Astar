import sys
import os
import math

# Custom hash table implementation
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None
    
    def contains(self, key):
        return self.get(key) is not None

# Define the heuristic function
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.hypot(x2 - x1, y2 - y1)

# A* search implementation
def a_star_search(cities, start, goal):
    open_list = []
    closed_list = set()
    open_list.append((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(cities.get(start)['coords'], cities.get(goal)['coords'])}

    while open_list:
        open_list.sort(key=lambda x: x[0])
        current = open_list.pop(0)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        closed_list.add(current)

        for neighbor, cost in cities.get(current)['neighbors']:
            if neighbor in closed_list:
                continue

            tentative_g_score = g_score[current] + cost

            if neighbor not in [i[1] for i in open_list]:
                open_list.append((f_score.get(neighbor, float('inf')), neighbor))

            if tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(cities.get(neighbor)['coords'], cities.get(goal)['coords'])

    return None

# Reconstruct the path from the goal to the start
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def main():
    if len(sys.argv) < 3:
        start_city = input("Enter the start city: ")
        end_city = input("Enter the end city: ")
    else:
        start_city, end_city = sys.argv[1], sys.argv[2]

    # Ensure the map file exists
    map_file = 'FRANCE.MAP'
    if not os.path.exists(map_file):
        print("Map file not found")
        return 2

    # Read the map data
    cities = read_map(map_file)
    if cities is None:
        print("Error reading map file")
        return 2

    # Check if cities exist
    if not cities.contains(start_city) or not cities.contains(end_city):
        print("Unknown city")
        return 1

    # Perform A* search
    path = a_star_search(cities, start_city, end_city)
    if path is None:
        print("No path found")
        return 3
    else:
        print("Path found:", path)
        return 0

def read_map(file_path):
    cities = HashTable()
    data = {
        "Avignon": {"coords": (310, -730), "g": 134, "h": 134, "f": 134},
        "Bordeaux": {"coords": (-740, -470), "g": 321, "h": 321, "f": 321},
        "Brest": {"coords": (-1400, 560), "g": 616, "h": 616, "f": 616},
        "Caen": {"coords": (-600, 730), "g": 459, "h": 459, "f": 459},
        "Calais": {"coords": (-200, 1200), "g": 476, "h": 476, "f": 476},
        "Dijon": {"coords": (315, 220), "g": 115, "h": 115, "f": 115},
        "Grenoble": {"coords": (470, -370), "g": 84, "h": 84, "f": 84},
        "Limoges": {"coords": (-380, -190), "g": 174, "h": 174, "f": 174},
        "Lyon": {"coords": (290, -215), "g": 0, "h": 0, "f": 0},
        "Marseille": {"coords": (430, -910), "g": 209, "h": 209, "f": 209},
        "Montpellier": {"coords": (120, -830), "g": 196, "h": 196, "f": 196},
        "Nancy": {"coords": (510, 600), "g": 259, "h": 259, "f": 259},
        "Nantes": {"coords": (-910, 220), "g": 409, "h": 409, "f": 409},
        "Nice": {"coords": (810, -790), "g": 274, "h": 274, "f": 274},
        "Paris": {"coords": (-190, 640), "g": 334, "h": 334, "f": 334},
        "Rennes": {"coords": (-910, 480), "g": 474, "h": 474, "f": 474},
        "Strasbourg": {"coords": (800, 600), "g": 331, "h": 331, "f": 331},
        "Toulouse": {"coords": (-350, -830), "g": 314, "h": 314, "f": 314},
    }

    # Insert city data into the hash table
    for city, info in data.items():
        cities.insert(city, info)

    # Manually define neighbors and distances (This needs to be adjusted based on actual map data)
    cities.get("Avignon")["neighbors"] = [("Lyon", 227)]
    cities.get("Bordeaux")["neighbors"] = [("Nantes", 329), ("Toulouse", 259)]
    cities.get("Brest")["neighbors"] = [("Rennes", 244)]
    cities.get("Caen")["neighbors"] = [("Paris", 241)]
    cities.get("Calais")["neighbors"] = [("Paris", 297)]
    cities.get("Dijon")["neighbors"] = [("Lyon", 192)]
    cities.get("Grenoble")["neighbors"] = [("Lyon", 104)]
    cities.get("Limoges")["neighbors"] = [("Lyon", 396)]
    cities.get("Lyon")["neighbors"] = [("Dijon", 192), ("Grenoble", 104), ("Marseille", 216)]
    cities.get("Marseille")["neighbors"] = [("Lyon", 216), ("Nice", 158)]
    cities.get("Montpellier")["neighbors"] = [("Lyon", 216)]
    cities.get("Nancy")["neighbors"] = [("Paris", 372)]
    cities.get("Nantes")["neighbors"] = [("Bordeaux", 329)]
    cities.get("Nice")["neighbors"] = [("Marseille", 158)]
    cities.get("Paris")["neighbors"] = [("Lyon", 241)]
    cities.get("Rennes")["neighbors"] = [("Brest", 244)]
    cities.get("Strasbourg")["neighbors"] = [("Nancy", 145)]
    cities.get("Toulouse")["neighbors"] = [("Bordeaux", 259)]

    return cities

if __name__ == "__main__":
    result = main()
    sys.exit(result)
