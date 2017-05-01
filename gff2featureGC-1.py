#! /usr/bin/env python3.5

# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys
import collections



# a function to clean up a DNA sequence
def clean_seq(input_seq):
    #print("first time in clean:"+ andy)
    #andy += 1
    #print("second time in clean:" + andy)
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return clean


def nuc_freq(sequence, base1,base2,sig_digs=2):
    # Calculate the length of the sequence
    length = len(sequence)

    # genome covered with the feature
    genome_cover=(len(sequence)/len(genome))*100
    
    # count the number of this nucleotide
    count_of_base1 =sequence.count(base1)

    count_of_base2 =sequence.count(base2)

    # calculate the gc content
    gc_content=((count_of_base1+count_of_base2)/length)*100

    # retun the frequence and the legth
    return (length,genome_cover,round(gc_content,sig_digs))

# Function to generate complement sequence
def reverse_compl(dna_seq):
    replacement1=dna_seq.replace('A','t')
    replacement2=replacement1.replace('T','a')
    replacement3=replacement2.replace('C','g')
    replacement4=replacement3.replace('G','c')
    return (replacement4.upper())


usage = sys.argv[0] + ": watermelon.fsa watermelon.gff"

if len(sys.argv) < 3:
    print(usage)
    sys.exit("\nThis script requires both watermelon FSA file and a watermelon GFF file\n")

watermelon_gff = sys.argv[1]
watermelon_fsa= sys.argv[2]

#print(gff + "\n"  genome)

#andy = 42
#print("Main"-1:", andy)


    
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

   #types = line.split('; type ')
    #other_type = types[len(types)-1]
    # print(other_type)
    
    fields = line.split('\t')
    type  = fields[2]
    strand=field[6]

    #print(gene[0])
    start = int(fields[3])
    end   = int(fields[4])
    
    # print(type, "\t", start, "\t", end)

    # extract this feature from the genome
    fragment = genome[start-1:end]
    
   fragment = clean_seq(fragment)
   # print(clean_seq)

   if type in feature_sequences:
        feature_sequences[type] +=fragment
    else:
        feature_sequences[type]=fragment

    if type=='CDS':
        gene_feature=fields[8]
        gene1=gene_feature.split(';')
        gene=gene1[0]
        gene_sequence=genome[start-1:end]

        if strand=='-':
            #print("Before ")
            complement_sequence=reverse_compl(gene_sequence)
            exon_sequences[gene]=complement_sequence
            #print("After ")
        else:
            exon_sequences[gene]=gene_sequence
        
    #print (clean)
    #print(gene[0])
    
#close the GFF file
gff_in.close()
    

        

# order the exon sequences
ordered_exons_sequences = collections.OrderedDict(sorted(exon_sequences.items()))
    
for exon, seq in ordered_exons_sequences.items():
    print(">", exon,"\n",seq)  #print out the exon and the sequences


    
for feature, sequence in feature_sequences.items():

    #calculate the nucleotide composition for each feature
    (feature_length,cover, feature_comp)=nuc_freq(sequence,base1='C',base2='G',sig_digs=2)
     
    print(feature.ljust(20), str(feature_length), "(%1.1f" %cover, "%)", "\t",str(feature_comp)+"%")


    




#function for reverse complement
#function for G+C
#print/store/build cds for each gene
#capture the gene name and _ + if _ call reverse function
