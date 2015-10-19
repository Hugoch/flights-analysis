#!/usr/bin/env python

import pandas as pd
from gcmap import GCMapper, Gradient

# define CSV colum names
CSV_COLS = ('dep_lat', 'dep_lon', 'arr_lat', 'arr_lon', 'nb_flights', 'CO2')

routes = pd.read_csv('data.csv', names=CSV_COLS,
                     na_values=['\\N'], sep=';', skiprows=1)

# create gradient to color the routes according to the number of flights
grad = Gradient(((0, 0, 0, 0), (0.5, 204, 0, 153), (1, 255, 204, 230)))
# initialize GCMapper and set data
gcm = GCMapper(cols=grad, height=2000, width=4000)
gcm.set_data(routes['dep_lon'], routes['dep_lat'], routes['arr_lon'],
             routes['arr_lat'], routes['nb_flights'])
# run & save
img = gcm.draw()
img.save('flights_map_gcmap.png')
