# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    if len(l) == 1:
        return l[0]
    
    else:
        largest = find_max(l[1:])
        if largest > l[0]:
            return largest
        else:
            return l[0]

print(find_max([1000, 4, 45, 6, -50, 10, 2,100]))
# => 45