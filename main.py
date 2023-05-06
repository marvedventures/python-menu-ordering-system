###########################################################################################################################################
# MENU ORDERING SYSTEM: Functions, loops and data structures, f strings, padding strings using formatting specifier (:)
###########################################################################################################################################

#  Menu ordering system which will allow users to input three choices for a select menu

menu = {
    1: {'name': 'espresso',
        'price': 1.99},
    2: {'name': 'coffee',
        'price': 2.50},
    3: {'name': 'cake',
        'price': 2.79},
    4: {'name': 'soup',
        'price': 4.50},
    5: {'name': 'sandwich',
        'price': 4.99}
}


# SUBTOTAL
def calculate_subtotal(order):

    print('Calculating bill subtotal...')

    sub_total = 0
    for item in order:
        sub_total += item['price']
    return round(sub_total, 2)


# TAX
def calculate_tax(subtotal):

    print('Calculating tax from subtotal...')

    return round(subtotal * 15 / 100.00, 2)


# SUMMARIZE ORDER
def summarize_order(order):

    print_order(order)

    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item['name'] for item in order]
    return names, total


# PRINT ORDER
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item['name'] for item in order]
    print(items)
    return order


# DISPLAY MENU
def display_menu():
    print('------- Menu -------')
    for selection in menu:
        # pads the output string of menu[selection]['name'] to a width of 9 characters, aligning it to the left of that space.
        # pads the output string of menu[selection]['price'] to a width of 5 characters, aligning it to the right of that space.
        print(
            f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


# TAKE ORDER
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input(f'Select menu item number {count} (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


# INVOKE FUNCTIONS
def main():

    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print(f'Subtotal for the order is: {subtotal}')

    tax = calculate_tax(subtotal)
    print(f'Tax for the order is: {tax}')


if __name__ == '__main__':
    main()
