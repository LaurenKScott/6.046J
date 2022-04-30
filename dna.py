'''
'''


# dna_seq = a string of characters corresponding to nucleotide bases in DNA (a, t, c, g)
def transcribe(dna_seq):
    to_rna = {'A':'U', 'T':'A', 'C':'G', 'G': 'C'}
    rna_seq = ""
    for char in dna_seq:
        try:
            rna_seq += to_rna[char.upper()]
        except KeyError:
            print('ERROR. INVALID BASE:', char, 'at index', dna_seq.find(char))
            return None
    return rna_seq

# Maps 3-letter codon to 1-letter amino acid abbr
def translate(rna_seq):
    codons = {x: x+1 for x in range(10)}
    # want to compare all 3 letter sequences in rna using sliding window
    for i in range(len(rna_seq)-2):
        window = rna_seq[i:i+3]
        print(window)
    print(codons)
translate(transcribe('tgcgctctaactttctcggactcaaagccc'))