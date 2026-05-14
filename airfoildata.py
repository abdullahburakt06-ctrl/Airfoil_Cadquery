import math
import numpy
import cadquery
#https://web.itu.edu.tr/~atares/courses/CA/3.1.1_NACA4.html
#link above used as reference for equations and as a starting point for coding
def naca4eq(nacastr, c, resolution):
    
    nacastr = nacastr[4:]
    ms = nacastr[0]
    ps = nacastr[1]
    ts = nacastr[2:]
    m = int(ms)
    p = int(ps)
    t = int(ts)    
    #c is chord length
    m = m*0.01
    p = 0.1*p
    t = 0.01*t 

    #Constant coefficients for NACA 4 series
    a0 =  1.4845
    a1 = -0.6300
    a2 = -1.7580
    a3 =  1.4215
    a4 = -0.5075
    
    #Functions defined to be used in the for loop
    def yt(xs):
        x = xs/c
        return t*c*(a0*pow(x, 1/2)+a1*x+a2*pow(x, 2)+a3*pow(x, 3)+a4*pow(x, 4))
    def yc(x):
        if x/c < p:
            return c*m/(p**2)*(2*p*x/c-pow(x/c, 2))
        else:
            return c*m/pow(1-p, 2)*((1-2*p)+2*p*x/c-pow(x/c, 2))
    def dycdx(x):
        if x/c < p:
            return 2*m/pow(p, 2)*(p-x/c)
        else:
            return 2*m/pow(1-p, 2)*(p-x/c)

    #Assumes linearly distributed control points, may not be optimal/can be changed    
    x = numpy.linspace(0,c,resolution)

    xu = numpy.zeros(resolution)
    xl = numpy.zeros(resolution)
    yu = numpy.zeros(resolution)
    yl = numpy.zeros(resolution)

    #Main for loop to determine variables
    for i in range(resolution):
        theta = numpy.arctan(dycdx(x[i]))
        xu[i] = x[i] - yt(x[i])*numpy.sin(theta)
        xl[i] = x[i] + yt(x[i])*numpy.sin(theta)
        yu[i] = yc(x[i]) + yt(x[i])*numpy.cos(theta)
        yl[i] = yc(x[i]) - yt(x[i])*numpy.cos(theta)
    xlt = xl[::-1]
    ylt = yl[::-1]
    xl = xlt
    yl = ylt
    xset = numpy.concatenate((xu, xl), axis=0)
    yset = numpy.concatenate((yu, yl), axis=0)
    return [xset, yset]


  



    
