""""

Reverse Complement Problem: Find the reverse complement of a DNA string.

    Input: A DNA string Pattern.
    Output: Patternrc , the reverse complement of Pattern.


"""

def reverse_complement(seq: str) -> str:

    compl: dict[str, str] = {"A": "T", "T": "A", "C": "G", "G": "C"}
    rev_comp_seq:str = ""
    for nuc in seq[::-1]:
        rev_comp_seq+=compl[nuc]
    return rev_comp_seq


def reverse_complement_naive(seq: str) -> str:

    rev_comp_seq: list[str] = []
    for nuc in seq[::-1]:
        if nuc == "A":
            rev_comp_seq.append("T")
        elif nuc == "T":
            rev_comp_seq.append("A")
        elif nuc == "G":
            rev_comp_seq.append("C")
        elif nuc == "C":
            rev_comp_seq.append("G")
    return "".join(rev_comp_seq)


def main():
    print(reverse_complement("AAAACCCGGT"))


main()
