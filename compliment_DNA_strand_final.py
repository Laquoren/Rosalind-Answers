dna_bases = {
    "A": "T",
    "G": "C",
    "C": "G",
    "T": "A"
}

def reverse(str1):
    return str1[::-1]

def compliment(dna):
    for letter in dna:
        print(dna_bases.get(letter), end="")

# paste data from Rosalind here
ex1 = "GGTACTAGATGC"

x = reverse(ex1)
compliment(x)
