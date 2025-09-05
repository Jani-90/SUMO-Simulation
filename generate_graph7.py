import pymongo
import matplotlib.pyplot as plt

#==========================================================================================
#     Hourly HC Emission of Light-duty Vehicles for 24 hours based on the day of the week
#==========================================================================================

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["SimOutputDataNew"]
mycol = mydb["emissionData"]

def generate_graph_data(locationD, dateD):
  mydoc = mycol.aggregate([
    { "$match": { 
        "location" : locationD, 
        "date" : dateD,
        "context" : "electricCar_4.8",
        "vType" : { "$in": ["Car", "Motor_Bike"] } 
      } 
    },
    {
      "$group": {
        "_id": "$time_interval",  #Group by the 'time_interval' field
        "total_amount": { "$sum": "$HC" }  #Total sum of HC
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

  return a,b,total
  
def plot_graph_vehicle_count(locationD):
  if locationD == "FIFTEENTH AVE":
    x,y1,t1 = generate_graph_data('FIFTEENTH AVE', '11112024')
    x,y2,t2 = generate_graph_data('FIFTEENTH AVE', '12112024')
    x,y3,t3 = generate_graph_data('FIFTEENTH AVE', '13112024')
    x,y4,t4 = generate_graph_data('FIFTEENTH AVE', '14112024')
    x,y5,t5 = generate_graph_data('FIFTEENTH AVE', '08112024')
    x,y6,t6 = generate_graph_data('FIFTEENTH AVE', '09112024')
    x,y7,t7 = generate_graph_data('FIFTEENTH AVE', '10112024')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('7 Days Hourly HC Emission of Light-duty Vehicles : Fifteenth Avenue Between Cameron Road and Devonport Road')

  elif locationD == "NEWTON STREET":
    x,y1,t1 = generate_graph_data('NEWTON STREET', '29072024')
    x,y2,t2 = generate_graph_data('NEWTON STREET', '30072024')
    x,y3,t3 = generate_graph_data('NEWTON STREET', '31072024')
    x,y4,t4 = generate_graph_data('NEWTON STREET', '01082024')
    x,y5,t5 = generate_graph_data('NEWTON STREET', '02082024')
    x,y6,t6 = generate_graph_data('NEWTON STREET', '03082024')
    x,y7,t7 = generate_graph_data('NEWTON STREET', '28072024')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('7 Days Hourly HC Emission of Light-duty Vehicles : Newton Street Between Aerodrome Road and Tatua Way')

  elif locationD == "TURRET ROAD":
    x,y1,t1 = generate_graph_data('TURRET ROAD', '21082023')
    x,y2,t2 = generate_graph_data('TURRET ROAD', '22082023')
    x,y3,t3 = generate_graph_data('TURRET ROAD', '23082023')
    x,y4,t4 = generate_graph_data('TURRET ROAD', '24082023')
    x,y5,t5 = generate_graph_data('TURRET ROAD', '18082023')
    x,y6,t6 = generate_graph_data('TURRET ROAD', '19082023')
    x,y7,t7 = generate_graph_data('TURRET ROAD', '20082023')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('7 Days Hourly HC Emission of Light-duty Vehicles : Turret Road Between Fifteenth Avenue and Harini Bridge')


  print(x)
  print(y1)
  print(y2)
  print(y3)
  print(y4)
  print(y5)
  print(y6)
  print(y7)
  print(f"Monday : {t1}")
  print(f"Tuesday : {t2}")
  print(f"Wednesday : {t3}")
  print(f"Thursday : {t4}")
  print(f"Friday : {t5}")
  print(f"Saturday : {t6}")
  print(f"Sunday : {t7}")

  
  plt.xlabel("Time (Hour)")
  plt.ylabel("HC Amount (kg)")

  plt.plot(time, y1, color='#4E79A7', label='Monday', marker = 'o')
  plt.plot(time, y2, color='#F28E2B', label='Tuesday', marker = 'o')
  plt.plot(time, y3, color='#59A14F', label='Wednesday', marker = 'o')
  plt.plot(time, y4, color='#E15759', label='Thursday', marker = 'o')
  plt.plot(time, y5, color='#B07AA1', label='Friday', marker = 'o')
  plt.plot(time, y6, color='#EDC948', label='Saturday', marker = 'o')
  plt.plot(time, y7, color='#76B7B2', label='Sunday', marker = 'o')

  # Displaying the legend
  plt.legend()

  plt.show()

def main(): 
    #plot_graph_vehicle_count('FIFTEENTH AVE')
    #plot_graph_vehicle_count('TURRET ROAD')
    plot_graph_vehicle_count('NEWTON STREET')

  

if __name__ == "__main__": 

	# calling main function 
	main()

