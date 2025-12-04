class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        n = len(directions)
        dp = [0] * n
        first = True
        cnt = 0
        ans = 0
        for i in range(n):
            if first and directions[i] == "L":
                continue
            else:
                first = False
            if cnt == 0 and directions[i] == "L":
                ans += 1
            elif directions[i] == "R":
                cnt += 1
            elif directions[i] == "L":
                ans += cnt + 1
                cnt = 0
            elif directions[i] == "S":
                ans += cnt
                cnt = 0
        return ans

# 최초 작성한 답
# 하지만 왼쪽, 오른쪽만 strip으로 트리밍 하고 L, R 갯수만 세어도 끝임..
class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")

        return directions.count("R") + directions.count("L")