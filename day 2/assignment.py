bmi=84/1.65**2
print(bmi)
# this gives long floating points so we can solve that by gives 30.844124123424
print(int(bmi))
#changing result to int first and printing gives 30
#but we dont need that instead we can use round to round off values like 

print(round(bmi))
# this gives rounded off value to 31 also

print(round(bmi,2))
#this gives value upto two decimal places this is used when accuracy is important
#gives 30.84

#assignment operators
score=1
score +=1
print(score)  #gives 2

score=1
score -=1
print(score)     #gives 0

score=1
score *=1
print(score)     #gives 1

score=1
score /=1
print(score)     #gives 1.0


