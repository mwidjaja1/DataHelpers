#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper Functions to create a Folium Maps Plot
"""

import folium
import pandas as pd


def scatterplot_map(data, map_opts, out_path):
    """ Creates a folium (Open source tiles) map with circle marker plots, the
        markers having no interactivity.

        Inputs:
        data: A dictionary or Pandas series with index col of data.
              Keys or index must be a tuple of coordinates as (<lat>, <lon>)
              Values must be how many 'items' are in that coordinate.
        map_opts: Dict of map settings including these keys:
                  lat = latitude center of map
                  lng = longitude center of map
                  size = A number which will be multipled by the value to
                         determine the size of the circle marker.
                  color = HTML color code for the circle
        out_path: Path to save the HTML plot to
    """
    map = folium.Map(location=[map_opts['lat'], map_opts['lng']])
    if isinstance(data, dict):
        keys = data.keys()
    elif isinstance(data, pd.Series):
        keys = data.index
    else:
        print('ERROR: Unknown data type to plot here')
        keys = []

    for coordinate in keys:
        lat, lon = coordinate  # (y,x) effectively
        folium.CircleMarker([lat, lon],
                            radius=data[coordinate] * map_opts['size'],
                            popup='Occurances: {}'.format(data[coordinate]),
                            fill_color=map_opts['color']).add_to(map)
    map.save(out_path)
