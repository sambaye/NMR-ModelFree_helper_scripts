import numpy as np

def getEasyData(fname):
 data= np.loadtxt(fname)
 spins = data[:,0]
 val = data[:,1]
 error = data[:,2]
 return spins,val,error

def getS2Data(fname):
 data= np.loadtxt(fname)
 spins = data[1:,0]
 val = data[1:,2]
 error = data[1:,3]
 return spins,val,error

def fixstr(val):
 newval = " "
 for i in range(len(val)):
  if val[i] == "\t" or val[i] == '':
   newval += 'x'
  else:
   newval += val[i]
 return newval[:len(newval)-1]

def getrexData(fname):
 data = open(fname,"r").readlines()
 rexX = open("rexX.dat","w")
 for i in range(len(data)):
  vals = fixstr(str(data[i]))
  rexX.write(vals+"\n")
 return 0

a = getrexData('Input/par.dat')
