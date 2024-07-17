infix = [] #?
operaters = []
postfix = []
notint = ['+','-','*','^','/','(',')']
for t in range(len(infix)):
    if infix[t] not in notint:
        postfix.append(infix[t])
    else:
        while len(operaters)>0 and infix[t]!='(' and infix[t]<operaters[-1]:
            postfix.append(operaters[-1])
            operaters = operaters[:-1]
        operaters.append(infix[t])
    if infix[t] =='(':
        operaters.append(infix[t])
    if infix[t] ==')':
        while operaters[-1]!='(':
            postfix.append(operaters[-1])
            operaters = operaters[:-1]
        operaters.pop('(')
while len(operaters)!=0:
    postfix.append(operaters[-1])
    operaters = operaters[:-1]

print(postfix)

