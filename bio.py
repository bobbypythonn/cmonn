class BioSequence:
    def __init__(self, sequence_type, sequence):
        self.sequence_type = sequence_type
        self.sequence = sequence

def insert(sequence_array, pos, sequence_type, sequence):
    if pos < 0 or pos >= len(sequence_array):
        print("Error: Position out of bounds")
        return

    if sequence_type == "DNA" and not all(base in "ACGT" for base in sequence):
        print("Error: Invalid DNA sequence")
        return
    elif sequence_type == "RNA" and not all(base in "ACGU" for base in sequence):
        print("Error: Invalid RNA sequence")
        return

    sequence_array[pos] = BioSequence(sequence_type, sequence)

def print_sequences(sequence_array):
    for i, bio_sequence in enumerate(sequence_array):
        if bio_sequence:
            print(f"Position {i}: Type {bio_sequence.sequence_type}, Sequence {bio_sequence.sequence}")

def print_sequence_at_pos(sequence_array, pos):
    if pos < 0 or pos >= len(sequence_array) or not sequence_array[pos]:
        print("Error: No sequence at this position")
        return

    bio_sequence = sequence_array[pos]
    print(f"Position {pos}: Type {bio_sequence.sequence_type}, Sequence {bio_sequence.sequence}")

def remove(sequence_array, pos):
    if pos < 0 or pos >= len(sequence_array):
        print("Error: Position out of bounds")
        return

    sequence_array[pos] = None

def copy(sequence_array, pos1, pos2):
    if pos1 < 0 or pos1 >= len(sequence_array) or not sequence_array[pos1]:
        print("Error: No sequence at source position")
        return

    sequence_array[pos2] = BioSequence(sequence_array[pos1].sequence_type, sequence_array[pos1].sequence)

def swap(sequence_array, pos1, start1, pos2, start2):
    if pos1 < 0 or pos1 >= len(sequence_array) or not sequence_array[pos1] or \
       pos2 < 0 or pos2 >= len(sequence_array) or not sequence_array[pos2]:
        print("Error: One or both positions do not contain a sequence")
        return

    seq1 = sequence_array[pos1].sequence
    seq2 = sequence_array[pos2].sequence

    if sequence_array[pos1].sequence_type != sequence_array[pos2].sequence_type:
        print("Error: Sequences are not of the same type")
        return

    if start1 < 0 or start1 > len(seq1) or start2 < 0 or start2 > len(seq2):
        print("Error: Invalid start position")
        return

    new_seq1 = seq1[:start1] + seq2[start2:]
    new_seq2 = seq2[:start2] + seq1[start1:]

    sequence_array[pos1].sequence = new_seq1
    sequence_array[pos2].sequence = new_seq2

def transcribe(sequence_array, pos):
    if pos < 0 or pos >= len(sequence_array) or not sequence_array[pos]:
        print("Error: No sequence at this position")
        return

    bio_sequence = sequence_array[pos]
    if bio_sequence.sequence_type != "DNA":
        print("Error: Transcription can only be performed on a DNA sequence")
        return

    dna_sequence = bio_sequence.sequence
    rna_sequence = ""

    for base in dna_sequence:
        if base == "T":
            rna_sequence += "U"
        elif base == "A":
            rna_sequence += "A"
        elif base == "C":
            rna_sequence += "G"
        elif base == "G":
            rna_sequence += "C"

    rna_sequence = rna_sequence[::-1]

    sequence_array[pos].sequence_type = "RNA"
    sequence_array[pos].sequence = rna_sequence

# Main program
if __name__ == "__main__":
    sequence_array = [None] * 100

    with open("command-file.txt", "r") as file:
        for line in file:
            command = line.strip().split()
            if command[0] == "insert":
                insert(sequence_array, int(command[1]), command[2], command[3])
            elif command[0] == "print":
                if len(command) == 1:
                    print_sequences(sequence_array)
                else:
                    print_sequence_at_pos(sequence_array, int(command[1]))
            elif command[0] == "remove":
                remove(sequence_array, int(command[1]))
            elif command[0] == "copy":
                copy(sequence_array, int(command[1]), int(command[2]))
            elif command[0] == "swap":
                swap(sequence_array, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
            elif command[0] == "transcribe":
                transcribe(sequence_array, int(command[1]))
