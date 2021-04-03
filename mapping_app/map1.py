import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elevation):
    if(elevation < 1000):
        return "green"
    elif(elevation > 1000 and elevation < 2000):
        return "purple"
    else:
        return "beige"


latids = df["LAT"]
longids = df["LON"]
info = df["ELEV"]
map = folium.Map(zoom_start=5.5, location=[38.58, -99.09], tiles='Stamen Toner')
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, lg, inf in zip(latids, longids, info):
    iframe = folium.IFrame(html=html % str(inf), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location = [lt, lg], fill_color = color_producer(inf), color = "grey", fill = True, fill_opacity = 0.7, radius=6, popup = folium.Popup(iframe)))
    #fg.add_child(folium.Marker(location = [lt, lg], icon = folium.Icon(color=color_producer(inf)), popup = folium.Popup(iframe)))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                                                                                   else 'purple' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
