import movie_services

class bc():
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

def movie_search_event_loop():
    search = 'first run'
    while search != 'x':
        search = input(f'Movie search text, [x] to exit: {bc.WARNING}')
        search = search.strip()
        print(f'{bc.ENDC}')

        if search != 'x':
            results = movie_services.find_movies(search)
            plural = 's' if len(results) > 1 else ''
            print(f'{bc.OKGREEN}Found {len(results)} movie{plural}!{bc.ENDC}')

            for movie in results:
                print(f'{movie.year} -- {movie.title}')
                print()
    
    print("exiting...")

def main():
    print_title("MOVIE SEARCHER")
    movie_search_event_loop()
    print_exit()

if __name__ == '__main__':
    main() 