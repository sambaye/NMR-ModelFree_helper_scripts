#!/bin/bash 

# Extract Chi Squared Values From ModelFree output file. 
awk '{ print $1 }' 'Input/par.dat' > spinS2.dat
awk '{ print $3 }' 'Input/par.dat' > S2.dat
awk '{ print $4 }' 'Input/par.dat' > S2err.dat

mv *.dat Input/ 
