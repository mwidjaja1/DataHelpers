#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper Functions to create Matplotlib visualizations
"""

# import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors


def get_cmap(N):
    """ Returns a function that maps each index in 0, 1, ... N-1 to a distinct
        RGB color.

        Inputs:
        N = Number of colors to generate

        Outputs:
        A call to map_index_to_rbg_color. To invoke the color when plotting,
        call <output_from_get_cmap>(<current_int_index>).
    """
    color_norm = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')

    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color
