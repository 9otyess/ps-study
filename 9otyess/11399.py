#11399 ATM

# 1대의 ATM기, N명의 사람들(번호매김)
# 돈을 인출하는 데 필요한 시간을 입력 받고,
# 이를 작은 값부터 차례로 다시 줄 세움
# 1번 주자부터 ,, n번 주자까지 각자 걸리는 시간을 각각 구해
# 이를 모두 더한 값을 출력

n=int(input())
time=list(map(int,input().split()))
time.sort()

sum_li=[]
res=0
result=0
for i in range(n):
    for k in range(i+1):
        res+=time[k]
print(res)