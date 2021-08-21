import os 
import glob
import collections
from typing import List

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')

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

def get_folder():
    """
        brief: gets the full system path for the root folder to begin the search. 
        return: the full system path provided by the user 
    """
    folder = ''
    while not os.path.isdir(folder): 
        folder = input(f'Folder to begin search: {bc.WARNING}')
        folder = folder.strip()
        print(f'{bc.ENDC}')
    return os.path.abspath(folder) 

def get_keyword():
    """
        brief: gets the keyword to look for during the search. 
        return: the keyword provided by the user 
    """

    keyword = ''
    while keyword == '': 
        keyword = input(f'Keyword to search for: {bc.WARNING}')
        keyword = keyword.strip()
    
    print(f'{bc.ENDC}')
    return keyword

def search_folder_by_keyword(folder:str, keyword:str):
    """
        brief: recursively searches folders and files for the given keyword. 
        return: SearchResult tuple object, note utilizes a generator method to yield a search result one at a time. 

        param: folder   - the root folder 
        param: keyword  - the word to search for
    """
    items = glob.glob(os.path.join(folder, '*'))
    for item in items:
        if os.path.isdir(item):
            yield from search_folder_by_keyword(item, keyword) 
        else:
            yield from search_file_by_keyword(item, keyword)

def search_file_by_keyword(file:str, keyword:str):
    """
        brief: reads file line by line searching for the keyword, if there is a match
                stores filename, line number, and the associated text into SearchResult object. 
        return: SearchResult(file, line, text) named tuple. 

        param: file     - the file to search
        param: keyword  - the keyword to search for 
    """
    line_number = 0
    with open(file, 'r', encoding='unicode_escape', errors='ignore') as fin:
        for line in fin:
            line_number += 1
            if line.lower().find(keyword) >= 0:
                yield SearchResult(file=file, line=line_number, text=line)

def print_results(results: List[SearchResult]):
    """
        brief: prints output of a list of SearchResult named tuples
        return: None

        param: results - a list of SearchResult named tuples
    """
    for result in results:
        print(f'{bc.OKGREEN}---- MATCH ----{bc.ENDC}')
        print(f'Line: {result.line}')
        print(f'File: {result.file}')
        print(f'Text: {result.text.strip()}')
        print()

def main():
    print_title("FILE SEARCHER")
    folder = get_folder()
    keyword = get_keyword()
    search_results = search_folder_by_keyword(folder, keyword)
    print_results(search_results)

if __name__ == '__main__':
    main() 