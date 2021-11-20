#%% Libraries
import pyautogui as pGUI
import time as time
import argparse

#Command line arguments
parser = argparse.ArgumentParser(description="""This program keeps your workstation active for a defined time""")
parser.add_argument('-tgp', '--timegap', default=3,
                      help= 'Leave blank unless for extended awake time',
                      type= int)
parser.add_argument('-clktm', '--clicktime', default=60,
                      help= 'defines the time interval between clicks',
                      type= int)
parser.add_argument('-x', '--xcoord', default=1142,
                      help= 'click x coordinate',
                      type= int)
parser.add_argument('-y', '--ycoord', default=1066,
                      help= 'click y coordinate',
                      type= int)

#Parse arguments 
args = parser.parse_args()
timegap = args.timegap
clicktime = args.clicktime
xcoord = args.xcoord
ycoord = args.ycoord

#Set the co-ordinates for the point where the tool clicks
'''
you can determine where you want to click by hovering your mouse over the area and then
determining the location of that point on screen like so > pGUI.position()
'''
clickpoint = [xcoord,ycoord]

awake_time = time.localtime(time.time())[3] + timegap
print('End time: {}, Timegap: {}, Clicktime: {}, Xcoord: {}, Ycoord: {}'.format(awake_time, timegap, clicktime, xcoord, ycoord))

#Find the on screen position of the mouse currently
position = pGUI.position()

while (time.localtime(time.time())[3] < awake_time):
    print('The time is {}:{}'.format(time.localtime(time.time())[3],time.localtime(time.time())[4]))
    #Move mouse to the click point
    pGUI.moveTo(x=clickpoint[0], y=clickpoint[1], duration=0.1)
    #Click on the point 
    pGUI.click(x=clickpoint[0], y=clickpoint[1], clicks=1, interval=0.05, button='left')
    #Make sure the mouse is back at the desired co-ordinates
    pGUI.moveTo(x=clickpoint[0], y=clickpoint[1], duration=0.1)
    #Click again on the coordinate to minimize window
    pGUI.click(x=clickpoint[0], y=clickpoint[1], clicks=1, interval=0.1, button='left')
    #Click again on the coordinate to minimize window
    pGUI.click(x=clickpoint[0], y=clickpoint[1], clicks=1, interval=0.2, button='left')
    #Return the mouse to its original position
    pGUI.moveTo(x=position[0], y=position[1], duration=0.1)
    #pause the program for the desired interval
    time.sleep(clicktime)
##%%
