#! /usr/bin/env python3.5

# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys

usage = sys.argv[0] + ": watermelon.fsa watermelon.gff"

if len(sys.argv) < 3:
    print(usage)
    sys.exit("\nThis script requires both watermelon FSA file and a watermelon GFF file\n")

watermelon_gff = sys.argv[1]
watermelon_fsa= sys.argv[2]

#print(gff + "\n" + genome)

#andy = 42
#print("Main"-1:", andy)

# a function to clean up a DNA sequence
def clean_seq(input_seq):
    #print("first time in clean:"+ andy)
    #andy += 1
    #print("second time in clean:" + andy)
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return clean


def nuc_freq(sequence, base, sig_digs=2):
    # Calculate the length of the sequence
    length = len(sequence)
    
    # count the number of this nucleotide
    count_of_base = count(base)

    # Calculate the base frequencey
    feq_of_base = count_of_base/length
    
    # return the frequency and the length
    return (length, round(freq_of _base, sig_digs))
    
    


# declare the file names
gff_file = 'watermelon.gff'
fsa_file = 'watermelon.fsa'

# open the files for reading
gff_in = open(gff_file, 'r')
fsa_in = open(fsa_file, 'r')

# declare variable that will hold the genome sequence
genome = ''

# initialize a line counter
line_number = 0

# read in the genome file
for line in fsa_in:
    # print(str(line_number) + ": " + line)

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    if line_number > 0:
        genome = genome + line

    # increment line_number
    line_number += 1

# did we get the genome correctly?
# print(len(genome))
    
# close the genome file
fsa_in.close()

cds     = ''
trna    = ''
rrna    = ''
intron  = ''
misc    = ''
repeats = ''

# read in the GFF file
for line in gff_in:

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    fields = line.split('\t')
    type  = fields[2]
    start = int(fields[3])
    end   = int(fields[4])
    
    # print(type, "\t", start, "\t", end)

    # extract this feature from the genome
    fragment = genome[start-1:end]
    
   fragment = clean_seq(fragment)
   # print(clean_seq)

    

    if type == 'CDS':
        cds += fragment

    if type == 'intron':
        intron += fragment

    if type == 'misc_feature':
        misc += fragment

    if type == 'repeat_region':
        repeats += fragment

    if type == 'rRNA':
        rrna += fragment

    if type == 'tRNA':
        trna += fragment
#for feature_type in list_of _features:
types =[cds, intron,misc,repeats,rrna,trna]

# loop over the 4 nucleotides
dict={

'exon':types[0],'intron':types[1],'misc_feature':types[2],'repeat_region':types[3],'rRNA':types[4],'tRNA':types[5]}
print("length and nucleotide composition of each feature type")
for feature_type, seq in dict.items():
    for nucleotide in ('A','C','G','T'):
        #calculate the nucleotide composition for each feature
        (feature_length,feature_comp)=nuc_freq(seq,base=nucleotide,sig_digs=2)
       
print(feature_type.ljust(20)+ str(feature_length)+"\t"+nucleotide+ " "+str(feature_comp))


# print the output
#print(cds.count('G'))
#print(cds.count('C'))
    

# close the GFF file
gff_in.close()
