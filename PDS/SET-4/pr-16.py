with open("C:/Users/Devanshu/Desktop/Python/PDS Manual/SET-4/demo.txt", "r") as file :
    lines = file.readlines()

    num_lines = len(lines)
    print("Number of lines:", num_lines)

    text = "".join(lines)

    statements = text.split(".")
 
    statements = [statement.strip() for statement in statements if statement.strip()]

    num_statements = len(statements)
    print("Number of statements:", num_statements)

    words = text.split()

    unique_words = set(words)
    num_unique_words = len(unique_words)
    print("Number of unique words:", num_unique_words)

    word_occurrences = {}
    for word in words:
        word_occurrences[word] = word_occurrences.get(word, 0) + 1

    print("\nWord occurrences in Dictionary:")
    for word, occurrence in word_occurrences.items():
        print(f"{word}: {occurrence}")