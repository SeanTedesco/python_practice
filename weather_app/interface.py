import weather
import tkinter as tk
from tkinter import Label, Menu
from tkinter import ttk


#######################################################################################
# GLOBALS
#
app = tk.Tk()
tab_control = ttk.Notebook(app)


def init_app(name):
    global app
    app.title(f'{name}')
    app.minsize(width=512, height=256) 

def _quit_app():
    global app
    app.quit()
    app.destroy()
    exit()

def generate_menubar():
    
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

def generate_weather_conditions_window():
    global tab_control

    """build the tab"""
    tab1 = ttk.Frame(tab_control)           # create
    tab_control.add(tab1, text='Tab 1')     # add
    tab_control.pack(expand=1, fill='both') # display


    """build first parent frame for combo widgets"""
    weather_cities_frame = ttk.LabelFrame(tab1, text='Latest Observation For: ')
    weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

    ### LOCATION ###
    ttk.Label(weather_cities_frame, text='Location: ').grid(column=0, row=0, padx=8, pady=4, sticky='W')

    city = tk.StringVar()
    citySelected = ttk.Combobox(weather_cities_frame, width=12, textvariable=city)
    citySelected['values'] = ('Los Angeles', 'New York', 'Rio de Janeiro, Brazil')
    citySelected.grid(column=1, row=0, padx=8, pady=4, sticky='W')
    citySelected.current(0)
    max_width = max([len(x) for x in citySelected['values']])
    citySelected.config(width=max_width-4)
    entry_width = max_width-4


    """build second parent frame for entry widgets"""
    weather_conditions_frame = ttk.LabelFrame(tab1, text='Current Weather Conditions')
    weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)
    roww = 0

    ### LAST UPDATE ###
    ttk.Label(weather_conditions_frame, text='Last Updated: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    updated = tk.StringVar()
    updatedEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=updated, state='readonly')
    updatedEntry.grid(column=1, row=roww, sticky='W')
    roww += 1
    
    ### WEATHER ###
    ttk.Label(weather_conditions_frame, text='Weather: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    weather = tk.StringVar()
    weatherEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=weather, state='readonly')
    weatherEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### TEMPERATURE ###
    ttk.Label(weather_conditions_frame, text='Temperature: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    temp = tk.StringVar()
    tempEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=temp, state='readonly')
    tempEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### DEWPOINT ###
    ttk.Label(weather_conditions_frame, text='Dewpoint: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    dew = tk.StringVar()
    dewEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=dew, state='readonly')
    dewEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### HUMIDITY ###
    ttk.Label(weather_conditions_frame, text='Humidity: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    humid = tk.StringVar()
    humidEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=humid, state='readonly')
    humidEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### WIND ###
    ttk.Label(weather_conditions_frame, text='Wind: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    wind = tk.StringVar()
    windEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=wind, state='readonly')
    windEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### Visibility ###
    ttk.Label(weather_conditions_frame, text='Visibility: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    visibility = tk.StringVar()
    visibilityEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=visibility, state='readonly')
    visibilityEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### Pressure ###
    ttk.Label(weather_conditions_frame, text='Pressure: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    pressure = tk.StringVar()
    pressureEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=pressure, state='readonly')
    pressureEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

    ### Altimeter ###
    ttk.Label(weather_conditions_frame, text='Altimeter: ').grid(column=0, row=roww, padx=8, pady=4, sticky='W')
    altimeter = tk.StringVar()
    altimeterEntry = ttk.Entry(weather_conditions_frame, width=entry_width, textvariable=altimeter, state='readonly')
    altimeterEntry.grid(column=1, row=roww, sticky='W')
    roww += 1

def generate_second_window():
    global tab_control
    
    tab2 = ttk.Frame(tab_control)           # create
    tab_control.add(tab2, text='Tab 2')     # add
    tab_control.pack(expand=1, fill='both') # display
    
def populate_gui_from_dic(dict):
    pass


def main():

    init_app("WEATHER APP")
    generate_menubar()
    generate_weather_conditions_window()
    generate_second_window()

    data_dict = weather.call_weather_api()
    print(data_dict)
    populate_gui_from_dic(data_dict)

    app.mainloop()
    

if __name__ =='__main__':
    main()