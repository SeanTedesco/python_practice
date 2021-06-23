import weather
import tkinter as tk
from tkinter import Label, Menu
from tkinter import ttk


#######################################################################################
# GLOBALS
#
app = tk.Tk()

def init_app(name):
    """
    breif: Adds a title, sets window sizes, and creates menubar for the app. 
    return: None
    """
    global app
    app.title(f'{name}')
    app.minsize(width=512, height=256) 

    generate_menubar()

def _quit_app():
    """
    breif: call back for quiting the application 
    return: None
    """
    global app
    app.quit()
    app.destroy()
    exit()

def generate_menubar():
    """
    breif: creates a menu bar for general saving, opening, closing functions 
    return: None 
    """
    
    global app

    menu_bar = Menu()
    app.config(menu=menu_bar)

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
    quit_menu.add_command(label='Close', command=_quit_app)
    menu_bar.add_cascade(label='Exit', menu=quit_menu)

def create_tab(tab_control, name:str='Tab'):
    """
    breif: adds a tab to the app interface
    param: tab_control  - the controller for all tabs
    param: name         - the name given to the tab
    return: tab         - the generated tab
    """
    tab = ttk.Frame(tab_control)           # create
    tab_control.add(tab, text=f'{name}')     # add
    tab_control.pack(expand=1, fill='both') # display
    return tab

def create_frame(tab, r:int, c:int, name:str='Window'):
    """
    breif: adds a frame to a tab
    param: tab      - the tab to which to add the frame
    param: r        - the row of the tab
    param: c        - the column of the tab
    param: name     - the name given to the label
    return: frame   - the generated frame
    """
    frame = ttk.LabelFrame(tab, text=f'{name}: ')
    frame.grid(row=r, column=c, padx=8, pady=4)
    return frame

def create_label_and_entry(frame, r:int, c:int, size:int, name:str='Label'):
    """
    breif: adds a labelled and a read only entry box to a frame
    param: frame    - the frame to which to add the label and entry 
    param: r        - the row of the frame
    param: c        - the column of the frame
    param: name     - the name given to the label
    return: update  - tk strink variable
    """
    ttk.Label(frame, text=f'{name}: ').grid(row=r, column=c, padx=8, pady=4, sticky='W')
    update = tk.StringVar()
    updateEntry = ttk.Entry(frame, width=size, textvariable=update, state='readonly')
    updateEntry.grid(row=r, column=c+1, sticky='W')
    return update

def create_label_and_combo(frame, r:int=0, c:int=0, name:str='Combo'):
    """
    breif: adds a labelled dropdown box to a specified frame
    param: frame    - the frame to which to add the dropdown box
    param: r        - the row of the frame
    param: c        - the column of the frame
    param: name     - the name given to the label
    return: str     - tk strink variable
    return: width   - length of label and combo box
    """
    ttk.Label(frame, text=f'{name}').grid(row=r, column=c, padx=8, pady=4, sticky='W')

    combo_str = tk.StringVar()
    strSelected = ttk.Combobox(frame, width=16, textvariable=combo_str)
    strSelected['values'] = ('Los Angeles', 'New York', 'Rio de Janeiro, Brazil')
    strSelected.grid(column=1, row=0, padx=8, pady=4, sticky='W')
    strSelected.current(0)
    max_width = max([len(x) for x in strSelected['values']])
    strSelected.config(width=max_width-4)
    width = max_width-4
    return combo_str, width

def main():

    init_app("WEATHER APP")

    tab_control = ttk.Notebook(app)
    tab1 = create_tab(tab_control, "Tab 1")
    tab2 = create_tab(tab_control, "Tab 2")

    # TAB 1, FRAME 1 # 
    weather_cities_frame = create_frame(tab1, 0, 0, 'Latest Observation For')
    city, entry_width = create_label_and_combo(weather_cities_frame, 0, 0, 'Location')
    
    # TAB1, FRAME 2 #
    weather_conditions_frame = create_frame(tab1, 1, 0, 'Current Weather Conditions')
    updated = create_label_and_entry(weather_conditions_frame, 0, 0, entry_width, 'Last Updated')
    weath = create_label_and_entry(weather_conditions_frame, 1, 0, entry_width, 'Weather')
    temp = create_label_and_entry(weather_conditions_frame, 2, 0, entry_width, 'Temperature')
    dewpoint = create_label_and_entry(weather_conditions_frame, 3, 0, entry_width, 'Dew Point')
    humidity = create_label_and_entry(weather_conditions_frame, 4, 0, entry_width, 'Humidity')
    wind = create_label_and_entry(weather_conditions_frame, 5, 0, entry_width, 'Wind')
    visibility = create_label_and_entry(weather_conditions_frame, 6, 0, entry_width, 'Visibility')
    pressure = create_label_and_entry(weather_conditions_frame, 7, 0, entry_width, 'Pressure')
    altimeter = create_label_and_entry(weather_conditions_frame, 8, 0, entry_width, 'Altimeter')

    data_dict = weather.call_weather_api()
    print(data_dict)

    app.mainloop()
    

if __name__ =='__main__':
    main()