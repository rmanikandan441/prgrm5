
n=int(input("Enter any number: "))
S=list(map(int,str(n)))
T=list(map(lambda x:x**3,S))
if(sum(T)==n):
    print("The number is an armstrong number. ")
else:
    print("The number is not an arsmtrong number. ")
