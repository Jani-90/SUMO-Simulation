import pymongo
import matplotlib.pyplot as plt
from datetime import datetime

#==================================================================================
#     Hourly Total Vehicle Volume for 24 hours based on the Vehicle Category
#==================================================================================

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["SimOutputDataNew"]
mycol = mydb["emissionData"]

def generate_graph_data(locationD, dateD, category):
  if category == "Light":
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
  elif category == "Heavy":
     mydoc = mycol.aggregate([
      { "$match": { 
          "location" : locationD, 
          "date" : dateD,
          "context" : "electricCar_4.8",
          "vType" : { "$in": ["Bus", "Truck"] } 
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
     

  x = []
  y = []
  for i in mydoc:

      x.append(i['_id'])
      y.append(i['distinctCount'])
      # Get the first 24 elements using slicing
      a = x[:24]
      b = y[:24]    

  return a,b


  
def plot_graph_vehicle_count(locationD, dateD):
  
  x,y1 = generate_graph_data(locationD, dateD, 'Light')
  x,z1 = generate_graph_data(locationD, dateD, 'Heavy')

  time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
  
  # Convert string to datetime object using strptime (DDMMYYYY format)
  date_obj = datetime.strptime(dateD, "%d%m%Y")
  formatted_date = date_obj.strftime("%B %d, %Y")

  print(x)
  print(y1)
  print(z1)

  plt.figure() 
  plt.title('Hourly Total Vehicle Volume based on Vehicle Category: ' + str(locationD) + ' on ' + str(formatted_date))
  plt.xlabel("Time (Hour)")
  plt.ylabel("Vehicle Count")

  plt.bar(time, y1, label='Light', color='b')  # First part
  plt.bar(time, z1, label='Heavy', color='r', bottom=y1)  # Second part stacked on top

  # Displaying the legend
  plt.legend()

  plt.show()

def main(): 
    #plot_graph_vehicle_count('FIFTEENTH AVE', '13112024')
    #plot_graph_vehicle_count('FIFTEENTH AVE', '11112024')
    #plot_graph_vehicle_count('NEWTON STREET', '31072024')
    plot_graph_vehicle_count('TURRET ROAD', '23082023')

  

if __name__ == "__main__": 

	# calling main function 
	main()

