import cadquery as cq
import numpy as np
from cadquery.vis import show
from rotatepoints import rotateabout
def airfoilList(afdata, wconstr, swept):
   
    if len(afdata) != len(wconstr):
        ValueError
    else:
        rangevalue = len(wconstr)
        workplane_init = cq.Workplane()
        for i in range(rangevalue):
            pos = wconstr[i][0]
            
            xvals = afdata[i][0] + swept*pos
            yvals = afdata[i][1]
            xytuple = list(zip(xvals, yvals))

            lastpos = wconstr[i][1]
            twist = wconstr[i][2]
            print("debug" + str(i))

            workplane_init.workplane(offset=pos).spline(xytuple, makeWire=True)

        wing = workplane_init.loft(combine=True)
        show(wing)
            

