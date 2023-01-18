"""

Frequent Words Problem: Find the most frequent k-mers in a string.

Input: A string Text and an integer k.
Output: All most frequent k-mers in Text.

FrequencyTable(Text, k)
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n − k
        Pattern ← Text(i, k)
        if freqMap[Pattern] doesn't exist
            freqMap[Pattern]← 1
        else
            freqMap[pattern] ←freqMap[pattern]+1 
    return freqMap

"""

import pattern_count


def get_kmer_counts(seq: str, k: int) -> dict[str, int]:
    """Look for kmers within a given sequence (text).

    Args:
        seq (str): sequence within which the kmers are searched
        k (int): kmer length

    Returns:
        dict[str, int]: kmer: kmer count in the sequence

    Usage examples:
    >>> get_kmer_counts("AAATTT", 1)
    {'A': 3, 'T': 3}
    """

    counts: dict[str, int] = {}

    for i in range(len(seq) - k + 1):
        subseq: str = seq[i : i + k]
        if subseq not in counts:
            counts[subseq] = pattern_count.count_pattern(seq, subseq)
    return counts


if __name__ == "__main__":

    freqs: dict[str, int] = get_kmer_counts(text, k)
    max_freq: int = max(freqs.values())

    most_freqs: list[str] = [key for key, value in freqs.items() if value == max_freq]
    print(" ".join(most_freqs))
