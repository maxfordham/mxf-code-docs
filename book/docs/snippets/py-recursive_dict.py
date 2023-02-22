
# NOT working!
def get_flat_index(di):
    global index 
    global flat 
    for k, v in di.items():
        index = tuple(list(index)+[k])
        if isinstance(v, dict):
            get_flat_index(v)
        else:
            flat[index] = v
            index = ()
    return flat
        
flat = {}
index = ()
di = {
    "a":{
        "aa":{"aaa":"aaaa"},
        "bb":{"bbb":"bbbb"},
    },
    "b":{
        "cc":{"ccc":"cccc"},
        "dd":{"ddd":"dddd"},
    },
    "c":"ee"
}
di_ = get_flat_index(di)
di_