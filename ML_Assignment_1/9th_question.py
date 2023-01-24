#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
#kilograms in a separate list using Loop. N: No of students (Read input from user)
#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]
Lbs=[]
Lbs=list(map(int,input().split()))
weight=[]
for i in Lbs:
    weight.append(round(i*0.453592,2))
print(weight)
