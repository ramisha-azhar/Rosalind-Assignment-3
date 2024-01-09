import re

with open('rosalind_ctbl (2).txt', 'r') as ctbl:
    tree = ctbl.read().strip()

def sort(labels):
    ok_labels = re.findall(r'\w+', labels)
    return sorted(ok_labels)

def char_table(tree):
    taxa_labels = sort(tree)
    l = []

    count, p, subtrees = 0, [], []

    for i, symbol in enumerate(tree):
        if symbol == '(':
            count+= 1
            p.append(i)
        elif symbol == ')':
            subtree = tree[p.pop() + 1:i]
            subtrees.extend([] for _ in range(len(subtrees), count))
            subtrees[count-1].append(subtree)
            count -= 1

    for i in range(1, len(subtrees)):
        for subtree in subtrees[i]:
            l.append([1 if label in sort(subtree) else 0 for label in taxa_labels])

    return l

for row in char_table(tree):
    print(''.join(map(str, row)))
  

