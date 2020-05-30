print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
library = {}
while True:
    user = input()
    if(user == "exit"):
        break
    try:
        library[user] += 1
    except:
        library[user] = 1
    if library[user] == 1:
        print(f"** {library[user]} order of {user} has been added to your meal **")
    elif library[user] > 1:
        print(f"** {library[user]} orders of {user} have been added to your meal **")

    print("")
