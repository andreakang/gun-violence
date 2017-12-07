import csv

results =[]
injured = int
killed = int
date = str
address = str
cityOrCounty = str
state = str
j = 0
printStarted = False

with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile)


	for row in reader:

		#print row
		#print row['Incident Date'], row['# Killed']
		results.append (row)
		

#for i in range (260):
#	killed = int(results[i]['# Killed'])
#	if killed > 0:
#		print results[i]['# Killed']
#		j += 1

#print j
#print len(results[i]['# Killed'])


#for x in range(250):
#	injured = int(results[x]['# Injured'])
#	print injured


for i in range (260):
	injured = int(results[i]['# Injured'])
	killed = int(results[i]['# Killed'])
	date = (results[i]['Incident Date'])
	address = (results[i]['Address'])
	cityOrCounty = (results[i]['City Or County'])
	state = (results[i]['State'])

	if injured > 0 or killed > 0:
		#	this is where the time instigator would go
		printStarted = True
		print printStarted
		print "Last Gun Violence Incident to Date"
		print "Date: " + date
		print "Address: " + address
		print "City or County: " + cityOrCounty
		print "State: " + state
		print "Number injured:", injured
		print "Number killed:", killed
		print "_________________________"
		printStarted = False






