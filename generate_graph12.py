import pymongo
import matplotlib.pyplot as plt
import numpy as np

#==========================================================================================
#     Relationship between Vehicle Emission and Vehicle Density for Light-duty Vehicles 

#     Vehicle Density = Length of Road Segment / Number of Vehicles on a Road Segment

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
        "distinctVehicleIds": { "$addToSet": "$vid" }  #Collect distinct 'vehicle ids'
      }
    },
    {
      "$project": {
        "_id": 1,  #Include the 'category'
        "distinctCount": { "$size": "$distinctVehicleIds" }  #Count the number of distinct 'vehicle ids'
      }
    },
    {
      "$sort": {
        "_id": 1  #Sort by 'time_interval' in descending order
      }
    }
  ])

  if locationD == "FIFTEENTH AVE":
    road_length = 550/1000  #Length of road segment in km
  elif locationD == "NEWTON STREET":
    road_length = 850/1000
  elif locationD == "TURRET ROAD":
    road_length = 650/1000

  x = []
  y = []
  for i in mydoc:
      #print(i)
      #print(i['_id'])
      x.append(i['_id'])
      y.append(round((i['distinctCount']/road_length),2))
      # Get the first 10 elements using slicing
      a = x[:24]
      b = y[:24]    

  return a,b

def generate_graph_data2(locationD, dateD):
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
      y.append(round(i['total_amount']/1000000,2))
      # Get the first 24 elements using slicing
      a = x[:24]
      b = y[:24]    

  return a,b
  
def plot_graph_vehicle_count(locationD):
  if locationD == "FIFTEENTH AVE":
    x,y1 = generate_graph_data('FIFTEENTH AVE', '13112024')
    x,z1 = generate_graph_data2('FIFTEENTH AVE', '13112024')
    # x,y2 = generate_graph_data('FIFTEENTH AVE', '12112024')
    # x,y3 = generate_graph_data('FIFTEENTH AVE', '13112024')
    # x,y4 = generate_graph_data('FIFTEENTH AVE', '14112024')
    # x,y5 = generate_graph_data('FIFTEENTH AVE', '08112024')
    # x,y6 = generate_graph_data('FIFTEENTH AVE', '09112024')
    # x,y7 = generate_graph_data('FIFTEENTH AVE', '10112024')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('Relationship between Vehicle Emission and Vehicle Density for Light-duty Vehicles : Fifteenth Avenue Between Cameron Road and Devonport Road')

  elif locationD == "NEWTON STREET":
    x,y1 = generate_graph_data('NEWTON STREET', '29072024')
    # x,y2 = generate_graph_data('NEWTON STREET', '30072024')
    # x,y3 = generate_graph_data('NEWTON STREET', '31072024')
    # x,y4 = generate_graph_data('NEWTON STREET', '01082024')
    # x,y5 = generate_graph_data('NEWTON STREET', '02082024')
    # x,y6 = generate_graph_data('NEWTON STREET', '03082024')
    # x,y7 = generate_graph_data('NEWTON STREET', '28072024')
    time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    plt.figure() 
    plt.title('Relationship between Vehicle Emission and Vehicle Density for Light-duty Vehicles : Newton Street Between Aerodrome Road and Tatua Way')


  print(x)
  print(y1)
  print(z1)
#   print(y2)
#   print(y3)
#   print(y4)
#   print(y5)
#   print(y6)
#   print(y7)

  
  plt.xlabel("Density (veh/km)")
  plt.ylabel("CO2 Emission (kg) ")
  plt.scatter(y1, z1, color='red', label='Data')
 
  x = np.array(y1)
  y = np.array(z1)

  # Sort data by x values
  sorted_indices = np.argsort(x)
  x_sorted = x[sorted_indices]
  y_sorted = y[sorted_indices]

  # Fit cubic polynomial
  coeffs = np.polyfit(x_sorted, y_sorted, deg=3)
  p = np.poly1d(coeffs)

  # Generate smooth curve for regression line
  x_smooth = np.linspace(x_sorted.min(), x_sorted.max(), 500)
  y_smooth = p(x_smooth)

  # # Fit a linear regression line
  # coefficients = np.polyfit(y1, z1, 3)  # degree 1 for linear
  # poly_eqn = np.poly1d(coefficients)
  # z1_fit = poly_eqn(y1)

 

# Plot the line
  #plt.plot(y1, z1_fit, color='green', label='Best Fit Line')
  #plt.plot(y1, z1_fit, color='green', label=f'Polynomial Fit: {poly_eqn}')
  plt.plot(x_smooth, y_smooth, color='green', label='Cubic Regression')

  #plt.plot(time, y1, color='red', label='Monday', marker = 'o')
#   plt.plot(time, y2, color='green', label='Tuesday', marker = 'o')
#   plt.plot(time, y3, color='blue', label='Wednesday', marker = 'o')
#   plt.plot(time, y4, color='yellow', label='Thursday', marker = 'o')
#   plt.plot(time, y5, color='cyan', label='Friday', marker = 'o')
#   plt.plot(time, y6, color='magenta', label='Saturday', marker = 'o')
#   plt.plot(time, y7, color='gray', label='Sunday', marker = 'o')

  # Displaying the legend
  plt.legend()

  plt.show()

def main(): 
    plot_graph_vehicle_count('FIFTEENTH AVE')
    #plot_graph_vehicle_count('NEWTON STREET')

  

if __name__ == "__main__": 

	# calling main function 
	main()

