# Codes for parsing dssp file for helical segment
# Command >> python helixSeg.py helixPdb.txt /location of DSSP folder/
# helixPdb.txt file data format(tab delimited): pdbId  chain	scopHierarchy	sequenceAssignedByScop
# Copyright () 2013 Ankesh Kumar Thakur
# Email: ankeshth@gmail.com


import sys
import os

def findHelixDssp(pdbId, chain, scopH, scopSeq, dssp):
  helixStart = 'no'							# To check pointer is inside the helix
  helixEnvironment = 'no'						# To check if helix exists in the seq
  seqNum = ''
  count = 0
  #chainAdjust = 0
  dsspFile = str(sys.argv[2]) + dssp
  if os.path.exists(dsspFile):						# Check if the file exists in the folder
    dssp = open(dsspFile) 
    for line in dssp:
      lineSeq = line.replace("  ", ' ').split()
      if len(lineSeq) == 19 and lineSeq[-1] == 'Z-CA':			# The last entry
        break
    for line in dssp:
      item = line.replace("  ", ' ').split()
      '''if '!' in item[1]:
        chainAdjust += 1
        continue'''
      if item[4] == 'H' and helixStart == 'no' and item[2] == chain.upper():
        helixStart = 'yes'
        helixEnvironment = 'yes'
        #seqNum += str(int(item[0]) - chainAdjust) + ':'			# Exclude the occurence of !* or !
        seqNum += str(int(item[0])) + ':'
        count +=1
      elif item[4] != 'H' and helixStart == 'yes' and item[2] == chain.upper():
        helixStart = 'no'
        #seqNum += str(int(item[0]) - chainAdjust - 1) + ','		# Pointer is pointing to an AA which is ahead of last Helix so -1
        seqNum += str(int(item[0]) - 1) + ','
    '''if helixEnvironment == 'yes':
      print pdbId + '\t' + chain + '\t' + scopH + '\t' + scopSeq.replace('\n','') + '\t' + seqNum'''
  return count

def main():
  pdbId = []
  count = 0
  pdbList = open(sys.argv[1])
  for line in pdbList:
    pdbId = line.split('\t')
    count += findHelixDssp(pdbId[0], pdbId[1], pdbId[2], pdbId[3], pdbId[0]+'.dssp')
    if pdbId == 'A':
      print 'yes ' + pdbId[0] +' '+ pdbId[1] + ' '+ pdb[2]
      break
  print count
  
if __name__ == '__main__':
    main()
