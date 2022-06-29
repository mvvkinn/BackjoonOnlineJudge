tested, reward = map(int, input().split())

score = list(list(map(int, input().split())))

score.sort(reverse=True)

print(score[reward-1])