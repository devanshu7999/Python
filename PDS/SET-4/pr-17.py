character_frequency = {}

with open("C:/Users/Devanshu/Desktop/Python/PDS Manual/SET-4/Bigfile.txt", "r") as file:

    for line in file:
        for char in line:
           
            if char.isalnum() and not char.isspace():
              
                character_frequency[char] = character_frequency.get(char, 0) + 1

print("Frequency/count of each unique character:")
for char, count in character_frequency.items():
    print(f"{char}: {count}")
