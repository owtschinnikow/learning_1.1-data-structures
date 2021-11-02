n, parents = int(input()), [int(i) for i in input().split()]
a = [[] for i in range(n + 1)]
for i in range(n):
  a[parents[i]] += [i]

root, lev = a[-1], 0
while len(root):
  q, root = root, []
  for b in q:
    root += a[b]
  lev += 1
print(lev)