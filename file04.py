def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    for line in data:
        if line.isalpha():
            k += line
        elif line == '\n':
            k += '\n'
    return k
    
# Read data from file
f = open('txt_file/data04.txt').read()

print(main(f))