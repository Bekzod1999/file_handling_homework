def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    i = []
    for listt in data:
        if listt != ',':
            listt = int(listt)
            k.append(listt)
    return k
# Read data from file

f = open('txt_file/data01.txt').read()
print(main(f))