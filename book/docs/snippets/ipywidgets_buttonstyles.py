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

# # Button Styles

import ipywidgets as widgets
from markdown import markdown


def _markdown(value="_Markdown_", **kwargs):
    """
    a simple template for markdown text input that templates required input
    fields. additional user defined fields can be added as kwargs
    """
    _kwargs = {}
    _kwargs["value"] = markdown(value)  # required field
    _kwargs.update(kwargs)  # user overides
    return widgets.HTML(**_kwargs)


def display_button_styles():
    """displays default ipywidget button styles"""
    styles = ["primary", "success", "info", "warning", "danger"]
    for s in styles:
        b = widgets.ToggleButton(description=s, button_style=s)
        t = _markdown(
            '```widgets.ToggleButton(description="{}", button_style="{}")```'.format(
                s, s
            )
        )
        display(widgets.HBox([b, t]))


display_button_styles() 


