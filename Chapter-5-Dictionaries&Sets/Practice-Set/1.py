translations = {
    "biral" : "Cat",
    "kukur" : "Dog",
    "amm" : "Mango",
    "shoitan" : "Devil",
    "foll" : "Fruit"
}
Word = input("Enter the word you want to translate: ").lower()
print("The translation of "+ Word + " is " + translations.get(Word, "Word not found"))