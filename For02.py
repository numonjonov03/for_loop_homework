def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s=""
    k=range(0,n)
    for i in k:
        s+=str(k[i])+","
    s = s.strip(',')
    return s