text = input("Enter your text: ")

def countVowels(str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for st in str:
        if st in vowels:
            count += 1
    
    return count

print("Total Vowel in your text is: ", countVowels(text))