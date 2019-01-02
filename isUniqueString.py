# CTCI Chapter 1
# Question 1.1 page 90


def isUnique_v1(string):
    """ str() -> bool
    implemented using set O(n)
    >>> isUnique_v1('')
    True
    >>> isUnique_v1('a')
    True
    >>> isUnique_v1('aabc')
    False
    >>> isUnique_v1('abcdef')
    True
    >>> isUnique_v1('ABCabc')
    False
    """
    return len(set(string.lower())) == len(string)

def isUnique_v2(string):
    """ str() -> bool
    implemented using dictionary O(n)
    >>> isUnique_v2('')
    True
    >>> isUnique_v2('a')
    True
    >>> isUnique_v2('aabc')
    False
    >>> isUnique_v2('abcdef')
    True
    >>> isUnique_v2('ABCabc')
    False
    """
    charSet = {}
    for char in string.lower():
        if char in charSet:
            return False
        charSet[char] = 1

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
