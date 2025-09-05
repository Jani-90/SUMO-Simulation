import xml.etree.ElementTree as ET
import random
import math

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
    veh_type_id = "carpool_car"

    if direction == 'P_1':
        target_route_edges_list = [
            ["874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
             "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "85469355#1", "821923308#0",
             "821923308#3", "874420151#0"]
        ]
    elif direction == 'P_2':
        target_route_edges_list = [
            ["-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2",
             "229242998#3", "821923309", "1091754523", "85469355#1", "821923308#0", "821923308#3", "874420151#0"]
        ]

    elif direction == 'P_3':
        target_route_edges_list = [
        ["874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
         "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "85469820#1"]
        ]

    elif direction == 'P_4':
        target_route_edges_list = [
            ["-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2",
             "229242998#3", "821923309", "1091754523", "85469820#1"]
        ]

    elif direction == 'P_5':
        target_route_edges_list = [
            ["874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
             "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3",
             "407171499#4", "1228125583"]
        ]

    elif direction == 'P_6':
        target_route_edges_list = [
            ["-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2",
             "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3", "407171499#4", "1228125583"]
         ]
    elif direction == 'S_1':
        target_route_edges_list = [
            ["874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "375748800#0", "375748800#1", "375748800#4"]
         ]
    elif direction == 'S_2':
        target_route_edges_list = [
            ["874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3", "-1091754525#1", "-1091754525#0",
             "-1091754524", "874944056", "874944055#0", "874944055#1"]
        ]
    elif direction == 'S_3':
        target_route_edges_list = [
            ["229243004", "1100993459#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "375748800#0", "375748800#1", "375748800#4"]
        ]
    elif direction == 'S_4':
        target_route_edges_list = [
            ["229243004", "1100993459#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2", "-229242998#1",
             "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3", "-1091754525#1", "-1091754525#0",
             "-1091754524", "874944056", "874944055#0", "874944055#1"]
        ]
    elif direction == 'S_5':
        target_route_edges_list = [
            ["-874420151#0", "821923307#0", "821923307#1", "85469404#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3",
             "-229242998#2", "-229242998#1", "-229242998#0", "229242996#0", "229242996#1", "375748800#0", "375748800#1", "375748800#4"]
        ]
    elif direction == 'S_6':
        target_route_edges_list = [
            ["-874420151#0", "821923307#0", "821923307#1", "85469404#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3",
             "-229242998#2", "-229242998#1", "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3",
             "-1091754525#1", "-1091754525#0", "-1091754524", "874944056", "874944055#0", "874944055#1"]
        ]


    #MAX_REMOVE = 100  # Number of cars to randomly remove

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

    cars_to_remove = round(cars_matched * 0.2)
    print(cars_matched)
    print(cars_to_remove)

    if cars_to_remove > 1:
        random.shuffle(matching_vehicles)
        vehicles_to_remove = matching_vehicles[:cars_to_remove]

        print(len(vehicles_to_remove))


        # === Remove Selected Vehicles from Tree ===
        for v in vehicles_to_remove:
            print(v.get("id"))
            root.remove(v)
        cars_removed = len(vehicles_to_remove)
    else:
        cars_removed = 0


    print(f"Matched {cars_matched} cars between 08:00–09:00.")
    print(f"Removed {cars_removed} cars between 08:00–09:00.")

    return root, cars_removed

def define_carpoolCar(input_fileD):
    # === PARSE XML ===
    tree = ET.parse(input_fileD)
    root = tree.getroot()

    veh_type_id = "carpool_car"

    # === Define carpool car if Not Present ===
    if not any(vt.get("id") == veh_type_id for vt in root.findall("vType")):
        veh_type = ET.Element("vType", {
            "id": veh_type_id,
            "length": "5.0",
            "maxSpeed": "50.0",
            "accel": "3.0",
            "decel": "6.0",
            "color": "51,194,213"
            
        })

        root.insert(0, veh_type)

    return root

def insert_carpool_cars(root, cars_removed, start_timeD, direction):

    # tree = ET.parse(input_fileD)
    # root = tree.getroot()
    print(cars_removed)
    if cars_removed > 0:
        veh_type_id = "carpool_car"

        num_of_carpool_cars = math.ceil(cars_removed/4)
        print(num_of_carpool_cars)
        #=== Find next available vehicle ID (integer-based) ===
        existing_ids = [int(v.get("id")) for v in root.findall("vehicle") if v.get("id").isdigit()]
        next_id = int(max(existing_ids) + 1 if existing_ids else 1)
        last_id = next_id + num_of_carpool_cars
        print(next_id)
        print(last_id)
        # === Define Tram Route (as edge list) ===


        if direction == 'P_1':
            carpool_route_edges = [
                "874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
                "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "85469355#1",
                "821923308#0", "821923308#3", "874420151#0"
            ]
        elif direction == 'P_2':
            carpool_route_edges = [
                "-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0",
                "229242998#1", "229242998#2",
                "229242998#3", "821923309", "1091754523", "85469355#1", "821923308#0", "821923308#3", "874420151#0"
            ]

        elif direction == 'P_3':
            carpool_route_edges = [
                "874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
         "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "85469820#1"
            ]

        elif direction == 'P_4':
            carpool_route_edges = [
                "-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0",
                "229242998#1", "229242998#2",
                "229242998#3", "821923309", "1091754523", "85469820#1"
            ]

        elif direction == 'P_5':
            carpool_route_edges = [
                "874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
                "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3",
                "407171499#4", "1228125583"
            ]

        elif direction == 'P_6':
            carpool_route_edges = [
                "-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0",
                "229242998#1", "229242998#2",
                "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3", "407171499#4", "1228125583"
            ]
        elif direction == 'S_1':
            carpool_route_edges = [
                "874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2",
                "-229242998#1",
                "-229242998#0", "229242996#0", "229242996#1", "375748800#0", "375748800#1", "375748800#4"
            ]
        elif direction == 'S_2':
            carpool_route_edges = [
                "874420155", "821923311#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2",
                "-229242998#1",
                "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3", "-1091754525#1",
                "-1091754525#0",
                "-1091754524", "874944056", "874944055#0", "874944055#1"
            ]
        elif direction == 'S_3':
            carpool_route_edges = [
                "229243004", "1100993459#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2",
                "-229242998#1",
                "-229242998#0", "229242996#0", "229242996#1", "375748800#0", "375748800#1", "375748800#4"
            ]
        elif direction == 'S_4':
            carpool_route_edges = [
                "229243004", "1100993459#0", "407171500#2", "407171500#3", "-821923309", "-229242998#3", "-229242998#2",
                "-229242998#1",
                "-229242998#0", "229242996#0", "229242996#1", "229242996#2", "229242996#3", "-1091754525#1",
                "-1091754525#0",
                "-1091754524", "874944056", "874944055#0", "874944055#1"
            ]
        elif direction == 'S_5':
            carpool_route_edges = [
                "-874420151#0", "821923307#0", "821923307#1", "85469404#0", "407171500#2", "407171500#3", "-821923309",
                "-229242998#3",
                "-229242998#2", "-229242998#1", "-229242998#0", "229242996#0", "229242996#1", "375748800#0",
                "375748800#1", "375748800#4"
            ]
        elif direction == 'S_6':
            carpool_route_edges = [
                "-874420151#0", "821923307#0", "821923307#1", "85469404#0", "407171500#2", "407171500#3", "-821923309",
                "-229242998#3",
                "-229242998#2", "-229242998#1", "-229242998#0", "229242996#0", "229242996#1", "229242996#2",
                "229242996#3",
                "-1091754525#1", "-1091754525#0", "-1091754524", "874944056", "874944055#0", "874944055#1"
            ]




        for i in range(next_id, last_id, 1):
            rand_time = round(random.uniform(start_timeD, start_timeD+3600),2)
            print(i)
            print(rand_time)
            # === Create Tram <vehicle> with child <route> ===
            carpool_vehicle = ET.Element("vehicle", {
                "id": str(i),
                "depart": str(rand_time),
                "type": veh_type_id,
            })

            carpool_route = ET.SubElement(carpool_vehicle, "route", {
                "edges": " ".join(carpool_route_edges)
            })

            insert_after_time = rand_time

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
                root.insert(insert_index, carpool_vehicle)
            else:
                root.append(carpool_vehicle)

            print(f"Inserted carpool car with id={next_id} after {insert_after_time} seconds")

    return root




def main():
    root_data = define_carpoolCar(
        "demand/electricCar_4.8/vehicle_demand_fifteenthAve_13112024_Wednesday_E4.8.rou.xml")

    for t in range(0, 85500, 3600):
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "P_1")      # 07:00 - 18:00
        root_data = insert_carpool_cars(root_data, cars_removed, t, "P_1")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "P_2")      # 07:00 - 18:00
        root_data = insert_carpool_cars(root_data, cars_removed, t, "P_2")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "P_3")      # 07:00 - 18:00
        root_data = insert_carpool_cars(root_data, cars_removed, t, "P_3")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "P_4")      # 07:00 - 18:00
        root_data = insert_carpool_cars(root_data, cars_removed, t, "P_4")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "P_5")      # 07:00 - 18:00
        root_data = insert_carpool_cars(root_data, cars_removed, t, "P_5")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "P_6")      # 07:00 - 18:00
        root_data = insert_carpool_cars(root_data, cars_removed, t, "P_6")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "S_1")
        root_data = insert_carpool_cars(root_data, cars_removed, t, "S_1")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "S_2")
        root_data = insert_carpool_cars(root_data, cars_removed, t, "S_2")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "S_3")
        root_data = insert_carpool_cars(root_data, cars_removed, t, "S_3")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "S_4")
        root_data = insert_carpool_cars(root_data, cars_removed, t, "S_4")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "S_5")
        root_data = insert_carpool_cars(root_data, cars_removed, t, "S_5")
        root_data, cars_removed = remove_cars(root_data, t, t+3600, "S_6")
        root_data = insert_carpool_cars(root_data, cars_removed, t, "S_6")


    print(root_data)
    # === Save Output ===
    indent(root_data)
    #
    output_file = "demand/carpooling/vehicle_demand_fifteenthAve_13112024_Wednesday_carpooling.rou.xml"

    tree = ET.ElementTree(root_data)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Saved modified route file as {output_file}")

if __name__ == "__main__":

	# calling main function
	main()
