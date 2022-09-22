# def main(data:str):
#     """
#     The data is from the file. Find the each row length and return as list type.
#     Args:
#         data: str
#     Returns:
#         list: return answer
#     """
#     k = []
#     lines = 0
#     for line in data:
#         if line == '\n':
#             lines += 1
#             break
#         # print(lengg)
#     return lines
# # Read data from file

# f = open('txt_file/data06.txt').read()

# print(main(f))

















def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    lines = 0
    for line in data:
        k.append(len(line)-1)
    return k

f = open('txt_file/data06.txt').readlines()

print(main(f))