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