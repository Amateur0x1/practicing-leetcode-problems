nums = [1,2,3,4,5,6]
for index ,i  in enumerate(nums):
    nums.remove(i)
    print("index_info",index, i)
    print("-----**")
    for index_j, j in enumerate(nums):
        print('index', index_j)
        nums.remove(j)
        print('remove_nums', nums)
        print('remove_num', j)
        nums.insert(index_j,j)
        print("appends", nums)
        print('-------------------------')