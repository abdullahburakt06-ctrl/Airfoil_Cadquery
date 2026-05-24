import cadquery as cq
import numpy as np
from cadquery.vis import show

def airfoilList(afdata, wconstr, swept, dihedral):
   
    if len(afdata) != len(wconstr):
        ValueError
    else:
        rangevalue = len(wconstr)
        workplane_init = cq.Workplane()
        for i in range(rangevalue):
            pos = wconstr[i][0]
            c = wconstr[i][3]

            xvals = afdata[i][0] + swept*pos
            yvals = afdata[i][1]

            xytuple = list(zip(xvals, yvals))

            lastpos = wconstr[i][1]
            twist = wconstr[i][2]
            print("Iteration complete: " + str(i))

            #trial
            n = len(xytuple)
            nhalf = int(n/2)

            xytuple1 = xytuple[0:nhalf]
            xytuple2 = xytuple[nhalf::]

            #determine radius necessary for radiusArc
            xStart = xytuple1[-1][0]
            yStart = xytuple1[-1][1]
            xEnd = xytuple2[0][0]
            yEnd = xytuple2[0][1]

            arcRad = np.sqrt(pow(xStart - xEnd, 2) + pow(yStart-yEnd, 2))/2

            (
                workplane_init
                .workplane()
                .transformed((0, 0, twist), offset=(pos*swept, dihedral*pos, pos))
                .lineTo(xvals[0], yvals[0], forConstruction=True)
                .spline(xytuple1)
                .radiusArc((xytuple2[0][0], xytuple2[0][1]), arcRad)
                .spline(xytuple2)
                .close()
            )

        wing = workplane_init.loft(combine=True, clean=True)
        show(wing)
        return(wing)
            

