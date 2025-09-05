import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["SimOutputData"]
mycol = mydb["emissionData"]

# if mycol.count_documents({}) == 0:
#     print("Collection is empty. Inserting a sample document...")
#
# else:
#     print("Collection already contains data.")

# Retrieve and print the first document
results = mycol.find_one()
print("First document in collection:")
print(results)
print("Success")

res = mycol.update_many(
  { "scenarioNo": { "$ne": 15 } },
  { "$set": { "context": "all_petrol" } }
)

print("Success")