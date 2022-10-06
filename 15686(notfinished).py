from itertools import combinations

n, m = map(int, input().split())

#지도
arr = [list(map(int, input().split())) for _ in range(n)]  

house = [] # 집 저장해서 검사
chicken = [] # 치킨집 저장해서 검사

#집, 치킨집 좌표 저장
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if arr[i][j] == 1:
      house.append((i, j))
    if arr[i][j] == 2:
      chicken.append((i, j))

      
result = 1e9 #현재 최소 거리 10억이라고 가정
# 예시 1: ((1, 2), (2, 2), (4, 4)), 해당 변수 m 과 chicken으로 치킨집 경우의 수(조합) 생성
for chick_combi in combinations(chicken, m): 
  city_chicken = 0 # 도시 치킨거리
  for house_loc in house:
    for chicken_loc in chick_combi: #첫번쨰 회전에서 무한대와 비교하고, 이후에도 비교후 최소값만 들어갈것
      result = min(result, abs(house_loc[0]-chicken_loc[1]) + abs(house_loc[1]-chicken_loc[1])) 
    city_chicken += result #해당 집과 모든 치킨집을 비교한 거리 중 최소를 모두 더함
  result = min(result, city_chicken)

print(result)