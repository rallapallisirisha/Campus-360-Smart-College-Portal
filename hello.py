# print("Hello world") 
# mice=list(map(int,input().split()))
# holes=list(map(int,input().split()))
# mice.sort()
# holes.sort()
# print(mice)
# print(holes)

# def sort_list(mice,holes):
#     for i in range(len(mice)):
#         for j in range(i+1,len(mice)):
#             if mice[i]>mice[j]:
#                 mice[i],mice[j]=mice[j],mice[i]
#     for i in range(len(holes)):
#         for j in range(i+1,len(holes)):
#             if holes[i]>holes[j]:
#                 holes[i],holes[j]=holes[j],holes[i]
#     return(mice,holes)
# list1=[5,4,7,9,1]
# list2=[6,8,1,3,4]
# print(sort_list(list1,list2))

# Count strings repeated in word 
# word="siri"
# count={}
# for ch in word:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# for ch in count:
#     print(ch,count[ch])

# leetcode 242 
# def anagram(s,t):
#     if len(s)!=len(t):
#         return False
#     count={}
#     for ch in s:
#         if ch in count:
#             count[ch]+=1
#         else:
#             count[ch]=1
#     for ch in t:
#         if ch in count:
#             count[ch]-=1
#         else:
#             return False
#     for ch in count:
#         if count[ch]!=0:
#             return False
#     return True
# s = input()
# t = input()
# print(anagram(s, t))

# leetcode 283 
# Move zeros 
# def movezeros(nums):
#     j=0
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[j],nums[i]=nums[i],nums[j]
#             j+=1
#     return nums
# nums=list(map(int,input().split()))
# print(movezeros(nums))

# leetcode 66 
# Plus one 
# nums=[1,2,3]
# num=0
# for i in nums:
#     num=num*10+i
# num+=1
# nums=list(map(int,str(num)))
# print(nums)

# Leetcode 1 
# Two sum 
# n=[1,2,3,4]
# target=3
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]+n[j]==target:
#             print(i,j)

# leetcode 217 
# Contains duplicate 
# n=[1,2,3,1]
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]==n[j]:
#             print(True)
#             break

# def duplicate(nums):
#     seen=set()
#     for i in nums:
#         if i in seen:
#             return True 
#         seen.add(i)
#     return False 
# nums=[1,2,3,1]
# print(duplicate(nums))

# Leetcode 121 
# Best time to buy and sell stock 
# def best(prices):
#     minimum=prices[0]
#     maximum=0
#     for price in prices:
#         if price<minimum:
#             minimum=price
#         profit=price-minimum
#         if profit>maximum:
#             maximum=profit
#     return maximum
# prices=list(map(int,input().split()))
# print(best(prices))













