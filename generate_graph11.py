import pymongo
import matplotlib.pyplot as plt

#==========================================================================================
#     Comparison of Hourly CO2 Emission of Light-duty Vehicles after replacement of Electric Cars
#==========================================================================================

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["SimOutputDataNew"]
mycol = mydb["emissionData"]

def generate_graph_data(locationD, dateD, contextD):
    if contextD == "all_petrol":
        mydoc = mycol.aggregate([
            { "$match": { 
                "location" : locationD, 
                "date" : dateD,
                "context" : contextD,
                "vType" : { "$in": ["Car", "Motor_Bike"] }
                
            } 
            },
            {
            "$group": {
                "_id": "$time_interval",  #Group by the 'time_interval' field
                "total_amount": { "$sum": "$CO2" }  #Total sum of CO2
            }
            },
            # {
            #   "$project": {
            #     "_id": 1,  #Include the 'category'
            #     "distinctCount": { "$size": "$distinctVehicleIds" }  #Count the number of distinct 'vehicle ids'
            #   }
            # },
            {
            "$sort": {
                "_id": 1  #Sort by 'time_interval' in descending order
            }
            }
        ])
    else:
        mydoc = mycol.aggregate([
            { "$match": { 
                "location" : locationD, 
                "date" : dateD,
                "context" : contextD,
                "vType" : { "$in": ["Car", "Motor_Bike", "electricCar"] }
                
            } 
            },
            {
            "$group": {
                "_id": "$time_interval",  #Group by the 'time_interval' field
                "total_amount": { "$sum": "$CO2" }  #Total sum of CO2
            }
            },
            # {
            #   "$project": {
            #     "_id": 1,  #Include the 'category'
            #     "distinctCount": { "$size": "$distinctVehicleIds" }  #Count the number of distinct 'vehicle ids'
            #   }
            # },
            {
            "$sort": {
                "_id": 1  #Sort by 'time_interval' in descending order
            }
            }
        ])


    x = []
    y = []
    for i in mydoc:

        x.append(i['_id'])
        y.append(round(i['total_amount']/1000000,4))
    
    # Get the first 24 elements using slicing
    a = x[:24]
    b = y[:24]
    total = sum(b)   

    if not x or not y:
        print(f"No data found for {locationD}, {dateD}, {contextD}")
        return [], []

    return a,b, total
  
def plot_graph_vehicle_count(locationD):
  if locationD == "FIFTEENTH AVE":
    #x,y1 = generate_graph_data('FIFTEENTH AVE', '11112024', 'all_petrol')
    # x,y2 = generate_graph_data('FIFTEENTH AVE', '12112024')
    # x,y3 = generate_graph_data('FIFTEENTH AVE', '13112024')
    # x,y4 = generate_graph_data('FIFTEENTH AVE', '14112024')
    # x,y5 = generate_graph_data('FIFTEENTH AVE', '08112024')
    # x,y6 = generate_graph_data('FIFTEENTH AVE', '09112024')
    # x,y7 = generate_graph_data('FIFTEENTH AVE', '10112024')
    x,y8,t8 = generate_graph_data('FIFTEENTH AVE', '13112024', 'electricCar_4.8')
    #x,y9 = generate_graph_data('FIFTEENTH AVE', '11112024', 'electricCar_10')
    x,y9,t9 = generate_graph_data('FIFTEENTH AVE', '13112024', 'electricCar_20')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('Comparison of Hourly CO2 Emission of Light-duty Vehicles after replacement of Electric Cars : Fifteenth Avenue Between Cameron Road and Devonport Road')

  elif locationD == "NEWTON STREET":
    x,y1 = generate_graph_data('NEWTON STREET', '29072024')
    x,y2 = generate_graph_data('NEWTON STREET', '30072024')
    x,y3 = generate_graph_data('NEWTON STREET', '31072024')
    x,y4 = generate_graph_data('NEWTON STREET', '01082024')
    x,y5 = generate_graph_data('NEWTON STREET', '02082024')
    x,y6 = generate_graph_data('NEWTON STREET', '03082024')
    x,y7 = generate_graph_data('NEWTON STREET', '28072024')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('Comparison of Hourly CO2 Emission of Light-duty Vehicles after replacement of Electric Cars : Newton Street Between Aerodrome Road and Tatua Way')


  print(x)
  #print(y1)
  print(y8)
  print(y9)
  print(f"Real World Scenario : {t8}")
  print(f"20% Electric Cars : {t9}")
#   print(y3)
#   print(y4)
#   print(y5)
#   print(y6)
#   print(y7)

  
  plt.xlabel("Time (Hour)")
  plt.ylabel("CO2 Amount (kg)")

  #plt.plot(time, y1, color='red', label='All Petrol Cars', marker = 'o')
  plt.plot(time, y8, color='red', label='Real World Scenario', marker = 'o')
  #plt.plot(time, y9, color='red', label='10% Electric Cars', marker = 'o', linestyle='dashed')
  plt.plot(time, y9, color='red', label='20% Electric Cars', marker = 'o', linestyle='dashed')

  # Displaying the legend
  plt.legend()

  plt.show()

def main(): 
    plot_graph_vehicle_count('FIFTEENTH AVE')
    #plot_graph_vehicle_count('NEWTON STREET')

  

if __name__ == "__main__": 

	# calling main function 
	main()

