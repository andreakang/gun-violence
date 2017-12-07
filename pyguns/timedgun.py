from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)
 
import csv

# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
GPIO.setup(segments, GPIO.OUT, initial=0)
 
# GPIO ports for the digit 0-3 pins 
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
GPIO.setup(digits, GPIO.OUT, initial=1)
 
#     (a,b,c,d,e,f,g,dp)
num = {' ':(0,0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0,0),
    '1':(0,1,1,0,0,0,0,0),
    '2':(1,1,0,1,1,0,1,0),
    '3':(1,1,1,1,0,0,1,0),
    '4':(0,1,1,0,0,1,1,0),
    '5':(1,0,1,1,0,1,1,0),
    '6':(1,0,1,1,1,1,1,0),
    '7':(1,1,1,0,0,0,0,0),
    '8':(1,1,1,1,1,1,1,0),
    '9':(1,1,1,1,0,1,1,0),
    'b':(0,0,1,1,1,1,1,0),
    'y':(0,1,1,1,0,1,1,0),
    'E':(1,0,0,1,1,1,1,0),
    'A':(1,1,1,0,1,1,1,0),
    'L':(0,0,0,1,1,1,0,0),
    'X':(0,1,1,0,1,1,1,0)}

# array of all the possible time values
time = [33, 15,	27,	40,	50,	75,	16,	25,	50,	18,	31,	107, 15, 62, 30, 55, 22, 50, 129, 19, 38, 25, 30, 18, 40, 23, 130, 20, 35, 18, 29, 90, 21, 47, 32, 15, 100, 14, 60, 19, 31, 26, 41, 120, 17, 16, 32, 20]
timerStarted = False
timeArrayValue = 0
currentCounter = int

# define variables for parsing the csv
results =[]
injured = int
killed = int
date = str
address = str
cityOrCounty = str
state = str
j = 0
printStarted = False # boolean to determine whether the printer can go into the next row & print

with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile)


	for row in reader:

		#print row
		#print row['Incident Date'], row['# Killed']
		results.append (row)
		


for i in range (260):
	injured = int(results[i]['# Injured'])
	killed = int(results[i]['# Killed'])
	date = (results[i]['Incident Date'])
	address = (results[i]['Address'])
	cityOrCounty = (results[i]['City Or County'])
	state = (results[i]['State'])

	if injured > 0 or killed > 0:
		try:
		    runningTime = 0
		    currentCounter = time[timeArrayValue]
		    while runningTime >= 0:
		    	#for n in time: 
		    	#if timerStarted == False:
			        display_string = str(n).rjust(4)
			        seg()
			        runningTime += 1

			        #printStarted = True
			        if runningTime == currentCounter: #once the running time meets the current counter, then print the data
						#do we need to create a mini timer here so that the clock doesn't keep running?
						print printStarted
						print "Last Gun Violence Incident to Date"
						print "Date: " + date
						print "Address: " + address
						print "City or County: " + cityOrCounty
						print "State: " + state
						print "Number injured:", injured
						print "Number killed:", killed
						print "_________________________"
						timeArrayValue +=1
						delay(10)
					#printStarted = False
			       # timerStarted = False
			        
		finally:
		    GPIO.cleanup()


def seg():
    for digit in range(4):
        GPIO.output(segments, (num[display_string[digit]]))
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)




