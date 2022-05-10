import folium
import pandas as pd 

my_map = folium.Map(location = [30.024, 31.1409], zoom_start = 4)

cities = pd.read_csv('cities.csv')

def selct_marker_color(row):
    if row['power_on'] == 'yes':
        return 'pink'
    else:
        return 'blue'

cities['color'] = cities.apply(selct_marker_color, axis=1)

for _, city in cities.iterrows():
    folium.Marker(
        location=[city['X'], city['Y']], 
        popup=city['name'],
        tooltip= city['name'], 
        icon=folium.Icon(color=city['color'], prefix='fa',icon= 'circle')
    ).add_to(my_map)


my_map.save('map.html')