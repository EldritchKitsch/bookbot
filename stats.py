def get_word_count(text: str):
    words = text.split()
    return len(words)

def get_char_dict(text: str):
    char_dict: dict[str, int] = {}

    for c in text:
        char = c.lower()
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def transform_char_dict(char_dict: dict[str, int]):
    char_list: list[dict[str, int | str]] = []

    for char in char_dict:
        char_list.append({
            "char": char, 
            "num": char_dict[char],
        })
    
    def get_num(dict_char):
        return dict_char["num"]
    
    char_list.sort(reverse=True, key=get_num)

    return char_list