SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    """Convert a size to human-readable form.
    Keyword arguments:
    size -- file size in bytes

    Return:string
    """
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('namber too large') #raise = throw in c-sharp