people = ['chloe', 'bonnie', 'alice', 'chloe',
         'david', 'chris', 'charlotte', 'kane',
         'ryan', 'david', 'spencer', 'bella']
completion = ['chloe', 'bonnie', 'alice', 'david',
              'david', 'charlotte', 'kane', 'ryan',
              'bella']

print("전체 참가자: ", people)
print("완주한 사람: ", completion)

# 완주하지 못한 사람을 확인하여 출력하세요.

uncompletion = []
for person in people:
    if person not in completion:
        uncompletion.append(person)
print("완주하지 못한 사람: ", uncompletion, " (", len(uncompletion), "명)")