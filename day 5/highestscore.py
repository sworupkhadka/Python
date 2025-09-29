students_score=[100,50,100,120]

#sum is used to give sum of values in the array 
total_score=sum(students_score)
print(total_score)


#  using loop it can also can be done as using loop by
sum=0
for score in students_score:
    sum += score
print(sum)



#returns max value in the array
print(max(students_score))


#using loop to get max value we can also do it as
max_score=0
for score in students_score:
    if score>max_score :
        max_score=score
print(max_score)

