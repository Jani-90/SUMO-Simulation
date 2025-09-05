import xml.etree.ElementTree as ET
import pandas as pd # To read excel data
import random

#--------------------------Direction P - Fourteenth Ave---------------------------------
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

def read_existing_file(input_fileD, data_fileD, output_fileD):
    # === PARSE XML ===
    tree = ET.parse(input_fileD)
    root = tree.getroot()

    #Read the traffic counts
    counts = pd.read_excel(data_fileD, "Sheet1")
    route = pd.read_excel(data_fileD, "Sheet2")
    vclass = pd.read_excel(data_fileD, "Sheet3")
    print(len(counts))

    for x in range(len(counts)):

        start_time = float(counts['Depart Time'][x])  # 08:00 in seconds
        end_time = start_time + 900
        #car_type_id = "Car"
        print(f"time {start_time}")
        routes = []
        for y in range(len(route)):
            if route['Direction Code'][y] == "P":
                routes.append(route['Route'][y])


        mask = counts['Depart Time'] == start_time
        count_p_value = counts.loc[mask, 'Count_P'].iloc[0]
        print(count_p_value)


        # === Collect Matching Vehicles First ===
        matching_cars = []
        matching_motorbike = []
        matching_bus = []
        matching_truck = []

        target_route_edges_list = [

            ["874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
             "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3",
             "407171499#4", "1228125583"],

            ["-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2",
             "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3", "407171499#4", "1228125583"],

            ["-874420151#0", "821923307#0", "821923307#1", "85469404#0", "407171499#1", "407171499#3", "407171499#4", "1228125583"]
        ]

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
                    vehicle_type == "Car"
                    and start_time <= depart <= end_time
                    and is_matching_route

                ):
                    matching_cars.append(vehicle)
                    print(vehicle.attrib)
                elif (
                        vehicle_type == "Motor_Bike"
                        and start_time <= depart <= end_time
                        and is_matching_route
                ):
                    matching_motorbike.append(vehicle)
                elif (
                        vehicle_type == "Bus"
                        and start_time <= depart <= end_time
                        and is_matching_route
                ):
                    matching_bus.append(vehicle)
                elif (
                        vehicle_type == "Truck"
                        and start_time <= depart <= end_time
                        and is_matching_route
                ):
                    matching_truck.append(vehicle)

        print(len(matching_cars))
        print(len(matching_motorbike))
        print(len(matching_bus))
        print(len(matching_truck))

        balance_veh = count_p_value - len(matching_cars) - len(matching_motorbike) - len(matching_bus) - len(matching_truck)
        print(balance_veh)

        f_vehicle_id = []
        f_depart_time = []
        f_route = []
        f_direction = []
        f_vtype = []

        # === Find next available vehicle ID (integer-based) ===
        existing_ids = [int(v.get("id")) for v in root.findall("vehicle") if v.get("id").isdigit()]
        next_id = int(max(existing_ids) + 1 if existing_ids else 1)
        last_id = next_id + balance_veh - 1
        print(next_id)
        print(last_id)

        time = []
        depart_time = []
        for k in range(0, balance_veh):
            # print(dtime+900)
            random_time = round(random.uniform(start_time, start_time + 900), 2)
            time.append(random_time)

        depart_time = sorted(time)
        print(depart_time)

        routeF = []
        for k in range(0, balance_veh):
            routeF.append(random.choice(routes))

        for i in range(0,balance_veh):
            print(i)
            vehicle_id = next_id + i
            f_vehicle_id.append(vehicle_id)
            f_depart_time.append(depart_time[i])
            f_route.append(routeF[i])
            f_vtype.append('Car')

        print(f_vehicle_id)
        print(f_depart_time)
        print(f_route)
        print(f_vtype)

        for i in range(0,balance_veh):
            # rand_time = round(random.uniform(start_timeD, start_timeD + 3600), 2)
            # print(i)
            # print(rand_time)
            # === Create Tram <vehicle> with child <route> ===
            carpool_vehicle = ET.Element("vehicle", {
                "id": str(f_vehicle_id[i]),
                "depart": str(f_depart_time[i]),
                "type": f_vtype[i],
            })

            carpool_route = ET.SubElement(carpool_vehicle, "route", {
                #"edges": " ".join(f_route[i])
                "edges": "".join(f_route[i])
            })

            insert_after_time = f_depart_time[i]

            # === Find insert index (first vehicle departing after insert_after_time) ===
            insert_index = None
            for j, child in enumerate(root):
                if child.tag == "vehicle":
                    depart_time = float(child.get("depart", "0"))
                    if depart_time > insert_after_time:
                        insert_index = j
                        break

            # === Insert vehicle ===
            if insert_index is not None:
                root.insert(insert_index, carpool_vehicle)
            else:
                root.append(carpool_vehicle)

            print(f"Inserted carpool car with id={f_vehicle_id[i]} after {insert_after_time} seconds")


    indent(root)
    tree = ET.ElementTree(root)
    tree.write(output_fileD, encoding="utf-8", xml_declaration=True)
    print(f"Saved modified route file as {output_fileD}")

def apply_veh_class(input_file, data_file, output_file):

    # === PARSE XML ===
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Read the traffic counts
    vclass = pd.read_excel(data_file, "Sheet3")

    for x in range(len(vclass)):
        if vclass['Dir'][x] == 'P':
            mask = (vclass['Time'] == vclass['Time'][x]) & (vclass['Dir'] == 'P')
            motor_bike_count = vclass.loc[mask, 'Motor Bike (CL1)'].iloc[0]
            car_count = vclass.loc[mask, 'Light (CL2 & CL3)'].iloc[0]
            bus_count = vclass.loc[mask, 'Bus (CL4)'].iloc[0]
            truck_count = vclass.loc[mask, 'Heavy (CL5-CL14)'].iloc[0]
            print(motor_bike_count)
            print(car_count)
            print(bus_count)
            print(truck_count)

            start = vclass['Depart'][x]
            end = start + 3600

            # === Collect Matching Vehicles First ===
            matching_cars = []
            matching_motorbike = []
            matching_bus = []
            matching_truck = []

            target_route_edges_list = [
                ["874944051", "1091754524", "1091754525#0", "1091754525#1", "229242995#0", "229242995#1", "229242995#2", "229242995#3",
                 "229242998#0", "229242998#1", "229242998#2", "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3",
                 "407171499#4", "1228125583"],

                ["-229243002#2", "-229243002#1", "-229243002#0", "229242995#2", "229242995#3", "229242998#0", "229242998#1", "229242998#2",
                 "229242998#3", "821923309", "1091754523", "407171499#1", "407171499#3", "407171499#4", "1228125583"],

                ["-874420151#0", "821923307#0", "821923307#1", "85469404#0", "407171499#1", "407171499#3",
                 "407171499#4", "1228125583"],

                ["229243004", "1100993459#0", "407171499#1", "407171499#3", "407171499#4", "1228125583"]
            ]

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
                            vehicle_type == "Car"
                            and start <= depart <= end
                            and is_matching_route

                    ):
                        matching_cars.append(vehicle)
                    elif (
                            vehicle_type == "Motor_Bike"
                            and start <= depart <= end
                            and is_matching_route
                    ):
                        matching_motorbike.append(vehicle)
                    elif (
                            vehicle_type == "Bus"
                            and start <= depart <= end
                            and is_matching_route
                    ):
                        matching_bus.append(vehicle)
                    elif (
                            vehicle_type == "Truck"
                            and start <= depart <= end
                            and is_matching_route
                    ):
                        matching_truck.append(vehicle)

            print(len(matching_cars))
            print(len(matching_motorbike))
            print(len(matching_bus))
            print(len(matching_truck))

            motor_bike_dis = motor_bike_count - len(matching_motorbike)
            bus_dis = bus_count - len(matching_bus)
            truck_dis = truck_count - len(matching_truck)

            print(motor_bike_dis)
            print(bus_dis)
            print(truck_dis)

            if motor_bike_dis > 0:
                cars_to_convert = random.sample(matching_cars, motor_bike_dis)
                for vehicle in cars_to_convert:
                    print(f"Converting vehicle ID {vehicle.get('id')} from Car to Motor Bike")
                    vehicle.set("type", "Motor_Bike")

            if bus_dis > 0:
                cars_to_convert = random.sample(matching_cars, bus_dis)
                for vehicle in cars_to_convert:
                    print(f"Converting vehicle ID {vehicle.get('id')} from Car to Bus")
                    vehicle.set("type", "Bus")

            if truck_dis > 0:
                cars_to_convert = random.sample(matching_cars, truck_dis)
                for vehicle in cars_to_convert:
                    print(f"Converting vehicle ID {vehicle.get('id')} from Car to Truck")
                    vehicle.set("type", "Truck")

    tree.write(output_file)

def main():
    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_11112024_Monday_6.rou.xml','data/forteenthAve-11112024-Monday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_11112024_Monday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_11112024_Monday_7.rou.xml", "data/forteenthAve-11112024-Monday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_11112024_Monday_8.rou.xml")

    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_12112024_Tuesday_6.rou.xml','data/forteenthAve-12112024-Tuesday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_12112024_Tuesday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_12112024_Tuesday_7.rou.xml", "data/forteenthAve-12112024-Tuesday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_12112024_Tuesday_8.rou.xml")

    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_13112024_Wednesday_6.rou.xml','data/forteenthAve-13112024-Wednesday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_13112024_Wednesday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_13112024_Wednesday_7.rou.xml", "data/forteenthAve-13112024-Wednesday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_13112024_Wednesday_8.rou.xml")

    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_14112024_Thursday_6.rou.xml','data/forteenthAve-14112024-Thursday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_14112024_Thursday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_14112024_Thursday_7.rou.xml", "data/forteenthAve-14112024-Thursday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_14112024_Thursday_8.rou.xml")

    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_08112024_Friday_6.rou.xml','data/forteenthAve-08112024-Friday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_08112024_Friday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_08112024_Friday_7.rou.xml", "data/forteenthAve-08112024-Friday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_08112024_Friday_8.rou.xml")

    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_09112024_Saturday_6.rou.xml','data/forteenthAve-09112024-Saturday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_09112024_Saturday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_09112024_Saturday_7.rou.xml", "data/forteenthAve-09112024-Saturday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_09112024_Saturday_8.rou.xml")

    read_existing_file('demand/all_petrol/vehicle_demand_fifteenthAve_10112024_Sunday_6.rou.xml','data/forteenthAve-10112024-Sunday.xlsx',"demand/all_petrol/vehicle_demand_fifteenthAve_10112024_Sunday_7.rou.xml")
    apply_veh_class("demand/all_petrol/vehicle_demand_fifteenthAve_10112024_Sunday_7.rou.xml", "data/forteenthAve-10112024-Sunday.xlsx","demand/all_petrol/vehicle_demand_fifteenthAve_10112024_Sunday_8.rou.xml")


if __name__ == "__main__":

	# calling main function
	main()
