# Program for parsing Amino Acid Sequences from pdb file in fasta format
# Copyright () 2013 Ankesh Kumar Thakur
# Email: ankeshth@gmail.com

import sys

def main():
  pdbId = ''
  pdb = open(sys.argv[1])
  aaCode = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}    # One letter code for Amino Acids
  chain = 'A'  							# Default chain assignment
  
  for line in pdb:							# PDBId identification
    hearderLine = line.replace("  ", ' ').split()
    if hearderLine[0] == 'HEADER':
      pdbId = hearderLine[-1]
      break
        
  print '>'+ pdbId + ':' + chain + '|PDBID|CHAIN|SEQUENCE'		#>4HHB:A|PDBID|CHAIN|SEQUENCE
  
  for line in pdb:
    lineSeq = line.replace("  ", ' ').split()
    if lineSeq[0] == 'SEQRES' :
      for itemIndex in range(4, len(lineSeq)):
        if lineSeq[2] != chain:
          chain = lineSeq[2]
          print '\n>'+ pdbId + ':' + chain + '|PDBID|CHAIN|SEQUENCE'			
        print aaCode[lineSeq[itemIndex]],
if __name__ == '__main__':
    main()
