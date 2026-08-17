def remove_fourth_character(word: str) -> str:
    first_remove = word[:3]
    second_remove = word[4:]

    final_word = first_remove + second_remove
    return final_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
