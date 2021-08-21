"""
street,city,zip,state,beds,baths,sqft,type,sale_date,price,latitude,longitude
"""
import os 
import csv
from typing import List
from data_types import Purchase
import statistics

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_title(title:str):
    print()
    print('--------------------------------------------------')
    print(f'{bc.HEADER}\t\t{title}{bc.ENDC}')
    print('--------------------------------------------------')
    print()

def print_exit():
    print()
    print(f'{bc.HEADER}--------------------------------------------------{bc.ENDC}')
    
def get_filename(file):
    """
    brief:  gets the full system filename of the file found in the local data/ directory
    return: the full system path

    param: file     - the name of the file 
    """
    parent_folder = os.path.dirname(__file__)
    return os.path.join(parent_folder, '..', 'data', file)

def load_file(filename:str):
    """
    brief: reads in a csv file provided by p/ filename using a csv.DictReader 
    return: a list of Purchase class objects 

    param: filename - the full system path of a csv file 
    """
    purchases = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            purchase = Purchase.create_from_dict(row)
            purchases.append(purchase)
        
        return purchases

def querry_data(data: List[Purchase]):
    """
        brief: outputs user readable data and statistics 
        return: None

        param: data - a list of purchases that will be used to generated the stats 
    """

    # sort calls key function on each of the elements in data 
    data.sort(key=lambda p: p.price)

    low_purchase = data[0] 
    print(f'Lowest cost house is a {low_purchase.beds} bed, {low_purchase.baths} bath at {low_purchase.street} with a cost of ${low_purchase.price}.')
    
    high_purchase = data[-1]
    print(f'Highest cost house is a {high_purchase.beds} bed, {high_purchase.baths} bath at {high_purchase.street} with a cost of ${high_purchase.price}.')
    

    # list comprehension: (projection / items) (the set to process) (possible condition)
    two_beds = [home for home in data if home.beds == 2]
    two_beds_prices = statistics.mean([p.price for p in two_beds])
    two_beds_baths = statistics.mean([p.baths for p in two_beds])
    two_beds_sqft = statistics.mean([p.sqft for p in two_beds]) 

    print(f'The average two-bed home costs ${round(two_beds_prices, 1)}, with {round(two_beds_baths, 1)}, and {round(two_beds_sqft, 1)} square ft.')

def main():
    print_title('Real Estate Data Miner')

    filename = get_filename('sacromento_real_estate_transactions.csv')
    data = load_file(filename)
    querry_data(data)
    
    print_exit()


if __name__ == '__main__':
    main() 