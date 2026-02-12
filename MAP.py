# # MAP FUNCTION

# def cube(v):
#     return v**3
# print(cube(6))

# l = [1,3,4,6,7,9]
# # newl = []
# # for i in l:
# #     newl.append(cube(i))
# cube1 = list(map(cube ,l))
# print(cube1)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest = max(arr)
    while highest in arr:
        arr.remove(highest)
    runnerup = max(arr)
    print(runnerup)