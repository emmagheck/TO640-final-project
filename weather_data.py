#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:20:32 2024

@author: emmaheck
"""

# Import Meteostat library
from datetime import datetime
# import matplotlib.pyplot as plt
from meteostat import Stations, Monthly

# Get Chicago (Midway) station id
stations = Stations()
stations = stations.nearby(41.7868, -87.7522)
midway = stations.fetch(1)

# Get Chicago (OHare) station id
stations = Stations()
stations = stations.nearby(41.9769, -87.9047)
ohare = stations.fetch(1)

# Get New York (JFK) station id
stations = Stations()
stations = stations.nearby(40.6446, -73.7797)
jfk = stations.fetch(1)

# Get New York (LGA) station id
stations = Stations()
stations = stations.nearby(40.7733, -73.8718)
lga = stations.fetch(1)

# Get New York (Newark) station id
stations = Stations()
stations = stations.nearby(40.6895, -74.1745)
newark = stations.fetch(1)

#Get Los Angeles (LAX) station id
stations = Stations()
stations = stations.nearby(33.9434, -118.4093)
lax = stations.fetch(1)

# Get Atlanta (ATL) station id
stations = Stations()
stations = stations.nearby(33.6362, -84.4294)
atl = stations.fetch(1)

# Get Miami (MIA) station id
stations = Stations()
stations = stations.nearby(25.7951, -80.2795)
mia = stations.fetch(1)

# Print DataFrame
print(midway)
print(ohare)
print(jfk)
print(lga)
print(newark)
print(lax)
print(atl)
print(mia)


# Set time period
start = datetime(2021, 1, 1)
end = datetime(2023, 12, 31)

# Get Monthly data for Midway station
data_midway = Monthly('72534', start, end)
data_midway = data_midway.fetch()

#Get Monthly data for OHare station
data_ohare = Monthly('72530', start, end)
data_ohare = data_ohare.fetch()

# Get Monthly data for JFK station
data_jfk = Monthly('74486', start, end)
data_jfk = data_jfk.fetch()

# Get Monthly data for LGA station
data_lga = Monthly('KNYC0', start, end)
data_lga = data_lga.fetch()

# Get Monthly data for Newark station
data_newark = Monthly('KLDJ0', start, end)
data_newark = data_newark.fetch()

# Get Monthly data for LAX station
data_lax = Monthly('72295', start, end)
data_lax = data_lax.fetch()

# Get Monthly data for ATL station
data_atl = Monthly('KFTY0', start, end)
data_atl = data_atl.fetch()

# Get Monthly data for MIA station
data_mia = Monthly('72202', start, end)
data_mia = data_mia.fetch()

print(data_midway)
print(data_ohare)
print(data_jfk)
print(data_lga)
print(data_newark)
print(data_lax)
print(data_atl)
print(data_mia)

import pandas as pd

# Combine data
weather_data = pd.concat([data_midway, data_ohare, data_jfk, data_lga, data_newark, data_lax, data_atl, data_mia])

# Drop the 'tsun' column because it returned all null values
weather_data.drop(columns=['tsun'], inplace=True)

# Add column for Airport
weather_data['Airport'] = ['Midway'] * len(data_midway) + ['OHare'] * len(data_ohare) + ['JFK'] * len(data_jfk) + ['LGA'] * len(data_lga) + ['Newark'] * len(data_newark) + ['LAX'] * len(data_lax) + ['ATL'] * len(data_atl) + ['MIA'] * len(data_mia)

# Add column for City
weather_data['City'] = ['Chicago'] * len(data_midway) + ['Chicago'] * len(data_ohare) + ['New York'] * len(data_jfk) + ['New York'] * len(data_lga) + ['New York'] * len(data_newark) + ['Los Angeles'] * len(data_lax) + ['Atlanta'] * len(data_atl) + ['Miami'] * len(data_mia)

# Write to csv file
weather_data.to_csv('weather_data.csv', index=False)
