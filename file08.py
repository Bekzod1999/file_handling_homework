def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
        if s < int(summ):
            s = int(summ)
        
    return s

# Read data from file

f = open('txt_file/data08.txt').read()

print(main(f))