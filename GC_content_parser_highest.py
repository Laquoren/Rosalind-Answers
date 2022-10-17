from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.SeqUtils import GC

parsed_seq = SeqIO.parse("rosalind_computingGC_sample copy.txt", "fasta")


def list_of_seq_record(parsed_file):
    lis = []
    for seq_record in parsed_file:
        lis.append(seq_record)
    print(lis)
    return lis

def gc_content(seq):
    count = 0
    for l in seq:
        if l == "C":
            count += 1
        elif l == "G":
            count += 1
    return count/len(seq) * 100

def gc_content_for_dic(parsed_file):
    out = {}
    for obj in parsed_file:
        ans = gc_content(obj.seq)
        out[obj.id] = ans
    print(out)
    return out


list1 = list_of_seq_record(parsed_seq)

x = gc_content_for_dic(list1)

# print(max(x) + " " + str(x.get(max(x))))

# highest = 0
# for num in x:
#     if num > highest:
#         highest = num
