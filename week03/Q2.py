#question 2: shopping cart(list - searching and removal)
cart = ["apple", "banana", "milk", "bread", "apple","eggs"]
print("number of apples", cart.count("apple"))
print("position of milk", cart.index("milk"))
cart.remove("apple")
print("remove item using pop", cart.pop())
print("is banana in the cart?", "banana" in cart)
print("final cart", cart)