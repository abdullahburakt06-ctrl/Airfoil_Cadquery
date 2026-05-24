#Backup for myself and as a way to keep changes visible
#not recommended for use

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

            workplane_init.workplane().transformed((0, 0, twist), offset=(pos*swept, dihedral*pos, pos)).spline(xytuple, makeWire=True)
           #15/5/2026 added twist and dihedral options. Set parameters in result=airfoilList(...)

        wing = workplane_init.loft(combine=True)
        show(wing)
            
