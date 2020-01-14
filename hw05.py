# hw05.py -csv C:\1\user_details.csv -json C:\1\user_details.json
import argparse
import csv
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-csv')
parser.add_argument('-json')
ns = parser.parse_args(sys.argv[1:])


data = {}
with open(ns.csv) as csvFile:
    csvReader = csv.DictReader(csvFile)
    fieldnames = [0]
    for csvRow in csvReader:
        user_id = csvRow['user_id']
        data[user_id] = csvRow
        data[user_id]["password"] = "NULL"
        with open(ns.json,'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent = 4))