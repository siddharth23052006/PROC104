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
data.sort()

if noOfWeights % 2 == 0:
  median1 = float(data[noOfWeights//2])
  median2 = float(data[noOfWeights//2+1])
  median = (median2+median1)/2

else:
  median = float(data[noOfWeights//2+1])

print("Median: ", str(median))