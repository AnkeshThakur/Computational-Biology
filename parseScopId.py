# Synopsis: This piece of code is written for extracting PDB ids from dir.des.scop.txt available at SCOP server as a part of 
# project "Prediction of Amphipathic Helices using Machine Learning Approach"
# Labels are cl (class), cf (fold), sf (superfamily), fa (family), dm (protein domain), sp (species), and px (domain entry)
# Copyright (C) 2013 Ankesh Kumar Thakur

import sys

def main():
  pdbDetails = ''

  scop = open(sys.argv[1])
  node = ['a', 'b', 'c', 'd', 'e']

  for line in scop:
    pdbId = line.split("\t")
    if len(pdbId) == 5 and pdbId[1] == 'px' and (pdbId[2][0] in node):
      pdbDetails = pdbId[-1].replace(':', ' ').split()
      if len(pdbDetails) == 2:
        print pdbDetails[0] + '\t' + pdbDetails[1] + '\t' + pdbId[2][0] + '\t0-0'
      elif pdbDetails[2].find('-') > 0:  			#data may be of this kind 1jmu C:,D:
	print pdbDetails[0] + '\t' + pdbDetails[1] + '\t' + pdbId[2][0] +  '\t' + pdbDetails[2]

	  
if __name__ == '__main__':
    main()
