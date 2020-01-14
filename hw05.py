# hw04.py -path_csv example.csv -col_name Marker_Strategy
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