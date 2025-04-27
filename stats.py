def get_num_words(book_content: str) -> int:
    return len(book_content.split())

def count_chars(book_content: str) -> dict[str, int]:
    
    d_count: dict[str, int] = {}

    for c in book_content.lower():
        d_count[c] = d_count.setdefault(c, 0) + 1

    return d_count


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[dict[str, int]]:
    sorted_list = []
    
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list