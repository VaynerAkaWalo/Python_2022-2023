def odwracanieIt(L, left, right):
    while right > left:
        temp = L[right]
        L[right] = L[left]
        L[left] = temp
        right -= 1
        left += 1
    return L

def odwracanieRek(L, left, right):
    if(right < left):
        return L
    
    temp = L[right]
    L[right] = L[left]
    L[left] = temp
    return odwracanieRek(L, left + 1, right - 1)


