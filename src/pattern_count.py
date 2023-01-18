"""

PatternCount(Text, Pattern)
  count ← 0
  for i ← 0 to |Text| − |Pattern|
    if Text(i, |Pattern|) = Pattern
      count ← count + 1
  return count

"""


def count_pattern(text: str, pattern: str) -> int:
    count: int = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1
    return count


def main() -> None:

    with open("./src/pattern_count/dataset_2_6.txt", "r") as file:
        # text file with two lines, first as text and last as pattern
        read_content: list[str] = file.read().split("\n")
        text: str = read_content[0]
        pattern: str = read_content[1]

    print("Number of patterns found: ", count_pattern(text, pattern))
