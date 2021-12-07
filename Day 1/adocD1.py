# Read file
# Convert file text to array
# Create counter
# Loop through Array
# Increase counter if next is higher than previous
# return counter value in the end

with open('adocD1.txt') as file:
    nums = file.readlines()

counts = 0
i=0

# Part One
# while i < len(nums)-1:
#     if int(nums[i+1]) > int(nums[i]):
#         counts += 1
#     i+=1

# Part Two
while i < len(nums)-:
    curr = int(nums[i])+int(nums[i+1])+int(nums[i+2])
    nex = int(nums[i+1])+int(nums[i+2])+int(nums[i+3])
    if nex > curr:
        counts+=1
    i+=1

print(counts)