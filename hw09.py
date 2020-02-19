import csv
import json
import pymongo


myclient = pymongo.MongoClient()
dblist = myclient.list_database_names()
if "test" in dblist:
    myclient.drop_database('test')
mydb = myclient["test"]
col_p = mydb.create_collection("project")
col_t = mydb.create_collection("tasks")


csv_t = 'C:/1/tasks.csv'
csv_p = 'C:/1/project.csv'

def json_to_mongodb(csv_f,colname):
    with open(csv_f, 'r') as csvfile:
        with open('tmp.json', 'w') as jsonfile:
            reader = csv.DictReader(csvfile)
            json.dump(list(reader), jsonfile)
    with open('tmp.json', "r") as f:
        data=json.load(f)
        for row in data:      
            colname.insert_one(row)

if __name__ == '__main__':
    json_to_mongodb(csv_t, col_t)
    json_to_mongodb(csv_p, col_p)

for row in col_t.find({"status": "canceled"}):
    print (row)