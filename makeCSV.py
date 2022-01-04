from numpy import *
import pandas as pd 

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str


def getEasyData(fname):
 data= loadtxt(fname)
 spins = data[:,0]
 val = data[:,1]
 error = data[:,2]
 return spins,val,error

def getS2Data(fname):
 data= loadtxt(fname)
 spins = data[1:,0]
 val = data[1:,2]
 error = data[1:,3]
 return spins,val,error

def getRX(val):
  RX = []
  for i in range(len(val)):
   if val[i] != ' ':
    RX.append(float(reverse(val[i])[:5]))
   else:
    RX.append(nan)
  return RX


def getRXerr(val):
  RXerr = []
  for i in range(len(val)):
   if val[i] != ' ':
    RXerr.append(float(reverse(val[i])[6:11]))
   else:
    RXerr.append(nan)
  return RXerr




def getrexData(fname):
 rx  = []
 rxerr = []
 newval = []
 data = open(fname,"r").readlines()
 for i in range(len(data)):
  val =(reverse(str(data[i]))[:18])
  if val.count('x') == 2:
   newval.append(val)
  else:
   newval.append(' ')
 return newval
r1x,r1val,r1err = getEasyData('Input/r1.dat')
r2x,r2val,r2err = getEasyData('Input/r2.dat')
noex,noeval,noeerr = getEasyData('Input/noe.dat')
s2x, s2val, s2err = loadtxt('Input/spinS2.dat')[:],loadtxt("Input/S2.dat")[:],loadtxt("Input/S2err.dat")[:]
rxraw = getrexData('Input/rexX.dat')
rx = asarray(getRX(rxraw))
rxerr = asarray(getRXerr(rxraw))


E1O4K_Data = {'Spins':r1x,'R1':r1val,'R1_Error':r1err,'R2':r2val,'R2_Error':r2err,'NOE':noeval,'NOE_Error':noeerr,'S2':s2val,'S2_Error':s2err,'Rex':rx,'Rex_Error':rxerr}



E1O4K_Data = pd.DataFrame(E1O4K_Data)
E1O4K_Data.to_csv('E1O4K_Data.csv', encoding='utf-8', index=False)
