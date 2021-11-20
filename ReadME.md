# Stay Awake

This tool is indended to keep computers with locked sleep and display controls to stay awake by automating mouse click controls

## Setup 

Create the required conda environment as provided in the repository 

## Usage
### Finding position of clickable object
TBD: for now you can determine where you want to click by hovering your mouse over the area and then determining the location of that point on screen like so > pGUI.position(). Easiest to do in the vscode hybrid window
### Batch file edits
1. Use the provided batch files as necessary for the length of time that the computer should stay awake.
2. Use the batch line script to enter the required details e.g.,: 
> python clicker.py -tgp 5 -clktm 120 -x 1142 -y 1066
3. The timegap is the length (in hours) that the batch file runs, the clicktime is the time between clicks (in seconds), the x and y co-ordinates are the x,y co-ordinates of the area being clicked.
4. In this example, the script runs for 5 hours, clicks on the co-ordinates every 120 seconds, and the co-ordinates it clicks on are (1142,1066)
