#!/usr/bin/env python

# import libraries
import sys, re
from argparse import ArgumentParser
from collections import Counter

# input
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = 
"Input sequence")

# classify the sequence
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()  
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print ('The sequence is RNA')
    elif re.search('U', args.seq) and re.search('T', args.seq):
        print ('The sequence is not DNA nor RNA')
    else:
        print ('The sequence can be DNA or RNA')
# adding conditions improve the sequence classifier

# nucleotide %
nucleotide_counter = Counter(args.seq)
nucleotide_percent = {nucleotide: round(count/len(args.seq)*100, 2) for nucleotide, count in nucleotide_counter.items()}
nucleotide_percent_sorted = dict(sorted(nucleotide_percent.items(), key=lambda x: x[1], reverse=True))
print("Percentage of each nucleotide in the sequence:")
for nucleotide, percent in nucleotide_percent_sorted.items():
    print(f"{nucleotide}: {percent}%")
