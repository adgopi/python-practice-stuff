def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """(str) -> bool
​
    Return True if and only if the DNA sequence dna contains no characters
    other than 'A', 'T', 'C' and 'G'
    
    >>> is_valid_sequence('ATCGACG')
    True
    >>> is_valid_sequence('BDKX')
    False
    """
    for nucleotide in dna:
        if nucleotide != 'A' and nucleotide != 'T' and nucleotide != 'C' and nucleotide != 'G':
            return False
    return True

def insert_sequence(dna1, dna2, index):
    """(str, str, int) -> str
    
    Returns the DNA sequence obtained by inserting the second DNA
    sequence dna2 into the first DNA sequence dna1 at the given index.
    
    >>>insert_sequence('CCGG', 'AT' , 2)
    'CCATGG'
    >>>insert_sequence('CCTTGG', 'AT' , 3)
    'CCTATTGG'
    """
    return dna1[0:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """(str) -> str

    Returns the input nucleotide's complement
    
    >>>get_complement('A')
    'T'
    >>>get_complement('T')
    'A'
    >>>get_complement('G')
    'C'
    >>>get_complement('C')
    'G'
    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'C':
        return 'G'

def get_complementary_sequence(dna):
    """(str) -> str

    Returns the input DNA sequence's complementary DNA sequence

    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('ACGTACG')
    'TGCATGC'
    """
    complement = ''
    for nucleotide in dna:
        complement = complement + get_complement(nucleotide)
    return complement



    
