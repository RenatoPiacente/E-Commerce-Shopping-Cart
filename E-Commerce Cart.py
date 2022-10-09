def shopping_cart():
    """Gets each product that was added to the cart, by appending the name and price to an empty list.
    Sums the prices of all products that were added to the cart.
    Returns the total price.
    """
    cart = []

    cart.append(('Shirt', 31.50))
    cart.append(('Jeans', 40.99))
    cart.append(('Sneakers', 97.95))

    total = sum([price for product, price in cart])
    return total

if __name__ == '__main__':
    print(f'Total of your purchase: ${shopping_cart():.2f}')
