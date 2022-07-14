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

# # Simple UI class with ipywidgets
import ipywidgets as widgets
import traitlets

class Test(traitlets.HasTraits):
    value = traitlets.Unicode()
    def __init__(self, value):
        self.text = widgets.Text(disabled=True)
        self.text1 = widgets.Text()
        self.text.value = value

class TestControls:
    def _init_controls(self):
        self.observe(self._update_change, "value")
        self.text1.observe(self._update_change1, "value")
        self.text1.observe(self._update_change1_1, "value")
        
    def _update_change(self, onchange):
        print('_update_change')
        self.text.value = self.value
        
    def _update_change1(self, onchange):
        print('_update_change1')
        self.value = self.text1.value + '-ffs'
        
    def _update_change1_1(self, onchange):
        print('_update_change1_1')

class ParentTest(Test, TestControls):
    def __init__(self, value):
        super().__init__(value)
        self._init_controls()
        
    def _ipython_display_(self):
        display(self.text)
        display(self.text1)

if __name__ == "__main__":
    t = ParentTest('asdf')
    display(t)
