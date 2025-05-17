from collections import namedtuple
from math import radians, cos, sin, sqrt, atan2

Place = namedtuple("Place", ["name", "lat", "lon"])

def read_places(filename):
    import csv
    places = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            places.append(Place(row["name"], float(row["lat"]), float(row["lon"])))
    return places

def haversine(p1, p2):
    R = 6371.0
    lat1, lon1 = radians(p1.lat), radians(p1.lon)
    lat2, lon2 = radians(p2.lat), radians(p2.lon)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))

def build_distance_matrix(places):
    n = len(places)
    dist = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = haversine(places[i], places[j])
    return dist

def greedy_tsp(dist, start_index=0):
    n = len(dist)
    visited = [False]*n
    path = [start_index]
    visited[start_index] = True
    current = start_index
    for _ in range(n - 1):
        next_city = min((i for i in range(n) if not visited[i]), key=lambda x: dist[current][x])
        path.append(next_city)
        visited[next_city] = True
        current = next_city
    return path

def total_distance(path, dist):
    return sum(dist[path[i]][path[(i+1) % len(path)]] for i in range(len(path)))

def two_opt(path, dist):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1: continue
                new_path = path[:i] + path[i:j][::-1] + path[j:]
                if total_distance(new_path, dist) < total_distance(path, dist):
                    path = new_path
                    improved = True
        if improved:
            break
    return path
