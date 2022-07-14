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

# # Remove invalid characters from String

# +

FILENAME_FORBIDDEN_CHARACTERS = {"<", ">", ":", '"', "/", "\\", "|", "?", "*"}

# +
def modify_string(s, 
                  remove_forbidden_chars=True, 
                  remove_spaces=False, 
                  fn_on_string=None,
                  max_length=None,
                  min_length=None):
    """
    
    Reference:
        [naming-a-file](https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file)
    """
    if remove_spaces:
        s = s.replace(" ", "")
    if remove_forbidden_chars:
        for c in FILENAME_FORBIDDEN_CHARACTERS:
            s = s.replace(c, "")
    if fn_on_string is not None:
        s = fn_on_string(s)
    if min_length is not None:
        if len(s) < min_length:
            s = s + "-"*(min_length-len(s))
    if max_length is not None:
        if len(s) > max_length:
            s = s[0:max_length]
    return s

modify_string('<this> is a string with max length',max_length=30)
# -


