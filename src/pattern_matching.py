"""
Code Challenge: Solve the Pattern Matching Problem.

    Input: Two strings, Pattern and Genome.
    Output: A collection of space-separated integers specifying all starting
    positions where Pattern appears as a substring of Genome.
"""


def pattern_matching(genome: str, pattern: str) -> list[int]:

    """Match a pattern (string) to a genome (string) and output  as an integer
    list.

    Returns:
        list[int]: the indeces of the first base (character string) of each
        match

    Usage examples:
    >>> pattern_matching("GATATATGCATATACTT", "ATAT")
    [1, 3, 9]
    """

    indices: list[int] = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i : len(pattern) + i] == pattern:
            indices.append(i)

    return indices


def main() -> None:

    pattern: str = "CTTGATCAT"

    with open("data/Vibrio_cholerae.txt", mode="r") as genome_file:
        genome: str = genome_file.read()

    # print(*list)
    print(*pattern_matching(genome, pattern))


main()
