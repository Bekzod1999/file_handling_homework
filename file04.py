def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    for strr in data:
        if strr.isalpha():
            k += strr
    return k
    
# Read data from file
f = open('txt_file/data04.txt').read()

print(main(f))