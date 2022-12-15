import csv

file = open("TitanicSurvival.csv","r")
data = list(csv.reader(file,delimiter = ","))
data[-1][4] = ('1st')
#for i in ([1:len(data)]
# data[i][4] = ('1st')		#overwrite 1st into every 4columb
data[-1].append('Very Good Person')	#add one columb into the array the string inside the brackets is to replace
file.close()

print(data[-1])
