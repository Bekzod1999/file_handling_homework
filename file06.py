def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    for line in data:
        if line[-1] == '\n':
            k.append(len(line)-1)
        else:
            k.append(len(line))
    return k

f = open('txt_file/data06.txt').readlines()

print(main(f))

# til va tarjimon aytmagan kafedra

