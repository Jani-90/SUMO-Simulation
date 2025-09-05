import xml.etree.ElementTree as ET
import random

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# === CONFIGURATION ===
def remove_cars(root, start_timeD, end_timeD, direction):

    start_time = float(start_timeD)  # 08:00 in seconds
    end_time = float(end_timeD)    # 09:00 in seconds
    car_type_id = "Car"
    tram_type_id = "tracklessTram"

    if direction == 'S':
        target_route_edges_list = [

            ["874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "375748800#0", "375748800#1", "375748800#4"],

            ["874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3", "-1091754525#1", "-1091754525#0",
             "-1091754524", "874944056", "874944055#0", "874944055#1"]

        ]
    elif direction == 'P':
        target_route_edges_list = [
            ["874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
             "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3",
             "407171499#4", "1228125583"],

            ["-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2",
             "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3", "407171499#4", "1228125583"]

        ]

    MAX_REMOVE = 100  # Number of cars to randomly remove

    # === Collect Matching Vehicles First ===
    matching_vehicles = []

    # # === PARSE XML ===
    # tree = ET.parse(input_file)
    # root = tree.getroot()

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
        print(v.get("id"))
        root.remove(v)
    cars_removed = len(vehicles_to_remove)


    print(f"Matched {cars_matched} cars between 08:00–09:00.")
    print(f"Removed {cars_removed} cars between 08:00–09:00.")

    return root

def define_trackless_tram(input_fileD):
    # === PARSE XML ===
    tree = ET.parse(input_fileD)
    root = tree.getroot()

    tram_type_id = "tracklessTram"

    # === Define Tram Type if Not Present ===
    if not any(vt.get("id") == tram_type_id for vt in root.findall("vType")):
        tram_type = ET.Element("vType", {
            "id": tram_type_id,
            "vClass": "bus",
            "guiShape": "rail",
            "length": "30.0",
            "width": "2.5",
            "maxSpeed": "25.0",
            "accel": "1.0",
            "decel": "2.0",
            "color": "255,128,0",
            "personCapacity": "100",
            "emissionClass": "Zero/default"
        })


        # Only insert if not already present
        #if not any(v.get("id") == "tracklessTram" for v in root.findall("vType")):
        root.insert(0, tram_type)

    return root

def insert_trackless_tram(root, start_timeD, direction):

    # tree = ET.parse(input_fileD)
    # root = tree.getroot()

    tram_type_id = "tracklessTram"

    #=== Find next available vehicle ID (integer-based) ===
    existing_ids = [int(v.get("id")) for v in root.findall("vehicle") if v.get("id").isdigit()]
    next_id = str(max(existing_ids) + 1 if existing_ids else 1)

    # === Define Tram Route (as edge list) ===
    if direction == "P":
        tram_route_edges = [
            "874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2",
            "229242995#3",
            "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1",
            "407171499#3",
            "407171499#4", "1228125583"
        ]
    elif direction == "S":
        tram_route_edges = ["874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3", "-1091754525#1", "-1091754525#0",
             "-1091754524", "874944056", "874944055#0", "874944055#1"]

    # === Create Tram <vehicle> with child <route> ===
    tram_vehicle = ET.Element("vehicle", {
        "id": next_id,
        "depart": str(start_timeD),
        "type": tram_type_id,
    })

    tram_route = ET.SubElement(tram_vehicle, "route", {
        "edges": " ".join(tram_route_edges)
    })

    insert_after_time = start_timeD

    # === Find insert index (first vehicle departing after insert_after_time) ===
    insert_index = None
    for i, child in enumerate(root):
        if child.tag == "vehicle":
            depart_time = float(child.get("depart", "0"))
            if depart_time > insert_after_time:
                insert_index = i
                break

    # === Insert vehicle ===
    if insert_index is not None:
        root.insert(insert_index, tram_vehicle)
    else:
        root.append(tram_vehicle)

    print(f"Inserted tram with id={next_id} after {insert_after_time} seconds")

    return root

# # === Append to XML root ===
# root.append(tram_vehicle)
# print(f"Added one tram with id={next_id}")




def main():
    root_data = define_trackless_tram(
        "demand/electricCar_4.8/vehicle_demand_fifteenthAve_13112024_Wednesday_E4.8.rou.xml")

    for t in range(25200, 68400, 3600):
        root_data = remove_cars(root_data, t, t+3600, "P")      # 07:00 - 18:00
        root_data = insert_trackless_tram(root_data, t, "P")
        root_data = remove_cars(root_data, t, t+3600, "S")
        root_data = insert_trackless_tram(root_data, t, "S")

    print(root_data)
    # === Save Output ===
    indent(root_data)
    #
    output_file = "demand/tracklessTram/vehicle_demand_fifteenthAve_13112024_Wednesday_TTram.rou.xml"

    # tree = ET.parse(output_file)
    # #root = tree.getroot()
    #
    # tree.write(output_file, encoding="utf-8", xml_declaration=True)
    # print(f"Saved modified route file as {output_file}")

    tree = ET.ElementTree(root_data)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Saved modified route file as {output_file}")

if __name__ == "__main__":

	# calling main function
	main()
