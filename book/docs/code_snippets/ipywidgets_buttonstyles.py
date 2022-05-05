import ipywidgets as widgets

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