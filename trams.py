import xml.etree.ElementTree as ET
import random

# === CONFIGURATION ===
input_file = "demand/tracklessTram/vehicle_demand_fifteenthAve_11112024_Monday_E4.2.rou.xml"
output_file = "demand/tracklessTram/output.rou.xml"
start_time = 28800  # 08:00 in seconds
end_time = 32400    # 09:00 in seconds
car_type_id = "Car"
tram_type_id = "tracklessTram"
tram_capacity = 60
avg_car_occupancy = 1.2
target_route_edges_list = [
    ["1091754525", "229242995#0", "229242995#1", "229242995#2", "229242995#3", "229242998#0", "229242998#1",
                      "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1"],
    ["-229243002", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2", "229242998#3",
                    "821923309", "1091754523", "407171499#1"]
]

MAX_REMOVE = 100  # Number of cars to randomly remove

# === Collect Matching Vehicles First ===
matching_vehicles = []

# === PARSE XML ===
tree = ET.parse(input_file)
root = tree.getroot()

cars_matched = 0
# Count cars removed
cars_removed = 0

# === Remove Cars with Exact Route Match ===
for vehicle in list(root.findall("vehicle")):
    depart = float(vehicle.get("depart", "0"))
    vehicle_type = vehicle.get("type")
    route_elem = vehicle.find("route")

    if route_elem is not None:
        route_edges = route_elem.get("edges", "")
        edge_list = route_edges.split()

        # === Check for exact route match ===
        is_matching_route = any(edge_list == route for route in target_route_edges_list)

        if (
            vehicle_type == car_type_id
            and start_time <= depart <= end_time
            and is_matching_route
        ):
            cars_matched += 1
            matching_vehicles.append(vehicle)

# === Select Random Subset ===
random.shuffle(matching_vehicles)
vehicles_to_remove = matching_vehicles[:MAX_REMOVE]

print(len(vehicles_to_remove))

# === Remove Selected Vehicles from Tree ===
for v in vehicles_to_remove:
    root.remove(v)
cars_removed = len(vehicles_to_remove)


print(f"Matched {cars_matched} cars between 08:00–09:00.")
print(f"Removed {cars_removed} cars between 08:00–09:00.")

# === Define Tram Type if Not Present ===
if not any(vt.get("id") == tram_type_id for vt in root.findall("vType")):
    tram_type = ET.Element("vType", {
        "id": tram_type_id,
        "vClass": "bus",
        "guiShape": "tram",
        "length": "30.0",
        "width": "2.5",
        "maxSpeed": "25.0",
        "accel": "1.0",
        "decel": "2.0",
        "personCapacity": "100",
        "emissionClass": "Zero/default"
    })
    root.Take(1).Last().AddAfterSelf(tram_type)
    print(f"Inserted tram type '{tram_type_id}'")

# === Find next available vehicle ID (integer-based) ===
existing_ids = [int(v.get("id")) for v in root.findall("vehicle") if v.get("id").isdigit()]
next_id = str(max(existing_ids) + 1 if existing_ids else 1)

# === Define Tram Route (as edge list) ===
tram_route_edges = [
    "1091754525", "229242995#0", "229242995#1", "229242995#2", "229242995#3", "229242998#0", "229242998#1",
    "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1"
]

# === Create Tram <vehicle> with child <route> ===
tram_vehicle = ET.Element("vehicle", {
    "id": next_id,
    "type": tram_type_id,
    "depart": str(start_time + 5),  # depart 5s after start
})

ET.SubElement(tram_vehicle, "route", {
    "edges": " ".join(tram_route_edges)
})

# === Append to XML root ===
root.append(tram_vehicle)
print(f"Added one tram with id={next_id}")

# === Save Output === (Always do this)
tree.write(output_file, encoding="utf-8", xml_declaration=True)
print(f"Saved modified route file as {output_file}")
