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
        if (sa, sb, depth) in check:
            return

        check.add((sa, sb, depth))
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
