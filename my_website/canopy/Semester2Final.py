import matplotlib.pyplot as plt
import os.path  

#Defines the color values corresponding to all 32 NFL teams (I use two colors per team)
teams = {'bears':[16,16,52], 'bears2':[230,96,0], 'bengals':[255,102,0], 'bengals2':[255,255,255], 'bills':[0,33,124],
'bills2':[193,196,205],'broncos':[230,96,0], 'broncos2':[16,16,52], 'browns':[204,102,0], 'browns2':[26,13,0],
'buccaneers':[165,0,0], 'buccaneers2':[64,64,64], 'cardinals':[165,0,0], 'cardinals2':[230,230,230], 'chargers':[0,0,102], 
'chargers2':[204,204,0], 'chiefs':[230,230,230], 'chiefs2':[165,0,0], 'colts':[0,51,204], 'colts2':[230,230,229],
'cowboys':[194,196,198], 'cowboys2':[2,16,51], 'dolphins':[54,150,126], 'dolphins2':[186,105,1], 'eagles':[27,48,27],
'eagles2':[129,132,129], 'falcons':[183, 1, 13], 'falcons2':[0,0,0], 'giants':[9,21,79], 'giants2':[127,1,13],
'jaguars':[66,153,163], 'jaguars2':[0,0,0], 'jets':[33,66,55], 'jets2':[206,206,206], 'lions':[4,62,209], 'lions2':[158,159,163],
'packers':[0,58,5], 'packers2':[193,204,2], 'panthers':[19,70,147], 'panthers2':[222,224,226], 'patriots':[5,22,48],
'patriots2':[135,0,0], 'raiders':[0,0,0], 'raiders2':[175, 174, 174], 'rams':[5,22,48], 'rams2':[193, 129, 0],
'ravens':[56, 19, 96], 'ravens2':[0,0,0], 'redskins':[230,230,230], 'redskins2':[91,6,6], 'saints':[0,0,0],
'saints2':[193,171,114], 'seahawks':[42,183,0], 'seahawks2':[0,3,91], 'steelers':[0,0,0], 'steelers2':[175,178,5],
'texans':[28,31,58], 'texans2':[86,0,4], 'titans':[35,97,160], 'titans2':[11,23,81], 'vikings':[68,4,142], 'vikings2':[181,191,1]}

#Function to check if the raw_input exists in the 'teams' list
def checkList(item):
    if item in teams:
        pass
    else:
        print " "
        print "Please enter a valid NFL team."
        recolor()

fig, ax = plt.subplots(1,1)
directory = ("C:\\Users\\hssteam\\Desktop\\dane\\finalproject")
#directory = ("/Users/dane/Desktop") 
filename = os.path.join(directory, 'sam.jpg')
img = plt.imread(filename)
height = len(img)
width = len(img[0])

def recolor():
    print "Which NFL team do you want Sam Darnold to play for?"
    choice = raw_input()
    #Runs the function to check if the raw_input exists in the 'teams' list
    checkList(choice.lower())
    color=teams[choice.lower()]
    color2=teams[choice.lower()+"2"]
    
    #Replaces the center of the jersey's color
    for r in range(181,328):
        for c in range(145, 254):
            if [270]>=img[r][c][0]>=[80] and [273]>=img[r][c][1]>=[80] and [300]>=img[r][c][2]>=[75]:
                img[r][c]=color
                
    #Replaces the jersey number color
    for r in range(181,277):
        for c in range(184, 254):
            if [140]>=img[r][c][0]>=[35] and [50]>=img[r][c][1]>=[0] and [40]>=img[r][c][2]>=[0]:
                img[r][c]=color2
                
    #Replaces the color on the jersey's left shoulder
    for r in range(147,181):
        for c in range(150, 200):
            if r in range (145,175) and c in range (156,171):
                pass
            elif [270]>=img[r][c][0]>=[80] and [273]>=img[r][c][1]>=[80] and [300]>=img[r][c][2]>=[75]:
                img[r][c]=color
    for r in range(155,181):
        for c in range(200,225):
            if r in range (155,175) and c in range (216, 225) or r in range (155,162) and c in range (205,220):
                pass
            elif [270]>=img[r][c][0]>=[80] and [273]>=img[r][c][1]>=[80] and [300]>=img[r][c][2]>=[75]:
                img[r][c]=color
    for r in range(149,214):
        for c in range(172,196):
            if [150]>=img[r][c][0]>=[35] and [50]>=img[r][c][1]>=[0] and [40]>=img[r][c][2]>=[0]:
                img[r][c]=color2
    for r in range(171,182):
        for c in range(214,226):
            if [150]>=img[r][c][0]>=[35] and [50]>=img[r][c][1]>=[0] and [40]>=img[r][c][2]>=[0]:
                img[r][c]=color2
                
    #Replaces the color on the jersey's right shoulder
    for r in range(179,235):
        for c in range(254, 295):
            if r in range (227,244) and c in range (258,276):
                pass
            elif [270]>=img[r][c][0]>=[80] and [273]>=img[r][c][1]>=[80] and [300]>=img[r][c][2]>=[75]:
                img[r][c]=color
    for r in range(200,234):
        for c in range(270,294):
            if r in range (227,244) and c in range (258,276):
                pass
            elif [155]>=img[r][c][0]>=[35] and [90]>=img[r][c][1]>=[0] and [70]>=img[r][c][2]>=[0]:
                img[r][c]=color2
    for r in range(179,202):
        for c in range(236,260):
            if r in range (227,244) and c in range (258,276):
                pass
            elif [155]>=img[r][c][0]>=[35] and [90]>=img[r][c][1]>=[0] and [70]>=img[r][c][2]>=[0]:
                img[r][c]=color2
    
    #Replaces the pants color
    for r in range(328,441):
        for c in range(148, 265):             
            if [260]>=img[r][c][0]>=[80] and [250]>=img[r][c][1]>=[0] and [260]>=img[r][c][2]>=[0]: 
                img[r][c]=color2
    
    #Replaces the helmet's color
    for r in range(106,138):
        for c in range(206, 251):
            #if r in range (140,176) and c in range (200,270):
                #pass      
            if r in range (105,113) and c in range (254,270):
                pass 
            elif [260]>=img[r][c][0]>=[40] and [250]>=img[r][c][1]>=[0] and [260]>=img[r][c][2]>=[0]: 
                img[r][c]=color2
    for r in range(110, 138):
        for c in range(251, 266):
            if r in range (109, 115) and c in range (258,266):
                pass
            elif [260]>=img[r][c][0]>=[40] and [250]>=img[r][c][1]>=[0] and [260]>=img[r][c][2]>=[0]: 
                img[r][c]=color2
    for r in range(137, 150):
        for c in range(205, 212):
            if [260]>=img[r][c][0]>=[40] and [250]>=img[r][c][1]>=[0] and [260]>=img[r][c][2]>=[0]:
                img[r][c]=color2
                
    ax.imshow(img)
    ax.set_axis_off()
    plt.show()
    
recolor()