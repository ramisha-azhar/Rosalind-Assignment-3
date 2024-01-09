def calculate_failure_array(s):
    n = len(s)
    failure_array = [0] * n

    j = 0
    for k in range(2, n + 1):
        while j > 0 and s[j] != s[k - 1]:
            j = failure_array[j - 1]
        if s[j] == s[k - 1]:
            j += 1
        failure_array[k - 1] = j

    return failure_array

def fasta_to_string(filename):
    file = open(filename)
    rawdata = {}
    names = []
    sequences = []
    for line in file:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            rawdata[name] = ''
        else:
            rawdata[name] += line.rstrip('\n')

    
    for item in rawdata.keys():
        names.append(item)

   
    for key in names:
        sequences.append(str(rawdata[key]))

    return str(sequences[0])

def main():
    
    dna_string = fasta_to_string('rosalind_kmp.txt')

    
    result = calculate_failure_array(dna_string)

    
    with open('output.txt', 'w') as output_file:
        output_file.write(" ".join(map(str, result)))

if __name__ == "__main__":
    main()