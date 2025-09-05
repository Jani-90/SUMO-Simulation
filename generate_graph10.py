import pymongo
import matplotlib.pyplot as plt

#==========================================================================================
#     Breakdown of Emission Components of Light-duty Vehicles per day
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
        "_id": "null",  #No grouping
        "total_CO2_amount": { "$sum": "$CO2" },  #Total sum of CO2
        "total_CO_amount": { "$sum": "$CO" },  #Total sum of CO
        "total_HC_amount": { "$sum": "$HC" },  #Total sum of HC
        "total_NOx_amount": { "$sum": "$NOx" },  #Total sum of NOx
        "total_PMx_amount": { "$sum": "$PMx" }  #Total sum of PMx
      }
    }
  ])

  x = []
  y1 = []

  for i in mydoc:

      x.append(i['_id'])
      y1.append(round(i['total_CO2_amount'],4))
      y1.append(round(i['total_CO_amount'],4))
      y1.append(round(i['total_HC_amount'],4)+round(i['total_HC_amount'],4)+round(i['total_PMx_amount'],4))

      # Get the first 24 elements using slicing
      a = x[:24]
      b = y1[:24] 

  return a,b
  
def plot_graph_vehicle_count(locationD, dateD):

  x,y1 = generate_graph_data(locationD, dateD)
  
  plt.figure() 
  plt.title('Breakdown of Emission Components of Light-duty Vehicles : ' + str(locationD) + ' on ' + str(dateD))

  print(x)
  print(y1)
  mylabels = ["CO2", "CO", "other"]

  amount, texts = plt.pie(y1, labels=mylabels)

  # Calculate percentages
  percentages = [f'{size / sum(y1) * 100:.4f}%' for size in y1]   

  # Customize the legend
  plt.legend(amount, [f'{label}: {pct}' for label, pct in zip(mylabels, percentages)], title="Emission Components")

  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.axis('equal')

  plt.show()


def main(): 
    #plot_graph_vehicle_count('FIFTEENTH AVE', '13112024')
    #plot_graph_vehicle_count('TURRET ROAD', '23082023')
    plot_graph_vehicle_count('NEWTON STREET', '02082024')

  

if __name__ == "__main__": 

	# calling main function 
	main()

