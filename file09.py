def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
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
        if s > int(summ):
            s = int(summ)
        
    return s

# Read data from file

f = open('txt_file/data09.txt').read()

print(main(f))
# Read data from file