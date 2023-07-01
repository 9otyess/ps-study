#1931 회의실 배정

# 한 개의 회의실과 이를 사용하고자 하는 n개의 회의, 회의실 사용표
# 각 회의 i에 대해 시작시간과 끝나는 시간이 주어짐
# 회의가 겹치지 않게 하는 회의의 최대 개수
# 끝남과 동시에 다음 회의 시작 가능, 시작과 동시에 끝남 가능

# 해결
# 

n = int(input())
con_li=[]
for i in range(n):
    start, end=map(int,input().split())
    con_li.append([start,end])