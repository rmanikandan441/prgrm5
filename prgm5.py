numa = 12
numb = 17
numc = 33



if (numa >= numb) and (numa >= numc):
   largest = numa
elif (numb >= numa) and (numb >= numc):
   largest = numb
else:
   largest = numc

print("The largest number between",numa,",",numb,"and",numc,"is",largest)

