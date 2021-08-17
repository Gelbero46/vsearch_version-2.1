#found = {'a' : 2, 'e' : 1 , 'i' : 0, 'o' : 0, 'u' : 0}
#print(found)
#for key, value in found.items():
#    print(key, "was found", str(value), 'time(s)')

def search4vowels(word:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def search4letter(phrase:str, letters: str = 'aeiou') -> set:
    """Return any vowels found in a supplied word."""
    return set(letters).intersection(set(phrase))


