import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

latList = list(data["LAT"])
lonList = list(data["LON"])
elevList = list(data["ELEV"])
nameList = list(data["NAME"])


def color_producer(elevation):
    if elevation <= 1000:
        return 'green'
    elif 1000 < elevation <= 2000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Vulcanos")

for lat, lon, elev in zip(latList, lonList, elevList):
    fgv.add_child(
        folium.CircleMarker(location=[lat, lon],
                            radius=6,
                            popup="Elevation: " + str(elev) + "m",
                            fill_color=color_producer(elev),
                            color='grey',
                            fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r',
                             encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
