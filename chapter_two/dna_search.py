from enum import IntEnum
from typing import Tuple, List, Optional

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]

Gene = List[Codon]

def string_to_codon(string: str) -> Optional[Codon]:
    if 3 >= len(string) :
        return (Nucleotide[string[0]], Nucleotide[string[1]], Nucleotide[string[2]])
    return None

def string_to_gene(string: str) -> Gene:
    string_length = len(string)
    codons: List[int] = [i for i in range(0, len(string), 3) if (2 + i < string_length)]
    return [(Nucleotide[string[c_i]], Nucleotide[string[c_i + 1]], Nucleotide[string[c_i + 2]]) for c_i in codons]

def contains_linear(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def contains_binary(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1

    while(low <= high):
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid -1
        else:
            return True

    return False

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
gene: Gene = string_to_gene(gene_str)
acg: Codon = string_to_codon("ACG")
gat: Codon = string_to_codon("GAT")

sorted_gene: Gene = sorted(gene)
