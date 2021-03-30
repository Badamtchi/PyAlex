def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if midpoint == target:
            return True
        elif midpoint < target:
            return recursive_binary_search(list[midpoint+1:], target)
        elif midpoint > target:
            return recursive_binary_search(list[:midpoint], target)
    return None

def verify(result):
    print('Target found:', result)