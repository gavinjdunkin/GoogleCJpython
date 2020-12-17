for i in range(int(input())):
    n, k = [int(s) for s in input().split(" ")]
    listc = []
    listd = []
    listc = [int(s) for s in input().split(" ")]
    listd = [int(s) for s in input().split(" ")]
    count = 0
    for a in range(n):
        for b in range(a+1,n+1):
            listsc = listc[a:b]
            listsc.sort()
            listsd = listd[a:b]
            listsd.sort()
            if abs(listsc[len(listsc)-1] - listsd[len(listsd)-1]) <= k:
                count += 1
    print('Case #{}: {}'.format(i+1,count))
