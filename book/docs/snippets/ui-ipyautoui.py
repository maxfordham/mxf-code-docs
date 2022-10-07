# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
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

# +
# ipyautoui simple, from pydantic model

import typing
from enum import Enum
from pydantic import Field, conint, constr
from ipyautoui.basemodel import BaseModel
from pydantic.color import Color
from datetime import datetime, date
import pathlib

from ipyautoui import AutoUi

STR_MARKDOWN = """
See details here: [__commonmark__](https://commonmark.org/help/)

or press the question mark button. 
"""

class GenderEnum(str, Enum):
    """available genders. this is just an example."""

    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class TestAutoLogicSimple(BaseModel):
    """this is a test UI form to demonstrate how pydantic class can be used to generate an ipywidget input form. 
    only simple datatypes used (i.e. not lists/arrays or objects)
    """

    string: str = Field(default="adsf", description="a description about my string")
    int_slider: conint(ge=0, le=3) = 2
    int_text: int = 1
    int_range_slider: tuple[int, int] = Field(default=(0, 3), ge=0, le=4)  # check
    float_slider: float = Field(default=2.2, ge=0, le=3)
    float_text: float = 2.2
    float_text_locked: float = Field(default=2.2, disabled=True)
    float_range_slider: tuple[float, float] = Field(default=(0, 2.2), ge=0, le=3.5)
    checkbox: bool = True
    dropdown: GenderEnum = Field(
        default=GenderEnum.female, description="updated description"
    )
    combobox: str = Field(
        default="asd", enum=["asd", "asdf"], autoui="ipyautoui.autowidgets.Combobox",
    )
    text: constr(min_length=0, max_length=20) = "short text"
    text_area: constr(min_length=0, max_length=800) = Field(
        "long text " * 50, description="long text field"
    )
    markdown: str = Field(
        STR_MARKDOWN, description="markdown widget!", format="markdown"
    )
    color_picker_ipywidgets: Color = "#f5f595"
    date_picker: typing.Optional[
        date
    ] = date.today()  # TODO: serialisation / parsing round trip not working...


AutoUi(TestAutoLogicSimple, path='ui.json')    
