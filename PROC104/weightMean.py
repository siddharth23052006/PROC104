import csv

with open('HeightWeight.csv', newline="") as f:
  reader = csv.reader(f)
  fileData = list(reader)

fileData.pop(0)

data = []
for weight in range(len(fileData)):
  n_weight = fileData[weight][2]
  data.append(float(n_weight))

noOfWeights = len(data)
aggregateWeight = 0
for weightValue in data:
  aggregateWeight+= weightValue

mean = aggregateWeight/noOfWeights
print("Mean:", str(mean))