#! /home/sandip/anaconda3/bin/python

# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys

## for argument in sys.argv:
##     print(argument)

## sys.exit()

usage = sys.argv[0] + ": watermelon.fsa watermelon.gff"

if len(sys.argv) < 3:
    print(usage)
    sys.exit("\nThis script requires both a watermelon.fsa file and a watermelon.gff file\n")

watermelon_fsa = sys.argv[1]
watermelon_gff = sys.argv[2]


#print(gff + "\n" + genome)

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

genome_length = len(genome)

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

# print the output
# G count of different features
cds_g_count= cds.count('G')
intron_g_count= intron.count('G')
misc_g_count= misc.count('G')
repeats_g_count= repeats.count('G')
rrna_g_count= rrna.count('G')
trna_g_count= trna.count('G')

# C count of different features
cds_c_count= cds.count('C')
intron_c_count= intron.count('C')
misc_c_count= misc.count('C')
repeats_c_count= repeats.count('C')
rrna_c_count= rrna.count('C')
trna_c_count= trna.count('C')

#G+C count of different features
cds_gc_count = (cds_g_count + cds_c_count)
intron_gc_count = (intron_g_count + intron_c_count)
misc_gc_count = (misc_g_count + misc_c_count)
repeats_gc_count = (repeats_g_count + repeats_c_count)
rrna_gc_count = (rrna_g_count + rrna_c_count)
trna_gc_count = (trna_g_count + trna_c_count)

# lenght of differnt features
length_cds = len(cds)
length_intron = len(intron)
length_misc = len(misc)
length_rrna = len(rrna)
length_repeats = len(repeats)
length_trna = len(trna)

# GC ratio of differnt features
gc_content_cds_ratio = (cds_gc_count/length_cds)*100
gc_content_intron_ratio = (intron_gc_count/length_intron)*100
gc_content_misc_ratio = (misc_gc_count/length_misc)*100
gc_content_rrna_ratio = (rrna_gc_count/length_rrna)*100
gc_content_repeats_ratio = (repeats_gc_count/length_repeats)*100
gc_content_trna_ratio = (trna_gc_count/length_trna)*100

#ratio of different features
CDS_ratio =(length_cds/genome_length)*100
intron_ratio =(length_intron/genome_length)*100
misc_ratio =(length_misc/genome_length)*100
rrna_ratio =(length_rrna/genome_length)*100
repeats_ratio =(length_repeats/genome_length)*100
trna_ratio =(length_trna/genome_length)*100


print("CDS", "          ", length_cds, "(",round (CDS_ratio,1),"%)",round (gc_content_cds_ratio, 2))
print("intron","       ", length_intron, "(", round (intron_ratio,1), "%)", round (gc_content_intron_ratio, 2))
print("misc_feature"," ", length_misc, "(", round (misc_ratio,1), "%)", round (gc_content_misc_ratio, 2))
print("rRNA","         ", length_rrna,"", "(", round (rrna_ratio,1), "%)", round (gc_content_rrna_ratio, 2))
print("repeat_regions",length_repeats, "(",round (repeats_ratio,1),"%)", round ( gc_content_repeats_ratio, 2))
print("tRNA","         ", length_trna,"", "(", round (trna_ratio,1),"%)", round (gc_content_trna_ratio, 2))


# close the GFF file
gff_in.close()
