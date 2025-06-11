def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(
        max(0, min(r, 255)),
        max(0, min(g, 255)),
        max(0, min(b, 255))
    )
