import weather
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

def create_frame(tab, r:int=0, c:int=0, name:str='Window'):
    """
    breif: adds a frame to a tab
    param: tab      - the tab to which to add the frame
    param: r        - the row of the tab
    param: c        - the column of the tab
    param: name     - the name given to the label
    return: frame   - the generated frame
    """
    frame = ttk.LabelFrame(tab, text=f'{name}: ')
    frame.grid(row=r, column=c, padx=8, pady=4, sticky='W')
    return frame

def create_scroll_box(frame, r:int=0, c:int=0, s:int=3, w:int=32, h:int=24):
    scr = scrolledtext.ScrolledText(frame, width=w, height=h, wrap=tk.WORD)
    scr.grid(row=r, column=c, columnspan=s, sticky='W')
    return scr

def create_label(frame, r:int=0, c:int=0, span:int=0):
    temp_label = tk.StringVar()
    ttk.Label(frame, textvariable=temp_label).grid(row=r, column=c, columnspan=span, sticky='W')
    return temp_label

def create_label_and_entry(frame, r:int=0, c:int=0, size:int=16, name:str='Entry'):
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

def create_label_and_combo(frame, entries, r:int=0, c:int=0, name:str='Combo'):
    """
    breif: adds a labelled dropdown box to a specified frame
    param: frame    - the frame to which to add the dropdown box
    param: entries  - a list of all the entries to apear in the dropdown box
    param: r        - the row of the frame
    param: c        - the column of the frame
    param: name     - the name given to the label
    return: str     - tk strink variable
    return: width   - length of label and combo box
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
    return ttk.Button(frame, text=f'{name}', command=cmd).grid(row=r, column=c, sticky='W')

def _weather_by_station_id(entry):
    station = entry.get()
    data_dict = weather.get_weather_by_station(station)
    if data_dict:
        _populate_entries_from_dict(data_dict)
    else:
        _clear_entries()

def _station_ids_by_state(entry):
    state_id = entry.get()
    current_state.set(state_id)
    stations_list, cities_list = weather.get_stations_by_state(state_id)
    _populate_scroll_box(stations_list, cities_list)

def _populate_entries_from_dict(dict):
    current_station.set(dict['location'])
    updated.set(dict['observation_time'].replace('Last Updated on ', ''))
    weath.set(dict['weather'])
    temp.set('{} \xb0F ({} \xb0C)'.format(dict['temp_f'], dict['temp_c']))
    dewp.set('{} \xb0F ({} \xb0C)'.format(dict['dewpoint_f'], dict['dewpoint_c']))
    humid.set(dict['relative_humidity'] + '%')
    wind.set(dict['wind_string'])
    visib.set(dict['visibility_mi'])
    press.set(dict['pressure_string'])
    alti.set(dict['pressure_in'])

def _clear_entries():
    current_station.set(' ')
    updated.set(' ')
    weath.set(' ')
    temp.set(' ')
    dewp.set(' ')
    humid.set(' ')
    wind.set(' ')
    visib.set(' ')
    press.set(' ')
    alti.set(' ')

def _populate_scroll_box(stations, cities):
    cities_stations_scroll.delete('1.0', tk.END)
    for i in range(len(stations)):
        city_station = cities[i] + ' (' + stations[i] + ')\n'
        cities_stations_scroll.insert(tk.INSERT, city_station)

################################################################################################################################
app = init_app("WEATHER GUI")
tab_control = ttk.Notebook(app)
tab1 = create_tab(tab_control, "Tab 1")
tab2 = create_tab(tab_control, "Tab 2")
tab3 = create_tab(tab_control, "Tab 3")

################################################################################################################################
# TAB 1, FRAME 1 # 
weather_station_frame = create_frame(tab1, 0, 0, 'Latest Observation For')

station_entries = ['CYYZ', 'CYWH', 'CYYC']
id_combo = create_label_and_combo(weather_station_frame, station_entries, 0, 0, 'Location')
weather_button = create_label_and_button(weather_station_frame, lambda: _weather_by_station_id(id_combo), 0, 2, 'Get Weather')

current_station = create_label(weather_station_frame, 1, 0, 3)

################################################################################################################################
# TAB1, FRAME 2 #
entry_width = 20
weather_conditions_frame = create_frame(tab1, 1, 0, 'Current Weather Conditions')
updated = create_label_and_entry(weather_conditions_frame, 0, 0, entry_width, 'Last Updated')
weath = create_label_and_entry(weather_conditions_frame, 1, 0, entry_width, 'Weather')
temp = create_label_and_entry(weather_conditions_frame, 2, 0, entry_width, 'Temperature')
dewp = create_label_and_entry(weather_conditions_frame, 3, 0, entry_width, 'Dew Point')
humid = create_label_and_entry(weather_conditions_frame, 4, 0, entry_width, 'Humidity')
wind = create_label_and_entry(weather_conditions_frame, 5, 0, entry_width, 'Wind')
visib = create_label_and_entry(weather_conditions_frame, 6, 0, entry_width, 'Visibility')
press = create_label_and_entry(weather_conditions_frame, 7, 0, entry_width, 'Pressure')
alti = create_label_and_entry(weather_conditions_frame, 8, 0, entry_width, 'Altimeter')

################################################################################################################################
# TAB 2, FRAME 1 #
weather_states_frame = create_frame(tab2, 0, 0, 'Weather Station IDs')

state_combo_entries = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
                 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
                 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
                 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
                ]
state_combo = create_label_and_combo(weather_states_frame, state_combo_entries, 0, 0, 'Select a State')
create_label_and_button(weather_states_frame, lambda: _station_ids_by_state(state_combo), 0, 2, 'Get Stations')

current_state = create_label(weather_states_frame, 1, 0, 3)

cities_stations_scroll = create_scroll_box(weather_states_frame, 2, 0, 3)

################################################################################################################################
# TAB 3, FRAME 1 # 
weather_images_frame = create_frame(tab3, 0, 0, 'Weather Images')

image = weather.get_open_weather_image()
img = pii.open(image)
im = pit.PhotoImage(img)
ttk.Label(weather_images_frame, image=im).grid(row=0, column=1, sticky='W')


################################################################################################################################
app.mainloop()