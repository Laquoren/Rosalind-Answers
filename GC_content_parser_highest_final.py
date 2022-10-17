from Bio import SeqIO


parsed_seq = SeqIO.parse("rosalind_gc (1).txt", "fasta")


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

t = max(x, key=x.get)
# to get max() to iterate over the values, you need to use get without () - same as max(x) for keys

v = x.get(t)

print(t + " " + str(v))

# for function for getting the highest value in a list
# highest = 0
# for num in list:
#     if num > highest:
#         highest = num
