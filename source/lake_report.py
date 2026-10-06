import csv

with open("data/bangalore_lakes.csv", "r") as file:
    reader = csv.DictReader(file)
    largest=0.0
    name=""
    for r in reader:
       area = float(r["area_acres"])
       if(area > largest):
           largest=area
           name=r["name"]
    print(name,largest)
    
    