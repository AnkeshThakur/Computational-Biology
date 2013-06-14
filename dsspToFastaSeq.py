# Codes for parsing Amino Acid Sequence from dssp file in FASTA format
# Copyright () 2013 Ankesh Kumar Thakur
# Email: ankeshth@gmail.com


import sys

def main():
  pdbId = ''
  dssp = open(sys.argv[1])
  
  chain = 'A'  							# Default chain assignment
  
  for line in dssp:							# PDBId identification
    hearderLine = line.replace("  ", ' ').split()
    if hearderLine[0] == 'HEADER':
      pdbId = hearderLine[-2]
      break
        
  print '>'+ pdbId + ':' + chain + '|PDBID|CHAIN|SEQUENCE'		#>4HHB:A|PDBID|CHAIN|SEQUENCE
  
  for line in dssp:
    lineSeq = line.replace("  ", ' ').split()
    if len(lineSeq) == 19 and lineSeq[-1] == 'Z-CA':			# The last entry
      break
  for line in dssp:
    item = line.replace("  ", ' ').split()
    if item[2] != chain and item[2].isalpha():
      chain = item[2]
      print '\n>'+ pdbId + ':' + chain + '|PDBID|CHAIN|SEQUENCE '
    if item[3].isalpha():
      print item[3],
   
  
if __name__ == '__main__':
    main()
