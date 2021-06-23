import os
import image_service

def print_beginning(title:str=""):
    print("-----------------------------------------")
    print(f'\t\t {title}')
    print("-----------------------------------------")
    print()

def print_ending(ending:str=""):
    print()
    print()
    print(f'\t\t {ending}')
    print("-----------------------------------------")

def set_output_dir(dir:str='changeme'):
    base_directory = os.path.dirname(__file__)
    full_path = os.path.join(base_directory, dir)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new directory... ' + full_path)
        os.mkdir(full_path)
    else:
        print(dir + ' directory already exists')
    
    return full_path

def download_images(dir, count):
    for i in range(1, count+1):
        file_name = f'image_{i}'
        image_service.get_image(dir, file_name)


def main():
    print_beginning("LOL CAT")

    directory = set_output_dir('cat-pictures')
    download_images(directory, 3)

    print_ending("GOOD BYE")
    
if __name__ =='__main__':
    main()