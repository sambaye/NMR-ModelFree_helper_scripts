I have coded up a few scripts in order to make analyzing the output of 
of NMR modelfree experiments a little easier. Take a look at the final output file of my protein("tem-1_E104K_800MHz.iter13.par"), It is very hard to deal with :(.

It is especially difficult to extract the exchange value("Rex") so I decided to semi-automate the process.

All you need now are the previously formatted files and some slight tinkering and my 
scripts will give you an easy to read csv file(check out my example CSV file). 


#Sample input files are located in the "Input" directory.

r1.dat: longitudinal relaxation formatted the following way (spin #, data height, error)
r2.dat: transverse relaxation formatted the following way (spin #, data height, error)
noe.dat: NOE experiment data formatted the following way (spin #, data height, error)
par.dat: I simply copied the unweildy "tem-1_E104K_800MHz.iter13.par" and removed the first line. 

If you have these files formatted the proper way you can easily get the desired csv file. 

# Commands and tips on how to get CSV files
0. pip install numpy 

0.1 pip install pandas

1. bash makeCHI.sh:
(you might have to sligtly modify the output files if there are some length descrepancies between your other input files) 

2. python makeREX.py:
(you might have to sligtly modify the output files if there are some length descrepancies between your other input files )

3. mv *.dat Input/

4. python makeCSV.py   
