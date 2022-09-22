# from curses.ascii import isdigit
# from unicodedata import digit


def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    d = 0
    s = 0
    for digitt in data:
        if digitt.isdigit():
            d += 1
        else:
            s += 1
    k.append(d)
    k.append(s)
    return k

f = open('txt_file/data05.txt').read()

print(main(f))


# Read data from file