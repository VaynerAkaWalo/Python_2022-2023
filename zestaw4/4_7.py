def flatten(sequence):
    result = []
    for x in sequence:
        if(isinstance(x, (list, tuple))):
            result += flatten(x)
        else:
            result.append(x)
    
    return result
