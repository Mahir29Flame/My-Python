def rem(l,word):
    n = []
    for item in l :
        if not (item == word):
            n.append(item.strip(word))
    return n    
l = ["Apple", "Banana", "Pizza", "Laptop", "Chair","Sat", "Coffee", "Book", "Carrot","At" "Milk", "Keyboard","Cat","Rat","Hat"]
remin = input(f"What do u wann remove from here?- {l} : ")
print(str(rem(l,remin)))