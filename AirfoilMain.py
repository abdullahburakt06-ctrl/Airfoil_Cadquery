import cadquery
from airfoildata import naca4eq
import csv as csv
from generatemodel import airfoilList

#Declare Dataset to store all relevant info
AirfoilDataset = []
WingConstructor = []
with open('enterparameters.csv', newline='') as csvfile:
    first_line = csvfile.readline().strip('\n')
    resolution = first_line.split(",")[1]
    resolution = int(resolution)
    if resolution > 500:
        RuntimeError("Do not go over 500 resolution, this is an arbitrary safeguard that you may change in source code")
    reader = csv.reader(csvfile)
    for row in reader: 
        i = 0
        if len(row) == 4: #TODO Change detection of relevant lines/info asap
            foilstd = row[0]
            c = float(row[1])
            AirfoilDataset.append(naca4eq(foilstd, c, resolution))
            lastpos = 0.0
        
            if str(row[2]).startswith('+')==False:
                pos = float(row[2])
                lastpos = pos
            elif str(row[2]).startswith('+'):
                pos = lastpos + float(row[2])
            
            twistAngle = float(row[3])
            WingConstructor.append([pos, lastpos, twistAngle])
    csvfile.close()

result = airfoilList(AirfoilDataset, WingConstructor, 0.0, 0.0) 
exporters.export(result, "wing.step")  #Write the full path to where you wish to export       
         


        

