'''!
@file       gcode converter.py
@brief      This file contains the code for converting gcode to polar coordinates
@details    This script opens a .nc file and creates 3 seperate lists of cartesian
            coordinates which are then converted to polar coordinates
@author     Jakob Frabosilio 
@author     Ayden Carbaugh 
@author     Cesar Santana
@date       02/22/2022
'''


import math

   
def carttopolar():
    '''!
    This method opens a .nc file that contains cartesian coordinates,
    splits them into 3 sperate lists and then converts them to 
    cartesian coordinates
    '''
    ## List of x values
    xlist = []
    ## List of y values
    ylist = []
    ##List of actuation values
    zlist = []
    ## List of theta values
    thetalist = []
    ## List of radial values
    rlist = []
    
    ## offset in inches
    d = 6.04
    ## distance between point of rotation and nozzle
    t = 1.89
    with open('toolpath.nc') as file:
        content = file.readlines()
        for column in content:
            content = column.split(',')
            zlist.append(content[0])
            xlist.append(content[1])
            ylist.append(content[2])
            # Eliminates spaces from the data.
        zlist = [i.replace(" ", "") for i in zlist]
        # Eliminates the \n from the x data.
        zlist = [i.replace("\n", "") for i in zlist]
        # Tests the x data to determine if it can be converted to a float.
        # Data that cannot be converted is removed.
        for i in zlist:
            try:
                i = float(i)
            except (ValueError, TypeError):
                zlist.remove(i)
        # Converts the x data strings to floats to be plotted.
        zlist = [float(i) for i in zlist]
        # Eliminates spaces from the data.
        xlist = [i.replace(" ", "") for i in xlist]
        # Eliminates the \n from the x data.
        xlist = [i.replace("\n", "") for i in xlist]
        # Tests the x data to determine if it can be converted to a float.
        # Data that cannot be converted is removed.
        for i in xlist:
            try:
                i = float(i)
            except (ValueError, TypeError):
                xlist.remove(i)
        # Converts the x data strings to floats to be plotted.
        xlist = [float(i) for i in xlist]
        # Eliminates spaces from the data.
        ylist = [i.replace(" ", "") for i in ylist]
        # Eliminates the \n from the x data.
        ylist = [i.replace("\n", "") for i in ylist]
        # Tests the x data to determine if it can be converted to a float.
        # Data that cannot be converted is removed.
        for i in ylist:
            try:
                i = float(i)
            except (ValueError, TypeError):
                ylist.remove(i)
        # Converts the x data strings to floats to be plotted.
        ylist = [float(i) for i in ylist]
        for i in range(0,len(xlist)):
            phi = math.atan( (ylist[i]+d) / xlist[i] )
            if xlist[i] > 0:
                theta = (phi - math.asin(t/ ( xlist[i]**2+(ylist[i]+d)**2 )**0.5 ) -math.pi/2)*(180/math.pi)
            else:
                theta = (phi - math.asin(t/ ( xlist[i]**2+(ylist[i]+d)**2 )**0.5 ) +math.pi/2)*(180/math.pi)
            thetalist.append(theta)
            r = ( (xlist[i]**2)+((ylist[i] + d)**2)-(t**2) )**(0.5)
            rlist.append(r)
        return [zlist, rlist, thetalist]
#         print(rlist)
#         print(thetalist)
if __name__ == "__main__":
    carttopolar()