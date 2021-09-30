count = int(input())
ls = list(map(int, input().split()))
t = tuple(map(int, ls[:count]))
print(hash(t))