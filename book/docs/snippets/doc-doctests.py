import pathlib

def get_path(path, fdir=None):
    """
    returns a full file path based on path, fdir. Appends path to fdir,
    but ignores appending if fdir already in path (thus supporting round-trips).

    Args:
        path (pathlib.Path): path
        fdir (pathlib.Path): fdir

    Returns:
        path (pathlib.Path): path

    Examples:
        >>> import pathlib
        >>> mk_str = lambda tu: tuple(str(t) for t in tu)

        # 1. if absolute path given return absolute path
        >>> path = pathlib.Path("/a/b/c.ext")
        >>> fdir = None
        >>> mk_str(get_path(path, fdir=fdir))
        ('/a/b/c.ext', 'None')

        # 2. if absolute path given return absolute path
        # as above but a logger.warning raised
        >>> path = pathlib.Path("/a/b/c.ext")
        >>> fdir = pathlib.Path("/d")
        >>> mk_str(get_path(path, fdir=fdir))
        ('/a/b/c.ext', 'None')

        # 3. if relative path and fdir is none
        >>> path = pathlib.Path("a/b/c.ext")
        >>> fdir = None
        >>> mk_str(get_path(path, fdir=fdir))
        ('a/b/c.ext', 'None')

        # 4. if relative path not in given fdir
        >>> path = pathlib.Path("a/b/c.ext")
        >>> fdir = pathlib.Path("d/e")
        >>> mk_str(get_path(path, fdir=fdir))
        ('a/b/c.ext', 'd/e')

        # 5. if path in given fdir
        >>> path = pathlib.Path("/a/b/c.ext")
        >>> fdir = pathlib.Path("/a/b")
        >>> mk_str(get_path(path, fdir=fdir))
        ('c.ext', '/a/b')
    """
    if fdir is None:
        # 1
        return path, fdir
    elif (
        fdir is not None
        and path.is_absolute()
        and not is_parent(fdir, path, error_if_false=False)
    ):
        # 2
        logger.warning(
            f"fdir set to None as not in absolute path. fdir={fdir}, path={path}"
        )
        fdir = None
        return path, fdir
    elif is_parent(fdir, path, error_if_false=False):
        return path_minus_fdir(path, fdir), fdir
    elif not is_parent(fdir, path, error_if_false=False) and not path.is_absolute():
        return path, fdir
    elif is_parent(fdir, path, error_if_false=True):
        # the above should raise an error as path not in fdir
        pass
    else:
        raise ValueError("unknown case for get_path")


# -


def get_path_new(path, fdir=None):
    """
    returns a full file path based on path, fdir. Appends path to fdir,
    but ignores appending if fdir already in path (thus supporting round-trips).

    Args:
        path (pathlib.Path): path
        fdir (pathlib.Path): fdir

    Returns:
        path (pathlib.Path): path

    Examples:
        >>> import pathlib
        >>> mk_str = lambda tu: tuple(str(t) for t in tu)

        # 1. if absolute path given return absolute path
        >>> path = pathlib.Path("/a/b/c.ext")
        >>> fdir = None
        >>> mk_str(get_path(path, fdir=fdir))
        ('/a/b/c.ext', 'None')

        # 2. if absolute path and fdir given return absolute path
        # as above but a logger.warning raised
        >>> path = pathlib.Path("/a/b/c.ext")
        >>> fdir = pathlib.Path("/d")
        >>> mk_str(get_path(path, fdir=fdir))
        ('/a/b/c.ext', 'None')

        # 3. if relative path and fdir is none
        >>> path = pathlib.Path("a/b/c.ext")
        >>> fdir = None
        >>> mk_str(get_path(path, fdir=fdir))
        ('a/b/c.ext', 'None')

        # 4. if relative path not in given fdir
        >>> path = pathlib.Path("a/b/c.ext")
        >>> fdir = pathlib.Path("d/e")
        >>> mk_str(get_path(path, fdir=fdir))
        ('d/e/a/b/c.ext', 'd/e')

        # 5. if path in given fdir
        >>> path = pathlib.Path("/a/b/c.ext")
        >>> fdir = pathlib.Path("/a/b")
        >>> mk_str(get_path(path, fdir=fdir))
        ('/a/b/c.ext', '/a/b')

        # 6. if path in given fdir
        >>> path = pathlib.Path("a/b/c.ext")
        >>> fdir = pathlib.Path("a/b")
        >>> mk_str(get_path(path, fdir=fdir))
        ('a/b/c.ext', 'a/b')
    """
    if fdir is None:
        # 1, 3
        return path, fdir
    elif (
        fdir is not None
        and path.is_absolute()
        and not is_parent(fdir, path, error_if_false=False)
    ):
        # 2
        logger.warning(
            f"fdir set to None as not in absolute path. fdir={fdir}, path={path}"
        )
        fdir = None
        return path, fdir
    elif not is_parent(fdir, path, error_if_false=False) and not path.is_absolute():
        # 4
        return fdir / path, fdir
    elif is_parent(fdir, path, error_if_false=False):
        # 5
        return path, fdir
    elif is_parent(fdir, path, error_if_false=True):
        # the above should raise an error as path not in fdir
        pass
    else:
        raise ValueError("unknown case for get_path")
