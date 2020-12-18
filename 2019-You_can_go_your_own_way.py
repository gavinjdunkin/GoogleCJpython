#Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
for b in range(int(input())):
    abc = int(input())
    lydia = str(input())
    string = ''
    for a in lydia:
        if a == 'S':
            string += 'E'
        else:
            string += 'S'
    print('Case #{}: {}'.format(b+1, string))
