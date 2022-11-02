def cipher(text, shift, encrypt=True):
    """
    The function enciphers or deciphers a string rely on "shifting letters" by a fixed number of position. 

    Parameters
    ----------
    text: string
        A string as input
    shift: int
        An integer for a fixed number to shift letters.
    encrypt: bool
        Boolean to decide whether or not the function should encrypt the input. 

    Returns
    -------
    str
        Encrypt or decrypt string. 

    Examples
    --------
    >>> text = "crystal" 
    >>> shift = 26
    >>> cipher_jl6276.cipher(text, shift, encrypt = True)
    "CRYSTAL"
    
    >>> text2 = "cde"
    >>> shift2 = 1
    >>> cipher_jl6276.cipher(text, shift, encrypt = False)
    "bcd"
   
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

