# A. Слишком длинные слова
# строки


n = int(input())
for i in range(n):
    w = input()
    if len(w)<=10:
        print(w)
    else:
        print(w[0]+str(len(w[1:-1]))+w[-1])

