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
    num = 0
    
    for char in dna:
        if char == nucleotide:
            num = num + 1
    return num


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    >>>> contains_sequence('AAGGTTCC', 'AA')
    
    

    """
    return dna1.find(dna2) >= 0
    
def is_valid_sequence(s):    

    """ (str) -> bool

    Returns True is the sequence contains only DNA letters. 

    >>>>is_valid_sequence('ATCG')
    True
    >>>>is_valid_sequence('ATCP')
    False
    >>>>is_valid_sequence('aTCG')
    False
    >>>>is_valid_sequence('ATCGGTCAGGTCACGTA')
    True
    """
    num = 0

    if s == '':
        return True

    if not s.isupper():
        return False
        
    for char in s:
        if not char in 'ATCG':
            num = num + 1
    return num <= 0


def insert_sequence(str1, str2, num):

    """ (str, str, int) -> str

    Returns a string that contains string1 with string2 inserted in a numbered place. 

    >>>>insert_sequence('CCGG','AT',2)
    CCATGG
    >>>>insert_sequence('CCGG','TT', 0)
    TTCCGG
    >>>>insert_sequence('CCGG','AA',4)
    CCGGAA    
    """
    return str1[:num] + str2 + str1[num:]


def get_complement(ntide):

    """ (str) -> str

    Returns a string that shows the complement of a given nucleotide.
    
    >>>>get_complement(A)
    T
    >>>>get_complement(T)
    A
    >>>>get_complement(C)
    G
    >>>>get_complement(G)
    C
    """
    result = ''
    
    if ntide == 'A':
        result = 'T'
    elif ntide == 'T':
        result = 'A'
    elif ntide == 'C':
        result = 'G'
    elif ntide == 'G':
        result = 'C'

    return result



def get_complementary_sequence(dnaseq):

    """(str) -> str

    >>>>get_complementary_sequence('GGTTAACC')
    CCAATTGG
    >>>>get_complementary_sequence('GGGGGGGG')
    CCCCCCCC
    >>>>get_complementary_sequence('GATACA')
    CTATGT
    """
    
    result = ''

    for char in dnaseq:
        result = result + get_complement(char)
    return result
