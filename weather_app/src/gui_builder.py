import tkinter as tk
from tkinter import Label, Menu
from tkinter import ttk
from tkinter import scrolledtext
import PIL.Image as pii
import PIL.ImageTk as pit

def init_app(name):
    """
        breif: Adds a title, sets window sizes, and creates menubar for a root application. 
        return: the instance of the application. 
    """
    root = tk.Tk()
    root.title(f'{name}')
    root.minsize(width=512, height=256) 
    generate_menubar(root)
    return root

def quit_app(root):
    """
        breif: call back for quiting the application 
        return: None
    """
    root.quit()
    root.destroy()
    exit()

def generate_menubar(root):
    """
        breif: creates a menu bar for general saving, opening, closing functions 
        return: None 

        param: root - the main application that is running 
    """
    menu_bar = Menu()
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New')
    file_menu.add_separator()
    file_menu.add_command(label='Open')
    file_menu.add_separator()
    file_menu.add_command(label='Save')
    menu_bar.add_cascade(label='File', menu=file_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='About')
    menu_bar.add_cascade(label='Help', menu=help_menu)

    quit_menu = Menu(menu_bar, tearoff=0)
    quit_menu.add_command(label='Close', command=lambda:quit_app(root))
    menu_bar.add_cascade(label='Exit', menu=quit_menu) 

def create_tab_control(root):
    """
        brief: create a tab controller to house multiple tabs in the GUI
        return: the tkinter notebook tab control 

        param: root - the main application that is running 
    """
    return ttk.Notebook(root)

def create_tab(tab_control, name:str='Tab'):
    """
        breif: adds a tab to the app interface
        return: tab         - the generated tk tab

        param: tab_control  - the controller for all tabs
        param: name         - the name given to the tab
    """
    tab = ttk.Frame(tab_control)           # create
    tab_control.add(tab, text=f'{name}')     # add
    tab_control.pack(expand=1, fill='both') # display
    return tab

def create_frame(tab, r:int=0, c:int=0, name:str='Window'):
    """
        breif: adds a frame to a tab
        return: frame   - the generated frame

        param: tab      - the tab to which to add the frame
        param: r        - the row of the tab
        param: c        - the column of the tab
        param: name     - the name given to the frame
    """
    frame = ttk.LabelFrame(tab, text=f'{name}: ')
    frame.grid(row=r, column=c, padx=8, pady=4, sticky='W')
    return frame

def create_scroll_box(frame, r:int=0, c:int=0, s:int=3, w:int=32, h:int=24):
    """
        breif: generates a text box with a scollbar
        return: frame   - the generated scroll box

        param: frame    - the frame to which to add the scroll box
        param: r        - the row of the tab
        param: c        - the column of the tab
        param: s        - the column span of the scroll box
        param: w        - the width in ASCII units? of the scroll box
        param: h        - the height in ASCII units? of the scroll box
    """
    scr = scrolledtext.ScrolledText(frame, width=w, height=h, wrap=tk.WORD)
    scr.grid(row=r, column=c, columnspan=s, sticky='W')
    return scr

def create_label(frame, r:int=0, c:int=0, s:int=0):
    """
        breif: generates a label that can exist within a tk frame 
        return: frame   - the generated label

        param: frame    - the frame to which to add the scroll box
        param: r        - the row of the tab
        param: c        - the column of the tab
        param: s        - the column span of the scroll box
    """
    temp_label = tk.StringVar()
    ttk.Label(frame, textvariable=temp_label).grid(row=r, column=c, columnspan=s, sticky='W')
    return temp_label

def create_label_and_entry(frame, r:int=0, c:int=0, size:int=16, name:str='Entry'):
    """
        breif: adds a labelled and a read only entry box to a frame
        return: update  - tk string variable used to set/get the entry box

        param: frame    - the frame to which to add the label and entry 
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the label
    """
    ttk.Label(frame, text=f'{name}: ').grid(row=r, column=c, padx=8, pady=4, sticky='W')
    update = tk.StringVar()
    updateEntry = ttk.Entry(frame, width=size, textvariable=update, state='readonly')
    updateEntry.grid(row=r, column=c+1, sticky='W')
    return update

def create_label_and_combo(frame, entries, r:int=0, c:int=0, name:str='Combo'):
    """
        breif:              - adds a labelled dropdown box to a specified frame
        return: combo_str   - the tk string variable. What is highlighted in the combo box can be used to set/get with this return variable. 

        param: frame    - the frame to which to add the dropdown box
        param: entries  - a list of all the entries to apear in the dropdown box
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the label
    """
    ttk.Label(frame, text=f'{name}').grid(row=r, column=c, padx=8, pady=4, sticky='W')

    combo_str = tk.StringVar()
    strSelected = ttk.Combobox(frame, width=16, textvariable=combo_str)
    strSelected['values'] = entries
    strSelected.grid(column=1, row=0, padx=8, pady=4, sticky='W')
    strSelected.current(0)
    max_width = max([len(x) for x in strSelected['values']])
    strSelected.config(width=max_width+1)
    return combo_str

def create_label_and_button(frame, cmd, r:int=0, c:int=0, name:str='Button'):
    """
        breif: generates a labelled button. Label apears on the button.
        return: the button instance. 

        param: frame    - the tk frame that holds the labelled button
        param: cmd      - lamda function that gets called with a button press. Ex: cmd = lambda: get_station_ids(state_combo_box)
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the labelled button
    """
    return ttk.Button(frame, text=f'{name}', command=cmd).grid(row=r, column=c, sticky='W')

def main():

    # create the app
    app = init_app("BASIC GUI")

    # put a tab controller into the app 
    tab_control =  create_tab_control(app) 

    # create the first tab and put it into the controller 
    tab1 = create_tab(tab_control, "Tab 1")

    # create a basic frame and put it into the tab
    weather_one = create_frame(tab1, 0, 0, 'Frame 1')

    # create a button and put it into the frame 
    weather_button = create_label_and_button(weather_one, lambda: print("HELLO"), 0, 1, 'Say Hello')

    # run the app
    app.mainloop()

if __name__ == '__main__':
    main()