items = [15, 7, 3, 30, 56]
print('기본 재료들: ', items)

new_item = 0

while min(items) >= 30:
  min_item = min(items)
  new_item = min(items) + min(min(items * 2))

print(new_item) 