import os
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

os.system ("tr [:upper:] [:lower:] < ../TextFiles/warandpeace.txt | sed 's/[^a-z]//g' | tr -d [:cntrl:] | sed 's/.\{1\}/& /g' | tr ' ' '\n' |sort | uniq -c >> ../TextFiles/raw.txt" )

RAWTEXT = open('../TextFiles/raw.txt')

for line in RAWTEXT:
    frequency, letter = line.split()
    plt.bar(letter, int(frequency), color = "black")

plt.show()




