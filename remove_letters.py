# remove_letters.py start

def remove_letters(string):
    result = string
    # removing lower case
    result = result.replace('a', '')
    result = result.replace('b', '')
    result = result.replace('c', '')
    result = result.replace('d', '')
    result = result.replace('e', '')
    result = result.replace('f', '')
    result = result.replace('g', '')
    result = result.replace('h', '')
    result = result.replace('i', '')
    result = result.replace('j', '')
    result = result.replace('k', '')
    result = result.replace('l', '')
    result = result.replace('m', '')
    result = result.replace('n', '')
    result = result.replace('o', '')
    result = result.replace('p', '')
    result = result.replace('q', '')
    result = result.replace('r', '')
    result = result.replace('s', '')
    result = result.replace('t', '')
    result = result.replace('u', '')
    result = result.replace('v', '')
    result = result.replace('w', '')
    result = result.replace('x', '')
    result = result.replace('y', '')
    result = result.replace('z', '')

    # upper case
    result = result.replace('A', '')
    result = result.replace('B', '')
    result = result.replace('C', '')
    result = result.replace('D', '')
    result = result.replace('E', '')
    result = result.replace('F', '')
    result = result.replace('G', '')
    result = result.replace('H', '')
    result = result.replace('I', '')
    result = result.replace('J', '')
    result = result.replace('K', '')
    result = result.replace('L', '')
    result = result.replace('M', '')
    result = result.replace('N', '')
    result = result.replace('O', '')
    result = result.replace('P', '')
    result = result.replace('Q', '')
    result = result.replace('R', '')
    result = result.replace('S', '')
    result = result.replace('T', '')
    result = result.replace('U', '')
    result = result.replace('V', '')
    result = result.replace('W', '')
    result = result.replace('X', '')
    result = result.replace('Y', '')
    result = result.replace('Z', '')

    # removing white space
    result = result.replace(' ', '')

    # special characters in german
    result = result.replace('Ä', '')
    result = result.replace('ä', '')
    result = result.replace('Ö', '')
    result = result.replace('ö', '')
    result = result.replace('Ü', '')
    result = result.replace('ü', '')

    return result
# remove_letters.py end
