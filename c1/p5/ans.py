print((lambda arr: (lambda set_list: (set_list.sort(reverse=True) != None) + set_list[1] if len(set_list) != 1 else -1)(list(set(arr))))([int(input()) for i in range(int(input()))]))