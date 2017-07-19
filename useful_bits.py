import numpy					#starts numpy
from numpy import genfromtxt			#loads text importer
a = genfromtxt('pcpe_rmsd_g_mono-a.xvg')	#reading in file
np.std(a[:,1])					#standard deviation. The [:,n] 
						#processes only the nth (zero indexed) column
np.mean(a[:,1])					#ditto, but for mean


a = genfromtxt('pcpe_rmsd_g_mono-a.xvg')
tmp=numpy.mean(data,axis=1)
numpy.savetxt('file.out', tmp) 
	or
numpy.savetxt('file.out', numpy.mean(data,axis=1))


import numpy as np				#running average
from numpy import genfromtxt		#a is data
a = genfromtxt('test_c.dat')		#N is window size
N = 1000
def running_mean(a, N):
    cumsum = np.cumsum(np.insert(a,0,0))
    return (cumsum[N:] - cumsum[:-N]) / N
np.savetxt('file.out', running_mean(a, N))


arrayvar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for var in arrayvar:

import numpy as np
a = np.genfromtxt('ce_a_theta.dat')
b = np.genfromtxt('ce_b_theta.dat')
from scipy.stats import linregress
linregress(a, b)
linregress(a, b[,:7])	#[,:7] gives 7th col. useful for the mindist and correlation
LinregressResult(slope=0.07658085801000937, intercept=26.765424436315683, rvalue=0.15023530211591166, pvalue=0.0, stderr=0.0015936505371346812)

import sys
firstarg=sys.argv[1]
secondarg=sys.argv[2]
thirdarg=sys.argv[3]
