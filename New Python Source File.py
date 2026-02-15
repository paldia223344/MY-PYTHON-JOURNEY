if __name__ == '__main__':
    N = int(input())   # number of commands
    my_list = []

    for _ in range(N):
        parts = input().split()
        cmd = parts[0]

        if cmd == "insert":
            i = int(parts[1])
            e = int(parts[2])
            my_list.insert(i, e)

        elif cmd == "print":
            print(my_list)

        elif cmd == "remove":
            e = int(parts[1])
            my_list.remove(e)

        elif cmd == "append":
            e = int(parts[1])
            my_list.append(e)

        elif cmd == "sort":
            my_list.sort()

        elif cmd == "pop":
            my_list.pop()

        elif cmd == "reverse":
            my_list.reverse()
