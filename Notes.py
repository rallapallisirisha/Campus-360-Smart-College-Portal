# 28/08/2026 
# def sumofNumbers(a,b):
#     sum=a+b
#     return sum
# ans=sumofNumbers(2,3)
# print(ans)

# Leetcode 412 
# n=int(input())
# ans=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         ans.append("FizzBuzz")
#     elif i%3==0:
#         ans.append("Fizz")
#     elif i%5==0:
#         ans.append("Buzz")
#     else:
#         ans.append(str(i))
# print(ans)

# Leetcode 1523 
# Count odd numbers in a range 
# low=int(input())
# high=int(input())
# print((high+1)//2 - low//2)

# Leetcode 1365 
# How many numbers are smaller than current number 
# n=list(map(int,input().split()))
# ans=[]
# for i in n:
#     c=0
#     for j in n:
#         if j<i:
#             c+=1
#     ans.append(c)
# print(ans)

# Leetcode 2520 
# count the digits that divide a number 
# n=int(input())
# original=n
# count=0
# while n>0:
#     digit=n%10
#     if digit!=0 and original%digit==0:
#         count+=1
#     n=n//10
# print(count)

# Leetcode 9 
# Palindrome 
# n=int(input())
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Leetcode 1281 
# Subtract the product and sum of digits of an integer 
# n=int(input())
# pro=1
# sum=0
# while n>0:
#     digit=n%10 
#     sum+=digit
#     pro*=digit
#     n=n//10
# print(pro-sum)

# Leetcode 1431 
# Kids with the greates number of candies 
# excandies=int(input())
# candies=list(map(int,input().split()))
# maxcandies=max(candies)
# ans=[]
# for i in candies:
#     if i+excandies>=maxcandies:
#         ans.append(True)
#     else:
#         ans.append(False)
# print(ans)

# 30/08/2026 
# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
# fun(3)

# Leetcode 509 
# Fibonacci series 
# def fun(n):
#     if n==0 or n==1:
#         return n
#     return fun(n-1)+fun(n-2)
# print(fun(3))

# Leetcode 1137 
# Nth tribonacci number 
# def fun(n):
#     if n==0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     return fun(n-1)+fun(n-2)+fun(n-3)
# print(fun(4))

# def fun(n):
#     if n==0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     a=0
#     b=1
#     c=1
#     for i in range(3,n+1):
#         a,b,c=b,c,a+b+c
#     return c
# print(fun(4))

# Leetcode 231 
# Power of two 
# def fun(n):
#     if n<=0:
#         return False
#     if n==1:
#         return True
#     if n%2!=0:
#         return False
#     return fun(n//2)
# print(fun(8))

# Leetcode 326 
# Power of Three 
# def fun(n):
#     if n<=0:
#         return False
#     if n==1:
#         return True
#     if n%3!=0:
#         return False
#     return fun(n//3)
# print(fun(27))

# Leetcode 1480 
# Running sum of 1D array 
# def fun(nums):
#     for i in range(1,len(nums)):
#         nums[i]=nums[i]+nums[i-1]
#     print(nums)
# fun([1,2,3,4])

# Leetcode 1672 
# Richest customer wealth 
# def fun(n):
#     ans=[]
#     for sublist in n:
#         ans.append(sum(sublist))
#     return max(ans)
# print(fun([[1,2,3],[3,2,1]]))

# Leetcode 1470 
# Shuffle the array 

# GCD and LCM 
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# def lcm(a,b):
#     return a*b//gcd(a,b)
# print(gcd(15,50))
# print(lcm(15,50))

# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# def lcm(a,b):
#     return a*b//gcd(a,b)
# a=15
# b=50
# c=25
# g=gcd(gcd(a,b),c)
# l=lcm(lcm(a,b),c)
# print("GCD",g)
# print("LCM",l)

# Leetcode 50 
# power(x,n) 
# def power(x,n):
#     return(x**n)
# print(power(2,5))

# Leetcode 26 
# Remove duplicates from sorted array 
# def sorted(arr):
#     count=[]
#     for i in range(len(arr)):
#         if i==0 or arr[i]!=arr[i-1]:
#             count.append(arr[i])
#     for i in range(len(count)):
#         arr[i]=count[i]
#     return len(count)
# print(sorted([1,1,2,2,3,3]))

# Leetcode 26 
# def dup(arr):
#     n=len(arr)
#     start=0
#     for i in range(1,n):
#         if arr[i]!=arr[start]:
#             start+=1
#             arr[start]=arr[i]
#     return start+1
# arr=[1,1,2]
# print(dup(arr))

# Leetcode 80 
# Remove duplicate elements in sorted array 
# def dup(arr):
#     n=len(arr)
#     start=1
#     if n<=2:
#         return n
#     for i in range(2,n):
#         if arr[i]!=arr[start-1]:
#             start+=1
#             arr[start]=arr[i]
#     return start+1
# arr=[1,1,1,2,2,2]
# print(dup(arr))


        












        


