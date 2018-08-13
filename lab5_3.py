def super_fibonacci(n,m):
    if m>=n:
        return 1
    else:
        sup_list = [1 for i in range(m)]
        for i in range(n-m):
            new_value = 0
            for j in range(m):
                new_value = new_value + sup_list[j]
            sup_list.insert(0,  new_value)
        return sup_list[0]
