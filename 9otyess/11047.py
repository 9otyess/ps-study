#11047
# 준규가 가지고 있는 동전은 총 n종류
# 동전을 적절히 사용하여 그 가치의 합을 k로 만들려함
# 이때 필요한 동전 개수의 최솟값 출력하기
# 첫째줄에 n k 입력
# 둘째 줄부터 n개의 줄에 동전의 가치가 오름차순으로 주어짐
# 해결
#1) 동전의 가치들은 리스트로 받고
#2) 큰 가치의 동전부터 가치의 합에서 빼줌
n,k=map(int,input().split())
won_list=[]
for i in range(n):
    won=int(input())
    won_list.append(won)
won_list.sort(reverse=True)
result=0
for i in won_list:
    result+=k//i
    k%=i
print(result)
