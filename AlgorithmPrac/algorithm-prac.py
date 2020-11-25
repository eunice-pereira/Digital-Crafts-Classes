# 1. Given an array nums, write a function to move all zeroes to the end of it 
# while maintaining the relative order of the non-zero elements.
arr = [1, 5, 0, 6, 8, 0, 9, 3, 2]

def push_zeros(arr):
    arr2 = [] 
    for i in arr:  
        if i != 0: 
            arr2.append(i)
            i += 1

#     print(arr2)
    

# push_zeros(arr)

# 2. Write a function that counts the number of times the number 7 occurs in a given integer
# without converting it to a string.
# For example the number 7,704,793 would output 3

num = 7,704,793
def seven_count(num): 
    count = 0 
    n = abs(num)
    while n > 0: 
        rem = n % 10 # checking if number is 7
        if rem == 7: 
            count += 1 
        n = (n - rem)/10 # removing number from count and retaining 
    return count
print(seven_count(num))

    
# 3. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Examples and clarification here: https://leetcode.com/problems/two-sum/
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Because nums[0] + nums[1] == 9, we return [0, 1].

