import xml.etree.ElementTree as ET
import random

def convert_to_electricCars(input_file, output_file, percentage):
    # Load the route file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Define the type(s) that count as petrol cars
    car_types_to_convert = {'Car'}  # Add your specific types
    bus_types_to_convert = {'Bus'}
    truck_types_to_convert = {'Truck'}
    motorbike_types_to_convert = {'Motor_Bike'}
    electricCar_types_to_convert = {'electricCar'}

    # Collect all vehicles of those types
    car_vehicles = [veh for veh in root.findall('vehicle') if veh.get('type') in car_types_to_convert]
    bus_vehicles = [veh for veh in root.findall('vehicle') if veh.get('type') in bus_types_to_convert]
    truck_vehicles = [veh for veh in root.findall('vehicle') if veh.get('type') in truck_types_to_convert]
    motorbike_vehicles = [veh for veh in root.findall('vehicle') if veh.get('type') in motorbike_types_to_convert]
    electricCar_vehicles = [veh for veh in root.findall('vehicle') if veh.get('type') in electricCar_types_to_convert]

    # Calculate % of them
    num_to_convert = int(percentage * len(car_vehicles))
    selected_cars = random.sample(car_vehicles, num_to_convert)

    # Convert to electric by changing their type
    for veh in selected_cars:
        veh.set('type', 'electricCar')

    # Write to a new file
    tree.write(output_file)
    print(f"Total {len(car_vehicles)} vehicles.")
    print(f"Total {len(bus_vehicles)} vehicles.")
    print(f"Total {len(truck_vehicles)} vehicles.")
    print(f"Total {len(motorbike_vehicles)} vehicles.")
    print(f"Total {len(electricCar_vehicles)} vehicles.")
    print(f"Converted {num_to_convert} vehicles to electric.")

def main():
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_11112024_Monday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_11112024_Monday_E4.8.rou.xml',0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_12112024_Tuesday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_12112024_Tuesday_E4.8.rou.xml',0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_13112024_Wednesday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_13112024_Wednesday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_14112024_Thursday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_14112024_Thursday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_08112024_Friday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_08112024_Friday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_09112024_Saturday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_09112024_Saturday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_fifteenthAve_10112024_Sunday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_fifteenthAve_10112024_Sunday_E4.8.rou.xml', 0.048)

    # ===========================================================================================================================

    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_21082023_Monday.rou.xml',
    #                         'demand/electricCar_4.8/vehicle_demand_turretRoad_21082023_Monday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_22082023_Tuesday.rou.xml',
    #                          'demand/electricCar_4.8/vehicle_demand_turretRoad_22082023_Tuesday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_23082023_Wednesday.rou.xml',
    #                          'demand/electricCar_4.8/vehicle_demand_turretRoad_23082023_Wednesday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_24082023_Thursday.rou.xml',
    #                          'demand/electricCar_4.8/vehicle_demand_turretRoad_24082023_Thursday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_18082023_Friday.rou.xml',
    #                          'demand/electricCar_4.8/vehicle_demand_turretRoad_18082023_Friday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_19082023_Saturday.rou.xml',
    #                          'demand/electricCar_4.8/vehicle_demand_turretRoad_19082023_Saturday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_turretRoad_20082023_Sunday.rou.xml',
    #                          'demand/electricCar_4.8/vehicle_demand_turretRoad_20082023_Sunday_E4.8.rou.xml', 0.048)

    #=======================================================================================================================

    #convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_29072024_Monday.rou.xml',
    #                       'demand/electricCar_4.8/vehicle_demand_newtonStreet_29072024_Monday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_30072024_Tuesday.rou.xml',
    #                        'demand/electricCar_4.8/vehicle_demand_newtonStreet_30072024_Tuesday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_31072024_Wednesday.rou.xml',
    #                        'demand/electricCar_4.8/vehicle_demand_newtonStreet_31072024_Wednesday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_01082024_Thursday.rou.xml',
    #                        'demand/electricCar_4.8/vehicle_demand_newtonStreet_01082024_Thursday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_02082024_Friday.rou.xml',
    #                        'demand/electricCar_4.8/vehicle_demand_newtonStreet_02082024_Friday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_03082024_Saturday.rou.xml',
    #                        'demand/electricCar_4.8/vehicle_demand_newtonStreet_03082024_Saturday_E4.8.rou.xml', 0.048)
    # convert_to_electricCars('demand/all_petrol/vehicle_demand_newtonStreet_28072024_Sunday.rou.xml',
    #                        'demand/electricCar_4.8/vehicle_demand_newtonStreet_28072024_Sunday_E4.8.rou.xml', 0.048)
    #

    #======================================================================================================================

    # convert_to_electricCars('demand/electricCar_4.8/vehicle_demand_fifteenthAve_11112024_Monday_E4.8.rou.xml',
    #                         'demand/electricCar_10/vehicle_demand_fifteenthAve_11112024_Monday_E10.rou.xml',0.1)

    convert_to_electricCars('demand/electricCar_4.8/vehicle_demand_fifteenthAve_13112024_Wednesday_E4.8.rou.xml',
                            'demand/electricCar_20/vehicle_demand_fifteenthAve_13112024_Wednesday_E20.rou.xml',0.2)




if __name__ == "__main__":

	# calling main function
	main()