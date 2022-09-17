def gc_content(seq):
    count = 0
    for l in seq:
        if l == "C":
            count += 1
        elif l == "G":
            count += 1
    return count/len(seq) * 100

# test with Rosalind sample data
print(gc_content("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"))

