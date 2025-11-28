# 2025 프로그래머스 코드 챌린지 2차 예선
# 완전 범죄

def solution(info, n, m):
    global minval, check
    check = set()
    ret = [0] * len(info)
    minval = 987654321
    def sol(depth, flag, sa, sb):
        global minval, check
        # print(flag)
        # print(depth, sa, sb)
        ret[depth] = flag
        if flag:
            sa += info[depth][0]
            if sa >= n:
                return
        else:
            sb += info[depth][1]
            if sb >= m:
                return
        if (sa, sb, depth) in check: # <-- 이 부분이 킥임, 같은 depth상태에서 sa, sb가 동일하다면 이후 결과는 스킵 해도 무방하다는 것..
            return
        check.add((sa, sb, depth)) # 저장을 꼭 기준 숫자로만 해야 하는것이 아니라 결과값을 메모해도 좋은 결과가 있음

        if depth == len(info) - 1:
            #print(ret, sa, sb)
            minval = min(minval, sa)
            return
        # if sa + info[depth][0] < n:
        #     sol(depth+1, True, sa, sb)
        # if sb + info[depth][1] < m:
        #     sol(depth+1, False, sa, sb)
        sol(depth+1, True, sa, sb)
        sol(depth+1, False, sa, sb)
    sol(0, True, 0, 0)
    sol(0, False, 0, 0)
    return minval if minval != 987654321 else -1
