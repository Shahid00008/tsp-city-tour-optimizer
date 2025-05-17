# tsp-city-tour-optimizer
# Traveling Salesman Problem Solver (TSP)

## Features

- Greedy TSP path finder
- 2-opt optimization
- CLI interface
- GeoJSON and HTML map output

## Requirements

```bash
pip install folium
```

## Run

```bash
python tsp.py --csv places.csv --start "Eiffel Tower" --return
```

Outputs:
- `route.geojson` (drag-drop into Google Maps)
- `route_map.html` (interactive map)

