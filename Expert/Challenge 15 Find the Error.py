def cleanList(obj) -> bool:
    """Return whether the given nested list is "clean"."""
    if isinstance(obj, int):
        return True
    elif isinstance(obj, list):
        if not len(obj)==0:
            return True
    else:
        all_ints = True
        all_lists = True
        all_semi = True
        for sublist in obj:
            if isinstance(sublist, int):
                all_lists = False
            elif isinstance(sublist, list):
                all_ints = False
                all_semi = cleanList(sublist)
    return (all_ints or all_lists) and all_semi

print(cleanList([[1], [4], [7], [6]]))