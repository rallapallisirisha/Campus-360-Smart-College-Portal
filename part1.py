# Find the smallest number in an array 
# def  smallest(arr):
#     small=arr[0]
#     for i in arr:
#         if i<small:
#             small=i
#     return small
# arr=[1,2,3,4,5,6]
# print(smallest(arr))

# Find the largest number in an array 
# def largest(arr):
#     large=arr[0]
#     for i in arr:
#         if i>large:
#             large=i
#     return large
# arr=[1,2,3,4,5,6]
# print(largest(arr))

# Second Smallest and Second Largest element in an array 
# def smallest(arr):
#     small=float('inf')
#     ssecond=float('inf')
#     for i in arr:
#         if i<=small:
#             ssecond=small
#             small=i
#         elif i>small and i<ssecond:
#             ssecond=i
#     return ssecond
# def largest(arr):
#     large=float('-inf')
#     lsecond=float('-inf')
#     for i in arr:
#         if i>large:
#             lsecond=large
#             large=i
#         elif i<large and i>lsecond:
#             lsecond=i
#     return lsecond
# arr=[1,2,3,4,5,6,7,8,9]
# print("Second smallest",smallest(arr))
# print("Second largest",largest(arr))

# Reverse a given array 
# def reverse(arr):
#     rev=[]
#     for i in range(len(arr)-1,-1,-1):
#         rev.append(arr[i])
#     return rev
# arr=[1,2,3,4,5]
# print(reverse(arr))

# Count frequency of each element in an array 
# def freq(arr):
#     count={}
#     for i in arr:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     return count
# arr=[1,1,2,2,3,3,4,4]
# print(freq(arr))

# Sum of ten numbers 
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

 # sum of first 10 even numbers 
# sum=0
# for i in range(2,11,2):
#     sum=sum+i
# print(sum)

# sum of even numbers between 20 and 30 
# sum=0
# for i in range(20,31,2):
#     sum=sum+i
# print(sum)

# sum of natural numbers 
# def natural(n):
#     if n==0:
#         return 0
#     rev=n*(n+1)//2
#     return(rev)
# print(natural(6))

# Rotate array by one left position 
# def rotate(arr):
#     k=int(input())
#     for j in range(k):
#         temp=arr[0]
#         for i in range(len(arr)-1):
#             arr[i]=arr[i+1]
#         arr[len(arr)-1]=temp
#     for i in arr:
#         print(i,end=" ")
# arr=[1,2,3,4,5]
# rotate(arr)

# rotate array by one right position 
# def rotate(arr):
#     n=len(arr)
#     k=int(input())
#     for j in range(k):
#         temp=arr[n-1]
#         for i in range(n-1,0,-1):
#             arr[i]=arr[i-1]
#         arr[0]=temp
#     for i in arr:
#         print(i,end=" ")
# arr=[1,2,3,4,5]
# rotate(arr)

# Reverse array in groups 
# def reverse(arr):
#     n=len(arr)
#     k=int(input())
#     for i in range(0,n,k):
#         left=i
#         right=min(i+k-1,n-1)
#         while left<right:
#             arr[left],arr[right]=arr[right],arr[left]
#             left+=1
#             right-=1
#     return arr
# arr=[1,2,3,4,5]
# print(reverse(arr))

# Sum of array 
# def sum(arr):
#     total=0
#     for i in range(len(arr)):
#         total=total+arr[i]
#     return total
# arr=[1,2,3,4]
# print(sum(arr))

# Alternates in array 
def alternate(arr):
    for i in range(len(arr)):
        return arr[::2]
arr=[1,2,3,4,5]
print(alternate(arr))
    








