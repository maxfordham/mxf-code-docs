# the simplest / cleanest way of accessing colour pallettes is to use Palletable
# view pallete's here: [finding-palettes](https://jiffyclub.github.io/palettable/#finding-palettes)

import ipywidgets as widgets
from palettable import tableau

def plot_color_list(li_colors):
    return widgets.VBox(
        [widgets.ColorPicker(concise=True, value=color) for color in li_colors]
    )
    
plot_color_list(tableau.Tableau_10.hex_colors)