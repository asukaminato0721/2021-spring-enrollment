from collections import deque


def test(n):
    q = deque([n])
    cnt = 0
    _set = set()
    while q:
        for _ in range(len(q)):
            tmp = q.popleft()
            if tmp == 0:
                print(cnt)
                return
            if tmp % 2 == 0 and tmp // 2 not in _set:
                q.append(tmp // 2)
                _set.add(tmp // 2)
            if tmp % 3 == 0 and tmp // 3 not in _set:
                q.append(tmp // 3)
                _set.add(tmp // 3)
            if tmp - 1 not in _set:
                q.append(tmp - 1)
                _set.add(tmp - 1)

        cnt += 1


T = int(input())
for _ in range(T):
    test(int(input()))
