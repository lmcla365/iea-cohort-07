lab_list=[ 1, 2, 3, 4, 5, 6 ]
length=len(lab_list)
   
first_half = lab_list[:len(lab_list)//2]
second_half = lab_list[len(lab_list)//2:]
reverse = second_half,first_half

if len(first_half) == len(second_half):
    middle = first_half[-1],second_half[1]
else:
    middle = first_half[-1]

print(second_half,first_half)
print(middle)
