# shading levels of each contribution tiles
def intensity_level(count: int) -> int:
    if count <= 0:
        return 0
    elif count < 3:
        return 1
    elif count < 6:
        return 2
    elif count < 10:
        return 3
    else:
        return 4
