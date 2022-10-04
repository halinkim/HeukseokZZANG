def comp(arr):
    dic = {x: i for i, x in enumerate(sorted(set(arr)))}
    return [dic[x] for x in arr]