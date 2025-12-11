fb = ["Ростислав", "Максим", "Ярослав", "Настя", "Даша"]
tg = ["Марат", "Даша", "Ліза", "Олег"]
tw = ["Настя", "Тоня", "Ростислав"]

def merge_guest_lists_compact(*lists):
    all_lists = []
    for lst in lists:
        all_lists.extend(lst)

    return sorted(list(set(all_lists)))

final_clean_list = merge_guest_lists_compact(fb, tg, tw)

print(f"Список гостей: {final_clean_list}")