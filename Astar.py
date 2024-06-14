import sys
import os
import math
import heapq

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

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.hypot(x2 - x1, y2 - y1)

def a_star_search(cities, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(cities.get(start)['coords'], cities.get(goal)['coords'])}

    print(f"{'OPEN':<15} {'CLOSED':<15} {'succ':<15} {'g(cur)':<10} {'c(cur,succ)':<15} {'g+c':<10}")
    
    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        closed_list.add(current)

        for neighbor, cost in cities.get(current)['neighbors']:
            if neighbor in closed_list:
                continue

            tentative_g_score = g_score[current] + cost

            if neighbor not in [i[1] for i in open_list]:
                heapq.heappush(open_list, (f_score.get(neighbor, float('inf')), neighbor))

            if tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(cities.get(neighbor)['coords'], cities.get(goal)['coords'])

            print(f"{current:<15} {closed_list} {neighbor:<15} {g_score[current]:<10} {cost:<15} {tentative_g_score:<10}")

    return None

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

    map_file = 'FRANCE.MAP'
    if not os.path.exists(map_file):
        print("Map file not found(2)")
        return 2

    cities = read_map(map_file)
    if cities is None:
        print("Error reading map file")
        return 2

    if not cities.contains(start_city) or not cities.contains(end_city):
        print("Unknown city (1)")
        return 1

    path = a_star_search(cities, start_city, end_city)
    if path is None:
        print("No path found(3)")
        return 3
    else:
        print("Path found:", path)
        return 0

def read_map(file_path):
    cities = HashTable()
    data = {
        "Avignon": {"coords": (310, -730), "neighbors": []},
        "Bordeaux": {"coords": (-740, -470), "neighbors": []},
        "Brest": {"coords": (-1400, 560), "neighbors": []},
        "Caen": {"coords": (-600, 730), "neighbors": []},
        "Calais": {"coords": (-200, 1200), "neighbors": []},
        "Dijon": {"coords": (315, 220), "neighbors": []},
        "Grenoble": {"coords": (470, -370), "neighbors": []},
        "Limoges": {"coords": (-380, -190), "neighbors": []},
        "Lyon": {"coords": (290, -215), "neighbors": []},
        "Marseille": {"coords": (430, -910), "neighbors": []},
        "Montpellier": {"coords": (120, -830), "neighbors": []},
        "Nancy": {"coords": (510, 600), "neighbors": []},
        "Nantes": {"coords": (-910, 220), "neighbors": []},
        "Nice": {"coords": (810, -790), "neighbors": []},
        "Paris": {"coords": (-190, 640), "neighbors": []},
        "Rennes": {"coords": (-910, 480), "neighbors": []},
        "Strasbourg": {"coords": (800, 600), "neighbors": []},
        "Toulouse": {"coords": (-350, -830), "neighbors": []},
    }

    for city, info in data.items():
        cities.insert(city, info)

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
    main()
