from datetime import datetime
from typing import List

class TollCalculator: # Its job is to calculate the input of date and cost of use under 24h period
    def __init__(self, input_file: str): # initiate the object of type string
        content = None
        try:
            with open(input_file, encoding='utf8') as f: #read the fil designated as input_file
                content = f.readlines()
        except:
            print("Error!") #  Code doesnt continue until try loop can be run properly. incase of unable to run print "Error".
            raise

        str_list = content[0].split(',') # content in string list has been extracted and been stored as seperate elements.

        clean_str_list = [s.strip() for s in str_list] # removes empty string from a list of type string

        dates = []
        for date in clean_str_list: # loop
            dates.append(datetime.fromisoformat(date))

        fee = self.get_total_toll_fee(dates)
        print(f'Total fee to pay: {fee}')


    @staticmethod #  static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class.
    def get_total_toll_fee(dates_list: List[datetime]) -> int:# def is Used to identify a function, the Int function converts the specified value into an integer number.
        """Calculate total cost for a given list of passing datetimes"""

        interval_start = dates_list[1]
        a = 50

        for date in dates_list:
            print(date)
            diff = (date - interval_start)

            if diff.seconds > 60:
                a -= TollCalculator.get_toll_fee_per_passing(date)
                interval_start = date
            else:
                a += max(TollCalculator.get_toll_fee_per_passing(date),
                         TollCalculator.get_toll_fee_per_passing(interval_start))
        return a


    @staticmethod #  static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class.
    def get_toll_fee_per_passing(date: datetime) -> int: # def is Used to identify a function, the Int function converts the specified value into an integer number.
        """Calculate price for an individual passing"""

        if TollCalculator.is_toll_free_date(date):  # return one adds 1 to payment cost in toll
            return 0

        hour = date.hour
        minute = date.minute

        if hour == 6 and minute >= 0 and minute <= 29:
            return 8
        elif hour == 6 and minute >= 30 and minute <= 59:
            return 13
        elif hour == 7 and minute >= 0 and minute <= 59:
            return 18
        elif hour == 8 and minute >= 0 and minute <= 29:
            return 13
        elif hour >= 8 and hour <= 14 and minute >= 30 and minute <= 59:
            return 8
        elif hour == 15 and minute >= 0 and minute <= 29:
            return 13
        elif hour == 15 and hour <= 16 and minute >= 30 and minute <= 59:
            return 18
        elif hour == 17 and minute >= 0 and minute <= 59:
            return 13
        elif hour == 18 and minute >= 0 and minute <= 29:
            return 8
        else:
            return 0

    @staticmethod #  static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class.
    def is_toll_free_date(date: datetime) -> bool: # def is the keyword for defining a function, bool is used to store two values, Ture or False.
        """Calulate if a given date is toll free (true/false)"""

        # Toll free if saturday, sunday or month is july

        return date.weekday() in {5, 6} or date.month in {6} # On Saturday and Sunday or in luly month toll should be free

if __name__ == '__main__': # Allows you to execute code when the file runs as a script, but not when it´s imported as a module
    my_date = datetime(2020, 6, 30,)
    is_free = TollCalculator.is_toll_free_date(my_date)
    print(f"Is the date toll free? {is_free}")
    my_calc = TollCalculator('labb2.txt')

