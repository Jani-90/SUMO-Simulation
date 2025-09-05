import random
import csv
import xml.etree.ElementTree as ET
import pymongo
import math

def generate_demand_file(count_df, routes_df, vclass_df, output_file):

    """
        Generate an XML file containing edge relation data based on the provided DataFrame.

        Parameters:
        - count_df (DataFrame): DataFrame containing edge relation data.
        - output_file (str): Path to the output XML file. Default is 'edge_relation_data.xml'.

        Returns:
        - None (outputs an edge relation file)
    """

    length = len(count_df)
    print(length)
    vehicle_id = 0
    random_time = 0

    routes = []
    routep = []
    f_vehicle_id = []
    f_depart_time = []
    f_route = []
    f_direction = []
    f_vtype = []

    for x in range(len(routes_df)):
        if routes_df['Direction Code'][x] == 'S':
            routes.append(routes_df['Route'][x])
        else:
            routep.append(routes_df['Route'][x])
    #print(routes)
    #print(routep)

    for x in range(len(vclass_df)):
        interval_cat = vclass_df['Time'][x]
        if vclass_df['Dir'][x] == 'P':

            for i in range(length):
                if count_df['Time'][i] == interval_cat:
                    vehicleS = []
                    vehicleP = []
                    time = []
                    depart_time = []
                    vehicle_count_S = count_df['Count_S'][i]
                    vehicle_count_P = count_df['Count_P'][i]
                    dtime = count_df['Depart Time'][i]
                    interval = count_df['Time'][i]

                # starts = routes[0]
                # res_s = list(itertools.islice(itertools.dropwhile(lambda i: i != starts, itertools.cycle(routes)), vehicle_count_S))
                #
                # startp = routep[0]
                # res_p = list(itertools.islice(itertools.dropwhile(lambda i: i != startp, itertools.cycle(routep)), vehicle_count_P))

                #print(res_p)
                    for k in range(0,vehicle_count_S):
                        vehicleS.append(random.choice(routes))


                    for k in range(0,vehicle_count_P):
                        vehicleP.append(random.choice(routep))

                #print(vehicleP)

                    result = two_lists(vehicleS, vehicleP)
                #print(result)

                    total_vehicle_count = vehicle_count_S + vehicle_count_P
                    for k in range(0, total_vehicle_count):
                        print(dtime)
                        #print(dtime+900)
                        random_time = round(random.uniform(dtime, dtime + 900), 2)
                        time.append(random_time)


                #interval = 900/total_vehicle_count
                    #print(total_vehicle_count)
                    #print(time)
                    depart_time = sorted(time)

                    for j in range(0,total_vehicle_count):
                        vehicle_id = vehicle_id + 1
                        f_vehicle_id.append(vehicle_id)
                        f_depart_time.append(depart_time[j])
                        f_route.append(result[j])
                        f_vtype.append('Car')

                        for k in range(len(routes_df)):
                            if routes_df['Route'][k] == result[j]:
                                #print(routes_df['Direction Code'][k])
                                f_direction.append(routes_df['Direction Code'][k])
                        #fh.write(f"\t<vehicle id =\"{vehicle_id}\" depart =\"{depart_time[j]}\">\n")
                        #fh.write(f"\t\t <route edges= \"{result[j]}\"/>\n")
                        #fh.write(f"\t</vehicle>\n")

    #print(f_vehicle_id)
    print(f_depart_time)
    #print(f_route)
    #print(f_direction)
    #print(f_vtype)

    total = 0
    inter = 0
    start_num = 0
    #print(len(vclass_df))
    for k in range(len(vclass_df)):

        if vclass_df['Time'][k] != inter:
            total = total + vclass_df['Total'][k]
        else:
            total = total + vclass_df['Total'][k]
            #print(start_num)
            #print(total-1)
            #rand_num1 = random.randrange(start_num,total-1)
            if vclass_df['Motor Bike (CL1)'][k-1] != 0:
                for n in range(vclass_df['Motor Bike (CL1)'][k-1]):
                    while True:
                        rand_num1 = random.randrange(start_num, total - 1)
                        if vclass_df['Dir'][k-1] == f_direction[rand_num1] and f_vtype[rand_num1] == 'Car':
                            f_vtype[rand_num1] = 'Motor_Bike'
                            break

            if vclass_df['Motor Bike (CL1)'][k] != 0:
                for n in range(vclass_df['Motor Bike (CL1)'][k]):
                    while True:
                        rand_num1 = random.randrange(start_num, total - 1)
                        if vclass_df['Dir'][k] == f_direction[rand_num1] and f_vtype[rand_num1] == 'Car':
                            f_vtype[rand_num1] = 'Motor_Bike'
                            break

            if vclass_df['Bus (CL4)'][k-1] != 0:
                for n in range(vclass_df['Bus (CL4)'][k-1]):
                    while True:
                        rand_num1 = random.randrange(start_num, total - 1)
                        #print('row',vclass_df['Dir'][k-1])
                        #print('random' ,rand_num1)
                        #print('dir',f_direction[rand_num1])
                        if vclass_df['Dir'][k-1] == f_direction[rand_num1] and f_vtype[rand_num1] == 'Car':
                            f_vtype[rand_num1] = 'Bus'
                            break

            if vclass_df['Bus (CL4)'][k] != 0:
                for n in range(vclass_df['Bus (CL4)'][k]):
                    while True:
                        rand_num1 = random.randrange(start_num, total - 1)
                        #print('row2',vclass_df['Dir'][k])
                        #print('dir2',f_direction[rand_num1])
                        if vclass_df['Dir'][k] == f_direction[rand_num1] and f_vtype[rand_num1] == 'Car':
                            f_vtype[rand_num1] = 'Bus'
                            break

            if vclass_df['Heavy (CL5-CL14)'][k-1] != 0:
                for n in range(vclass_df['Heavy (CL5-CL14)'][k-1]):
                    while True:
                        rand_num1 = random.randrange(start_num, total - 1)
                        if vclass_df['Dir'][k-1] == f_direction[rand_num1] and f_vtype[rand_num1] == 'Car':
                            f_vtype[rand_num1] = 'Truck'
                            break

            if vclass_df['Heavy (CL5-CL14)'][k] != 0:
                for n in range(vclass_df['Heavy (CL5-CL14)'][k]):
                    while True:
                        rand_num1 = random.randrange(start_num, total - 1)
                        if vclass_df['Dir'][k] == f_direction[rand_num1] and f_vtype[rand_num1] == 'Car':
                            f_vtype[rand_num1] = 'Truck'
                            break

            start_num = total
        inter = vclass_df['Time'][k]



    #print(f_vtype)

    with open(output_file, 'w') as fh:
        fh.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        fh.write("<routes xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:noNamespaceSchemaLocation='http://sumo.dlr.de/xsd/routes_file.xsd'>\n")
        fh.write(f"\t<vType id='Car' emissionClass='HBEFA3/PC_G_EU4' accel='3.0' decel='6.0' length='5.0' minGap='2.5' maxSpeed='50.0'/>\n")
        fh.write(f"\t<vType id='Bus' emissionClass='HBEFA3/LDV_D_EU4' accel='2.0' decel='5.0' length='7.0' minGap='3.5' maxSpeed='40.0' color='red' guiShape='bus'/>\n")
        fh.write(f"\t<vType id='Truck' emissionClass='HBEFA3/HDV_D_EU4' accel='1.0' decel='5.0' length='7.0' minGap='3.5' maxSpeed='40.0' color='blue' guiShape='truck'/>\n")
        fh.write(f"\t<vType id='Motor_Bike' emissionClass='HBEFA3/PC_G_EU4' accel='2.0' decel='4.0' length='3.0' minGap='2.5' maxSpeed='50.0' color='165,105,189' guiShape='motorcycle'/>\n")
        fh.write(
            f"\t<vType id='electricCar' emissionClass='Zero' accel='3.0' decel='6.0' length='5.0' minGap='2.5' maxSpeed='50.0' color='green'>\n")
        fh.write(f"\t\t <param key='has.battery.device' value='true'/> \n")
        fh.write(f"\t\t <param key='device.battery.capacity' value='2000'/> \n")
        fh.write(f"\t\t <param key='maximumPower' value='1000'/> \n")
        fh.write(f"\t\t <param key='frontSurfaceArea' value='5'/> \n")
        fh.write(f"\t\t <param key='airDragCoefficient' value='0.6'/> \n")
        fh.write(f"\t\t <param key='rotatingMass' value='100'/> \n")
        fh.write(f"\t\t <param key='radialDragCoefficient' value='0.5'/> \n")
        fh.write(f"\t\t <param key='rollDragCoefficient' value='0.01'/> \n")
        fh.write(f"\t\t <param key='constantPowerIntake' value='100'/> \n")
        fh.write(f"\t\t <param key='propulsionEfficiency' value='0.9'/> \n")
        fh.write(f"\t\t <param key='recuperationEfficiency' value='0.9'/> \n")
        fh.write(f"\t\t <param key='stoppingThreshold' value='0.1'/> \n")
        fh.write(f"\t\t <param key='device.battery.maximumChargeRate' value='150000'/> \n")
        fh.write(f"\t</vType>\n")

        for j in range(len(f_vehicle_id)):

            fh.write(f"\t<vehicle id =\"{f_vehicle_id[j]}\" depart =\"{f_depart_time[j]}\" type =\"{f_vtype[j]}\">\n")
            fh.write(f"\t\t <route edges= \"{f_route[j]}\"/>\n")
            fh.write(f"\t</vehicle>\n")

        fh.write("</routes>")
    fh.close()

def two_lists(lst1, lst2):
    result = []

    for pair in zip(lst1, lst2):
        result.extend(pair)

    if len(lst1) != len(lst2):
        lsts = [lst1, lst2]
        smallest = min(lsts, key=len)
        biggest = max(lsts, key=len)
        rest = biggest[len(smallest):]
        result.extend(rest)

    return result

def parseXML(locationD, dateD, dayD, xmlfile, contextD):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for sim Data
    simData = []
    #i = 1

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["SimOutputDataNew"]
    mycol = mydb["emissionData"]

    lastD = mycol.find().sort({ '_id': -1}).limit(1)


    if mycol.count_documents({}) == 0:
        print("The collection is empty.")
        scenarioNo = 0
        id = 0
    else:
        print("The collection is not empty.")
        for data in lastD:
            scenarioNo = data['scenarioNo']
            id = data['id']


    for timestep in root.findall('timestep'):

        for child in timestep:
            rowData = {}
            time_interval = math.floor(int(float(timestep.get('time')))/3600)
            rowData['id'] = id + 1
            rowData['scenarioNo'] = scenarioNo + 1
            rowData['location'] = locationD
            rowData['date'] = dateD
            rowData['day'] = dayD
            rowData['time'] = int(float(timestep.get('time')))
            rowData['time_interval'] = time_interval
            rowData['vid'] = child.get('id')
            rowData['CO2'] = float(child.get('CO2'))
            rowData['CO'] = float(child.get('CO'))
            rowData['HC'] = float(child.get('HC'))
            rowData['NOx'] = float(child.get('NOx'))
            rowData['PMx'] = float(child.get('PMx'))
            rowData['vType'] = child.get('type')
            rowData['speed'] = float(child.get('speed'))
            rowData['context'] = contextD
            #print(rowData)

            simData.append(rowData)
            id = id + 1

    return simData


def savetoCSV(simData, filename):

    # specifying the fields for csv file
    fields = ['id', 'scenarioNo', 'location', 'date', 'day', 'time', 'time_interval', 'vid', 'CO2', 'CO', 'HC', 'NOx', 'PMx', 'vType', 'speed', 'context']

    # writing to csv file
    with open(filename, 'w', newline = '') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(simData)


def DBinsert(locationD, dateD, dayD, result, contextD):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["SimOutputDataNew"]
    mycol = mydb["emissionData"]

    filter_dict = {'location': locationD,
                  'date': dateD, 'day': dayD, 'context': contextD}
    if mycol.count_documents(filter_dict):
        mycol.delete_many(filter_dict)
        mycol.insert_many(result)
    else:
        mycol.insert_many(result)


