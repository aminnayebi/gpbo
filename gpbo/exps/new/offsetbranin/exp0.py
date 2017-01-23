import gpbo
import numpy as np
import scipy as sp
#mode='run'
mode=['run','plot'][1]
vers=[2,3][0]
D=2

s=1e-6
lb = sp.array([-1.,-1.])
ub = sp.array([1.,1.])

from objective import f

from objective import truemin
all2confs=[]
all3confs=[]
rpath='results0'
#-----------------------
#eimle
C=gpbo.core.config.eimledefault(f,D,12,s,rpath,'null.csv')
C.aqpara['nrandinit']=10
C.stoppara = {'tmax': 60*50}
C.stopfn = gpbo.core.optimize.totaltstopfn

all2confs.append(['eimle',C])

#----------------------
#pesfs
C=gpbo.core.config.pesfsdefault(f,D,12,s,rpath,'null.csv')
C.stoppara = {'tmax': 60*1}
C.aqpara['nrandinit']=10
C.stopfn = gpbo.core.optimize.totaltstopfn

#all2confs.append(['pesfs',C])

#-----------------
#pesbs
C=gpbo.core.config.pesbsdefault(f,D,50,s,rpath,'null.csv')
C.stoppara = {'tmax': 60 * 50}
C.stopfn = gpbo.core.optimize.totaltstopfn
C.aqpara['overhead']='last'
C.aqpara['nrandinit']=20


all2confs.append(['pesbs',C])

#-----------------
#mtbo
C={'lowtask':2,
   'ninit':15,
   'nsteps':50}

all3confs.append(['mtbo2',C])

#-----------------
#mtbo
C={'lowtask':4,
   'ninit':10,
   'nsteps':11}

#all3confs.append(['mtbo4',C])

#-----------------
#mtbo
C={'lowtask':8,
   'ninit':15,
   'nsteps':50}

all3confs.append(['mtbo8',C])
#---------------
#fabolas
C={'ninit':20,
   'nsteps':60}
#all3confs.append(['fabolas',C])

if mode=='run':
    if vers==2:
        gpbo.runexp(f,lb,ub,rpath,1,all2confs)
    else:
        gpbo.runexp(f,lb,ub,rpath,1,all3confs)
elif mode=='plot':
    gpbo.plotall(all2confs+all3confs,1,rpath,trueopt=truemin)
else:
    pass