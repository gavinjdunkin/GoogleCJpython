#Problem: https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966
for l in range(int(input())):
    d, p = [s for s in input().split(" ")]
    d = int(d)
    shoot = 1
    damage = 0
    for a in p:
        if a == 'C':
            shoot *= 2
        if a == 'S':
            damage += shoot
    count = 0
    safety = 0
    while damage > d:
        for i in range(len(p), 0, -1):
            try:
                if p[i] == 'S' and p[i-1] == 'C':
                    p = p[0:i-1]+ p[i] + p[i-1] + p[i+1:len(p)]
                    count += 1
                    break
            except:
                pass
        safety += 1
        shoot = 1
        damage = 0
        for a in p:
            if a == 'C':
                shoot *= 2
            if a == 'S':
                damage += shoot
        if d < p.count('S'):
            count = 'IMPOSSIBLE'
            damage = d+1
            break
    print('Case #{}: {}'.format(l+1, count))
