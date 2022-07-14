# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Colors
#
# the simplest / cleanest way of accessing colour pallettes is to use Palletable
# view pallete's here: [finding-palettes](https://jiffyclub.github.io/palettable/#finding-palettes)

import ipywidgets as widgets
from palettable import tableau, 

def plot_color_list(li_colors):
    return widgets.VBox(
        [widgets.ColorPicker( value=color) for color in li_colors] #concise=True,
    )

plot_color_list(tableau.Tableau_10.hex_colors)


