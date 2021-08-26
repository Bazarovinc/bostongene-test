from typing import List


def convert_to_lowercase_naming(names: List[str]) -> List[str]:
    for i in range(len(names)):
        names[i] = names[i].lower()
    return names
