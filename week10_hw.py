def crossed(x1,r1,x2,r2):
    right1 = x1+r1
    # left1 = x1-r1

    # right2 = x2+r2
    left2 = x2-r2
    if right1>left2:
        return True
    # for i in range(left1,right1+1):
    #     for j in range(left2,right2+1):
    #         if i==j:
    #             return True
    return False
def how_many_crossed(l = [1,5,2,1,4,0]):
    cnt = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if crossed(i,l[i],j,l[j]):
                print(i,l[i],j,l[j])
                cnt+=1
                if cnt>10**7:
                    return -1
    return cnt
how_many_crossed()
# print(crossed(0,1,2,1))

def max_space(n):
    n_bin = ''
    while n>0:
        n_bin = str(n%2)+n_bin
        n//=2
    max = 0
    cnt = 0
    flag = False
    print(n_bin)
    for i in n_bin:
        if flag and i=='0':
            cnt+=1
        elif flag and i=='1':
            if max<cnt:
                max = cnt
            cnt = 0
            flag = False
        if not flag and i=='1':
            flag = True

    return max

def task2(a):
    #��������� � ������ ������ O(10^9)
    max = -10**9
    for i in a:
        if i>max:
            max = i
    indexes = []
    for i in range(max):
        indexes.append(False)
    for i in range(len(a)):
        indexes[a[i]-1] = not indexes[a[i]-1]
    for i in indexes:
        if i:
            print(a[i])
            break
def solution(A, B):
    cnt = 0
    st = []
    live = []
    for i in range(len(B)):
        if not B[i]: # 0
            if len(st) == 0:
                # print("first")
                live.append(i)
                # print(live, st)
            else:
                # print("second")
                while len(st):
                    if A[st[-1]]<A[i]:
                        st.pop()
                    else:
                        break
                if len(st) == 0:
                    live.append(i)
                # print(live, st)
        else:
            # print("third")
            st.append(i)
            # print(live, st)
    live += st
    return len(live)


# a = [4,3,2,1,5]
# b = [0,1,0,0,0]
# print(solution(a, b))
# a = [1,3,1,2,2]
# task2(a)
# print(max_space(5))
