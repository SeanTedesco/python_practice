import os 
from datetime import date

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

def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.txt'))
    return filename

def load(name):
    data = []
    filename = get_full_path(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def save(name, data):
    filename = get_full_path(name)
    print(f'... saving to {filename}')
    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\r\n')

def add_entry(data, entry):
    today = date.today()
    today = today.strftime("%Y/%m/%d")
    data.append(today + '$' + entry)

def read_entry(data, index):
    print('--------------------------------------------------')
    print(f'|\t\t {bc.OKCYAN}entry {index}{bc.ENDC}\t\t\t |')
    print('--------------------------------------------------')
    entry = data[index]
    entry= entry.split('$')[1]
    print(entry)
    print('--------------------------------------------------')
    print()
    print()

def remove_entry(data, index):
    data.pop(index)

def edit_entry(data, index):
    entry = data[index]
    entry = entry.split('$')[1]
    print(f'Entry to be edited: {entry}')
    print()
    print('write new entry...')
    new_entry = input()
    remove_entry(data, index)
    add_entry(data, new_entry)

def print_indexes(data):
    for index, entry in enumerate(data):
        if entry != '\n':
            print(f'| Entry [{index}] \t\t\t\t\t |')

def print_dates(data):
    for index, entry in enumerate(data):
        d1 = entry.split('$')[0]
        print(f'| [{bc.FAIL}{index}{bc.ENDC}] {d1} \t\t\t\t |')

def display_journal(name, data):
    print('--------------------------------------------------')
    print(f'|\t\t {bc.OKCYAN}{name}\'s journal{bc.ENDC}\t\t\t |')
    print('--------------------------------------------------')
    print_dates(data)
    print('--------------------------------------------------')