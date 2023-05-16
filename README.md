# Python Menu Ordering System

This is a Python Menu Ordering System using functions, loops and data structures, f strings, padding strings using formatting specifier (:).

## Table of contents

- [Overview](#overview)
  - [How to use the project](#how-to-use-the-project)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

### How to use the project

#### Step 1: Setting up Initial Requirements:

1. Python 3.11 and above — Follow [this link](https://www.python.org/downloads/) to download Python for your operating system. You can refer to these tutorials on YouTube for the same — Windows, Mac-OS, Ubuntu (it’ll be somewhat similar for other Linux distributions).

2. pip — pip has been included with the Python installer since versions 3.4 for Python 3 and 2.7.

3. Install pipenv using pip — pip install pipenv

#### Step 2: Setting up Python Virtual Environment using pipenv:

1. Install required dependencies using pipenv — pipenv install
2. Activate Python Virtual Environment — pipenv shell
3. Run the program — python main.py

### Screenshot
![image](https://user-images.githubusercontent.com/108392678/236617726-86500877-1f0d-4462-a209-d6c7952bb9eb.png)




### Links

- Github: [Code](https://github.com/marventures/python-menu-ordering-system)

## My process

### Built with

- [Python](https://www.python.org/) - python.org
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Python Virtual Environment.

### What I learned

- Python Functions
- Python Loops
- Python List Comprehensions
- Python Data Structures
- Python f strings
- Padding strings using formatting specifier (:)

Here is a code snippet:

```py
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


# PRINT ORDER
def print_order(order):
    print('\n')
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item['name'] for item in order]
    print(items)
    return order

```

### Useful resources

- [W3Schools Python Tutorial](https://www.w3schools.com/python/) - This helped me use python functions, loops and data structures, f strings, padding strings using formatting specifier (:)
- [Pipenv Setup](https://python.plainenglish.io/setting-up-a-basic-django-project-with-pipenv-7c58fa2ec631) - This helped me setup my python virtual env

## Author

- Website - [Marvin Morales Pacis](https://marvin-morales-pacis.vercel.app/)
- LinkedIn - [@marventures](https://www.linkedin.com/in/marventures/)
- Twitter - [@marventures11](https://www.twitter.com/marventures11)
