#import exceptions

class MenuItem:

    def __init__(self, name, cost, price):
        self._name = name
        self._cost = cost
        self._price = price

    def get_menu_name(self):
        return self._name

    def get_menu_cost(self):
        return self._cost

    def get_menu_price(self):
        return self._price

class SalesForDay:

    def __init__(self, which_day, sales_dict):
        self._which_day = which_day
        self._sales = sales_dict

    def get_which_day(self):
        return self._which_day

    def get_sales(self):
        return self._sales

class LemonadeStand:

    def __init__(self, name):
        self._stand_name = name
        self._current_day = 0
        self._menu_dict = {}
        self._list_of_sales = []

    def get_stand_name(self):
        return self._stand_name

    def get_current_day(self):
        return self._current_day

    def get_menu_dict(self):
        return self._menu_dict

    def get_list_of_sales(self):
        return self._list_of_sales

    def add_menu_item(self, item_obj):
        if item_obj in self.get_menu_dict():
            return "already on the menu"
        self._menu_dict[item_obj.get_menu_name()] = item_obj

    def enter_sales_for_today(self, itemsSold_dict):
        for key in itemsSold_dict.keys():
            if key not in self.get_menu_dict():
                raise InvalidSalesItemError
        todays_sales = SalesForDay(self.get_current_day(), itemsSold_dict)
        self._list_of_sales.append(todays_sales)
        self._current_day += 1

        #2 if statements: If an item in the menu doesn't
        #appear in the dictionary, then there were no sales 
        #of that item on that day. 

        #If the name of any item sold doesn't match the name of any MenuItem in the 
        #dictionary of MenuItem objects, this method should 
        #do nothing except raise an **InvalidSalesItemError**
        #(you'll need to define this exception class).

    def sales_of_menu_item_for_day(self, which_day):
        return self.get_list_of_sales()[which_day]

    def total_sales_for_menu_item(self, item_name):
        count = 0
        for sale_obj in self.get_list_of_sales():
            if item_name in sale_obj.get_sales():
                count+= sale_obj.get_sales()[item_name]
        return count
        
    def total_profit_for_menu_item(self, item_name):
        cost = self.get_menu_dict()[item_name].get_menu_cost()
        price = self.get_menu_dict()[item_name].get_menu_price()
        profit = price - cost
        total = profit * self.total_sales_for_menu_item(item_name)
        return total

    def total_profit_for_stand(self):
        profit = 0
        for key in self.get_menu_dict().keys():
            profit += self._total_profit_for_menu_item(key)
        return profit

stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand called 'Lemons R Us'
item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
item3 = MenuItem('cookie', 0.2, 1) # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

day_0_sales = {
    'lemonade' : 5,
    'cookie'   : 2
}

stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")  # print the total profit for lemonade so far
