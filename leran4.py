if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
    sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    for k,v in d:
        print(k[v])

