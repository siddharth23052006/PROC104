from collections import Counter
import csv

with open('HeightWeight.csv', newline="") as f:
  reader = csv.reader(f)
  fileData = list(reader)

fileData.pop(0)

weightData = []
for weight in range(len(fileData)):
  n_weight = fileData[weight][2]
  weightData.append(float(n_weight))

data = Counter(weightData)

ranges_of_data = {
  "75-85": 0,
  "85-95": 0,
  "95-105": 0,
  "105-115": 0,
  "115-125": 0,
  "125-135": 0,
  "135-145": 0,
  "145-155": 0,
  "155-165": 0,
  "165-175": 0
}

for weight, occurence in data.items():
  if 75 <= float(weight) < 85:
    ranges_of_data["75-85"]+= occurence

  if 85 <= float(weight) < 95:
    ranges_of_data["85-95"]+= occurence

  if 95 <= float(weight) < 105:
    ranges_of_data["95-105"]+= occurence

  if 105 <= float(weight) < 115:
    ranges_of_data["105-115"]+= occurence

  if 115 <= float(weight) < 125:
    ranges_of_data["115-125"]+= occurence

  if 125 <= float(weight) < 135:
    ranges_of_data["125-135"]+= occurence

  if 135 <= float(weight) < 145:
    ranges_of_data["135-145"]+= occurence

  if 145 <= float(weight) < 155:
    ranges_of_data["145-155"]+= occurence

  if 155 <= float(weight) < 165:
    ranges_of_data["155-165"]+= occurence

  if 165 <= float(weight) < 175:
    ranges_of_data["165-175"]+= occurence

#print(ranges_of_data)

modeRange, modeOccurence = 0, 0
for range, occurence in ranges_of_data.items():
  if occurence > modeOccurence:
    modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
  
mode = float((modeRange[0]+modeRange[1])/2)
print("Mode: ", str(mode))