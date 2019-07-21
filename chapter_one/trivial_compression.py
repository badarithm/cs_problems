from typing import Generator
from sys import getsizeof

class CompressedGene():
    def __init__(self, gene: str) -> None:
        self.compress(gene)

    def compress(self, gene: str) -> None:
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            self.bit_string <<= 2 # shift left two bits

            if "A" == nucleotide:
                self.bit_string |= 0b00
            elif "C" == nucleotide:
                self.bit_string |= 0b01
            elif "G" == nucleotide:
                self.bit_string |= 0b10
            elif "T" == nucleotide:
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid nucleotide : {}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ''

        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits: int = self.bit_string>>i&0b11 # just 2 relevant bits
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits : {}".format(bits))
            return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()

original: str = "TAGATAGATAGATAGATCTCTG" * 100
compressed: CompressedGene = CompressedGene(original)

print("original is {} bytes ".format(getsizeof(original)))
print("compressed is {} bytes".format(getsizeof(compressed)))
print("decompressed is {} bytes".format(getsizeof(compressed.decompress())))

print("original and decompressed are the same: {}".format(original == compressed.decompress()))