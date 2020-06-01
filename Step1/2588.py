num1=input("")
num2=input("")
sum1=0
result=0
for i in range(2,-1,-1):
    for j in range(0,3):
        sum1+=(int(num1[j])*(10**(2-j)))*(int(num2[i])*(10**(2-i)))
    result+=sum1
    print(int(sum1/(10**(2-i))))
    sum1=0
print(result)
