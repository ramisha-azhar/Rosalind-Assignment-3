taxa = ['Balaena_leptochelis', 'Chalcides_uncia', 'Charadrius_asperum', 'Lamprolepis_arvensis','Ptyodactylus_deremensis', 'Sternotherus_colubrinus', 'Streptopelia_cinclus']

trees = [['(', '(', taxa[1], ',', taxa[2], ')', ')', taxa[0], ';']]

new_items = taxa[3:]

def maketree(lst, new_taxa):
    new_tree = []
    for i in range(1,len(lst)-2):
        j = -1
        if not lst[i] in '(),;':
            j = i
        if lst[i]=='(':
            m=1
            for j in range(i+1, len(lst)):
                if lst[j]=='(':
                    m +=1
                elif lst[j]==')':
                    m -=1
                if m == 0:
                    break
        if j!=-1:
            t =  lst[:i] + ['('] + lst[i:j+1] + [','] + [new_taxa] + [')'] + lst[j+1:]
            new_tree.append(t)
    return new_tree

for new_taxa in new_items:
    t = []
    for tree in trees:

        t2 = maketree(tree, new_taxa)
        t = t + t2
    trees = t[:]

for tree in trees:
    print (''.join(tree))

   