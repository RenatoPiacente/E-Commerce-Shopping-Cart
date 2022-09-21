cart = []

cart.append(('Shirt', 30.50))
cart.append(('Jeans', 40.99))
cart.append(('Sneakers', 98.95))

total = sum([price for product, price in cart])

if __name__ == '__main__':
    print(f'Total of your purchase: ${total:.2f}')
