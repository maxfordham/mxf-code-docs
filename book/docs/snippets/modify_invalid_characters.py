import stringcase
FILENAME_FORBIDDEN_CHARACTERS = {"<", ">", ":", '"', "/", "\\", "|", "?", "*"}

def modify_string(s, 
                  remove_forbidden_chars=True, 
                  remove_spaces=True, 
                  fn_on_string=stringcase.pascalcase,
                  max_length=None
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
    if min_length is not None:
        if len(s) > max_length:
            s = s[0:max_length]
    return s