def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    for line in data:
        if line.isdigit():
            k += line
        # print(line)
    return k
    
# Read data from file
f = open('txt_file/data03.txt').read()

print(main(f))