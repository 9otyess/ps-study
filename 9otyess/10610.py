#10610 30

# 길거리에서 찾은 수 양수 N을 입력하고
# 숫자 N의 숫자들을 조합하여
# 30의 배수가 되는 가장 큰 수를 만들자
# 존재하지 않는다면 -1을 출력

# 해결
# 입력받은 수를 리스트로 쪼개고 큰수부터 정렬
# 30으로 나누어 떨어지려면 일의 자리수는 0이어야하고
# 모든 자리 수의 합이 3의 배수여야함 
# 0이 존재하지 않거나, 모든 자리 수의 합이 3의배수가 아니라면 -1 출력

n =list(input())
n.sort(reverse=True)

res=0
n_sum=0
for i in range(len(n)):
    n_sum+=int(n[i])

if '0' not in n or n_sum%3!=0:
    res=-1
else:
    res="".join(n)
print(res)