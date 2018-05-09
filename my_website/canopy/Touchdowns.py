import matplotlib.pyplot as plt
import os.path

import os.path
directory = os.path.dirname(os.path.abspath(__file__))
#Open the file
filename = os.path.join(directory, 'touchdowns.csv')
datafile = open(filename,'r')
data = datafile.readlines()

#Creates empty list for weight values and touchdowns scored values
xvalues=[]
yvalues=[]
#Appends the values to the respective list
for line in data:
    weight, touchdown = line.split(',')
    xvalues.append(int(weight))
    yvalues.append(int(touchdown))
#Creates an axis for the histogram
fig, ax = plt.subplots (1,1)
#Creates a bar graph with certain color and width
ax.bar(xvalues, yvalues, color='#3366FF', width=7)
#Sets axes titles and graph title
ax.set_title('Weight to Number of Touchdowns Scored (NFL Wide Receievers)')
ax.set_xlabel('Player Weight (Pounds)')
ax.set_ylabel('Number of Touchdowns Scored')
#Changes frequency of y ticks to more accurately read graph
ax.set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
fig.show()