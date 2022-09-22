def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    k = []
    s = 0
    for line in data:
        if line.isdigit():
            k += line

    for summ in k:
        s += int(summ)
    return s
    
# Read data from file
f = open('txt_file/data07.txt').read()

print(main(f))
# Read data from file