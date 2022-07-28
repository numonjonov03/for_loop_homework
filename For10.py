def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(len(list1)):
        s+=[list1[i].capitalize()]
    return s