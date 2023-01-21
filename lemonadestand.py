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
        if item_obj in get_menu_dict():
            return "already on the menu"
        self._menu_dict[item_obj.get_menu_name()] = item_obj

    def enter_sales_for_today(self, itemsSold_dict):
        todays_sales = SalesForDay(self.get_current_day(), itemsSold_dict)
        self._list_of_sales.append(todays_sales)
        self._current_day += 1
        #2 if statements: If an item in the menu doesn't
        #appear in the dictionary, then there were no sales 
        #of that item on that day. If the name of any item 
        #sold doesn't match the name of any MenuItem in the 
        #dictionary of MenuItem objects, this method should 
        #do nothing except raise an **InvalidSalesItemError**
        #(you'll need to define this exception class).

    def sales_of_menu_item_for_day(self, which_day):
        sales = self._list_of_sales[which_day]