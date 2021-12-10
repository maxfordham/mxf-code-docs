import pandas as pd
from pathlib import Path
import toml
from typing import List
from dataclasses import dataclass, asdict
from IPython.display import Markdown
import codecs
import re
import glob
import fnmatch
import os

# _utils.py ####
def recursive_glob(rootdir='.', pattern='*', recursive=True):
    """ 
    Search recursively for files matching a specified pattern.
    
    name: 
        20180506~3870~code~pyfnctn~jg~recursive_glob~A~0
    tags: 
        rootdir, pattern, finding-files
    Reference: 
        Adapted from: http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
        string pattern matching: https://jakevdp.github.io/WhirlwindTourOfPython/14-strings-and-regular-expressions.html
    Args:
        **rootdir (string): the directory that you would like to recursively search. 
            recursive means it will automatically look in all folders within this directory
        **pattern (string): the filename pattern that you are looking for.
        **recursive (bool): define if you want to search recursively (in sub-folders) or not. 
        
    Returns:
        matches(list): list of filedirectories that match the pattern
    Example:
        rootdir='J:\J'+'J9999'
        pattern='????????_????_?*_?*_?*_?*_?*_?*'
        recursive_glob(rootdir=rootdir, pattern=pattern, recursive=True)
    """
    matches=[]
    if recursive ==True:
        for root, dirnames, filenames in os.walk(rootdir):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))

    else:
        #a = glob.glob(pattern)
        for filename in glob.glob1(rootdir,pattern):
            matches.append(os.path.join(rootdir,filename))
            
    return matches

def flatten_list(list_of_lists: list)-> list: 
    """Flatten a list of (lists of (lists of strings)) for any level 
    of nesting
    
    Args:
        list_of_lists: with mix of lists and other
    Returns:
        rt: list with no nested lists
        
    """
    rt = []
    for i in list_of_lists:
        if isinstance(i,list): rt.extend(flatten_list(i))
        else: rt.append(i)
    return rt

def srch_tgs(df, clmn_nm, srch_tg, clmn_rtrn=None):
    """
    name:
        20180929~3870~dev~pyfnctn~jg~pandas indx mtch fnctn~B~0
    tags:
        index, match, search, tags, list, cross-reference
    Args:
        df (pd.DataFrame)=dataframe, containing a column with a tag to search for
        clmn_nm (string)=the column you want to search for a specific "srch_tg"
        srch_tg (string)=a string that you want to find in the column ['clmn_nm']
    Keyword Args:
        clmn_rtrn (string)=the column you want to output is ['clnm_nm']
            contains 'srch_tg'

    returns:
        if clmn_rtrn = None:
            li (list): a list of index values for the rows of the df where
            df['clmn_nm'] contained the search tag "srch_tg"
        elif: clmn_rtrn = var:
            li (list): a list of 'clmn_rtrn' values for the rows of the df
            where df['clmn_nm'] contained the search tag "srch_tg"

    """
    df[clmn_nm] = df[clmn_nm].astype(str)
    end = len(df)
    tag = srch_tg
    li = []
    for n in range(0, end):
        if tag in df.iloc[n][clmn_nm]:
            li.append(df.iloc[n].name)  # then return index

    if clmn_rtrn == None:
        return li
    else:
        return df.loc[li][clmn_rtrn]
    
# 

def get_jb_files(fdir=Path('.')):
    exts = ['*.ipynb', '*.md']
    fnms = []
    for e in exts: 
        tmp = recursive_glob(rootdir=fdir, pattern=e, recursive=True)
        fnms.extend(tmp)
    fpths = [Path(fnm) for fnm in fnms if ".ipynb_checkpoints" not in fnm]
    names = [p.stem for p in fpths]
    return dict(zip(names,fpths))

def create_img_fpth(tech):
    """creates fpth from name"""
    for t in tech['tech']:
        if t['image'] == '':
            name = t['name']
            t['image'] = f'images/{name}-icon.png'

def create_local_link(tech, paths_map):
    """"""
    for t in tech['tech']:
        if t['local_link'] == '':
            for tag in t['tags']:
                if tag in paths_map.keys():
                    t['local_link'] = paths_map[tag]
                else:
                    t['local_link'] = ''

@dataclass
class MfTech:
    name: str
    url: str
    description: str
    local_link: str
    image: str

@dataclass
class TechGroup:
    tag: str
    description: str
    local_link: str
    tech: List[MfTech] 


def create_tech_group(df, tag, tag_des) -> TechGroup:

    li_tmp = []
    df_tmp = srch_tgs(df, 'tags', tag, clmn_rtrn=list(df)).reset_index()
    keys = list(MfTech.__dict__['__annotations__'].keys())
    for index, row in df_tmp.iterrows():
        di = { key: dict(row)[key] for key in keys }
        tech = MfTech(**di)
        li_tmp.append(tech)
    if tag in tag_des.keys():
        description = tag_des[tag]
    else:
        description = ""
    local_link = df_tmp.local_link.unique()[0]
    return TechGroup(tag=tag, tech=li_tmp, description=description, local_link=local_link)

def create_tech_groups(df, tags, tag_des):

    li_tech_groups = []
    for tag in tags:
        #if type(tag) == list:
        #    for t in tag:
        #        li_tech_groups.append(create_tech_group(df, t, tag_des))
        #else:
        li_tech_groups.append(create_tech_group(df, tag, tag_des))
    return tuple(li_tech_groups)


def md_img_link(tech: MfTech)-> str:
    return f'[![{tech.name}]({tech.image})]({tech.url} "{tech.description}")'

def md_img_links(grp: TechGroup)-> str:
    return "\n".join([md_img_link(tech) for tech in grp.tech])

def create_panel_obj(grp: TechGroup) -> str:
    imgs = md_img_links(grp)
    return f"""
**[{grp.tag}]({grp.local_link})**
^^^
{grp.description}

{imgs}

---
"""
def create_panel_objs(li_grps: List[TechGroup]) -> str:
    return "\n".join([create_panel_obj(grp) for grp in li_grps])

def create_panel(tu_tech_grps: List[TechGroup]) -> str:
    output = """

:::{panels}
:container: +full-width text-center
:column: col-lg-4 px-2 py-2
:card:

""" + create_panel_objs(tu_tech_grps) + "\n :::"
    
    return output

def create_panels(df):
    tags = list(set(flatten_list(df.tags.tolist())))
    tags = [
    'software-automation',
    'authoring-tools',
    'frontend',
    'packaging',
    'deploying',
    'databases',
    'backend-tools',
    'external-experts',
    'documentation',
    #'developing',
    ]
    tag_des = tech['tags']
    tu_tech_grps = create_tech_groups(df, tags, tag_des)
    md_panels = create_panel(tu_tech_grps)
    return md_panels

def create_table(df):
    df1 = df.copy()
    df1['technology'] = "[!["+df['name']+"]("+df['image']+")  "+df['name']+"]("+df['url']+")"  # { width=150px }
    cols = ['technology', 'description']
    df1 = df1[cols] 
    return df1.to_markdown()

if __name__ == "__main__":
    if __debug__:
        pdf = True  #False #True
    else:
        import sys
        try:
            pdf = sys.argv[1]
        except:
            pdf = False
    # print(os.path.dirname(__file__))
    # pdf = False
    dirname = os.path.dirname(__file__) or '.'
    os.chdir(dirname)
    path_tech = Path('_preferred_technologies.toml')
    path_docs = Path('.')
    tech = toml.load(path_tech)
    create_img_fpth(tech)
    paths_map = get_jb_files(path_docs)
    create_local_link(tech, paths_map)
    df = pd.DataFrame.from_dict(tech['tech'])
    if pdf: 
        md_body = create_table(df)
    else:
        md_body = create_panels(df)

    md_header = """
# mfcode_docs

**Max Fordham Engineering Development Best Practice**

This documentation aims to provide high-level, non-verbose notes outlining Max Fordham's engineering software development infrastructure.
Links to external sources and standards to describe the approach are preferred where possible.
The intended audience are those contributing-to and maintaining internal development tools, or external parties and collaborators interested in our approach.
Code snippets are encouraged.

**We stand on the shoulders of giants**. Our software is built on robust, high-quality opensource packages, and we are proud to share the work that we produce with the opensource community.
When writing code there are always many solutions to a problem;
we standardise the technologies we use for a given task to ensure a consistent approach across projects. See below for key technologies on which we rely.

"""
    md = md_header + md_body 
    file = codecs.open("index.md", "w", "utf-8")
    file.write(md)
    file.close()