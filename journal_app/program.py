import journal

name = None 

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

def print_goodbye(goodbye:str):
    print()
    print()
    print(f'\t\t{goodbye}')
    print('--------------------------------------------------')

def log_in():
    global name
    while name != 'sean':
        name = input('Welcome to Journal. What is your name? ')
        name = name.lower().strip()
    print(f'Welcome, {bc.OKGREEN}{name}{bc.ENDC}')

def run_event_loop():

    global name
    print(f'What would you like to do today, {name}?')

    data = journal.load(name)
    
    cmd = None 
    while cmd != 'c':
        journal.display_journal(name, data)
        cmd = input('[R]ead Entry, [A]dd Entry, [D]elete Entry, [E]dit Entry, [C]lose Journal: ')
        cmd = cmd.lower().strip()

        if cmd == 'r':
            do_read(data)
        elif cmd == 'a':
            do_add(data)
        elif cmd == 'd':
            do_delete(data)
        elif cmd =='e':
            do_edit(data)
        elif cmd != 'c':
            print(f'Not sure what you mean by {cmd}!')

    print_goodbye("have a good one")
    journal.save(name, data)

def do_read(data):
    index = -1
    while index < 0 or index >= len(data):
        journal.display_journal(name, data)
        index = input('Enter Index or go [b]ack to Journal: ')
        index = index.lower().rstrip()
        if not index.isdigit():
            return
        else:
            index = int(index)

    journal.read_entry(data, index)
    input('done reading? ')

def do_add(data):
    entry = input('How are you today? ')
    journal.add_entry(data, entry)

def do_delete(data):
    index = -1
    while index < 0 or index > len(data):
        index = input('What entry do you want to remove? ')
        index = int(index.lower().rstrip())
    journal.remove_entry(data, index)

def do_edit(data):
    index = -1
    while index < 0 or index >= len(data):
        journal.display_journal(name, data)
        index = input('Which entry would you like to edit? ')
        index = index.lower().rstrip()
        if not index.isdigit():
            return
        else:
            index = int(index)

    journal.edit_entry(data, index)

def main():

    print_title("Journal App")
    log_in()
    run_event_loop()

if __name__ == '__main__':
    main()
    