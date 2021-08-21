import weather
import gui_builder as build
import tkinter as tk

def _weather_by_station_id(entry):
    station = entry.get()
    data_dict = weather.get_gov_weather_by_station(station)
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
# MAIN #
app = build.init_app("WEATHER GUI")
tab_control =  build.create_tab_control(app) 
tab1 = build.create_tab(tab_control, "Tab 1")
tab2 = build.create_tab(tab_control, "Tab 2")
tab3 = build.create_tab(tab_control, "Tab 3")

################################################################################################################################
# TAB 1, FRAME 1 # 
weather_station_frame = build.create_frame(tab1, 0, 0, 'Latest Observation For')

station_entries = ['CYYZ', 'CYWH', 'CYYC']
id_combo = build.create_label_and_combo(weather_station_frame, station_entries, 0, 0, 'Location')
weather_button = build.create_label_and_button(weather_station_frame, lambda: _weather_by_station_id(id_combo), 0, 2, 'Get Weather')

current_station = build.create_label(weather_station_frame, 1, 0, 3)

################################################################################################################################
# TAB1, FRAME 2 #
entry_width = 20
weather_conditions_frame = build.create_frame(tab1, 1, 0, 'Current Weather Conditions')
updated = build.create_label_and_entry(weather_conditions_frame, 0, 0, entry_width, 'Last Updated')
weath = build.create_label_and_entry(weather_conditions_frame, 1, 0, entry_width, 'Weather')
temp = build.create_label_and_entry(weather_conditions_frame, 2, 0, entry_width, 'Temperature')
dewp = build.create_label_and_entry(weather_conditions_frame, 3, 0, entry_width, 'Dew Point')
humid = build.create_label_and_entry(weather_conditions_frame, 4, 0, entry_width, 'Humidity')
wind = build.create_label_and_entry(weather_conditions_frame, 5, 0, entry_width, 'Wind')
visib = build.create_label_and_entry(weather_conditions_frame, 6, 0, entry_width, 'Visibility')
press = build.create_label_and_entry(weather_conditions_frame, 7, 0, entry_width, 'Pressure')
alti = build.create_label_and_entry(weather_conditions_frame, 8, 0, entry_width, 'Altimeter')

################################################################################################################################
# TAB 2, FRAME 1 #
weather_states_frame = build.create_frame(tab2, 0, 0, 'Weather Station IDs')

state_combo_entries = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
                 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
                 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
                 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
                ]
state_combo = build.create_label_and_combo(weather_states_frame, state_combo_entries, 0, 0, 'Select a State')
build.create_label_and_button(weather_states_frame, lambda: _station_ids_by_state(state_combo), 0, 2, 'Get Stations')

current_state = build.create_label(weather_states_frame, 1, 0, 3)

cities_stations_scroll = build.create_scroll_box(weather_states_frame, 2, 0, 3)

################################################################################################################################
# TAB 3, FRAME 1 # 
weather_images_frame = build.create_frame(tab3, 0, 0, 'Weather Images')

icon_data = weather.get_open_weather_image('01d')
photo = tk.PhotoImage(data=icon_data)
tk.Label(weather_images_frame, image=photo).grid(row=0, column=1, sticky='W')

################################################################################################################################
app.mainloop()