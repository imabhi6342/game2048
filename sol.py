'''input='aaaabbbccddd'
output=''
char='a'
counter=0
for ch in input:
    if char!=ch:
        output=output+str(counter)+char
        char=ch
        counter=1 
        
    else:
        counter+=1
output=output+str(counter)+char
print(input)
print(output)   
print
a='harry'
print(a.replace('harry','john'))
print(a)
" tuple as a argument"

def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
        print(i)
    print(str(sum/len(numbers)))
    print(type(numbers))    

average(1,2,3,4,5,6,7
"dictonary as a argument"
def name(**name):
    print("my name is ",name["fname"],name["mname"],name["lname"] )
name( fname="abhishek",mname="kumar",lname="yadav")    
'lists'
l=[1,2,3,4,5]
m=[6,7,8]
l.extend(m)
print(m+l)
print(m)
print(l)

'tuple'
t=(0,1,2,3,4,1,2,3,1,2,3,1,2,3)
print(t.index(3)) 'gives the 1st index of occourance of 3'
print(t.index(3,4,5)) '''
'''slice the tuple from 4 index to 5 then gives the 1st occurance
 of 3 between the interval, if 3 is not present in the interval then gives an
 error stating that 'not in tuple' 

'KBC PROJECT'
questions=[1,2,3,4]
options=[['a','b','c','d'],['a','b','c','d'],['a','b','c','d'],['a','b','c','d']]
answers=['a','b','c','d']
prize=[10,100,1000,10000]
print('WELCOME TO THE KON BANEGA CROREPATI')
print('ENTER YOUR GOOD NAME')
name=input()
print('LETS START THE GAME,',name)
reward=0
for i in questions:
    print('QUESTION NUMBER',i,'IS ON YOUR SCREEN')
    print(questions[i-1])
    print('YOUR OPTIONS ARE:')
    print(options[i-1])
    answer=input('YOUR ANSWER IS OPTION:',)
    if answer.lower()==answers[i-1]:
        reward=reward+prize[i-1]
        print('CONGRATULATION !!! THE ANSWER IS CORRECT')
        print('YOU HAVE WON',reward,'AMOUNT !!! LETS MOVE ON TO THE NEXT QUESTION')
    else:
       print('SORRY YOUR ANSWER IS WRONG')
       break    
print('THANKYOU',name,'FOR PLAYING KON BANEGA CROREPATI WITH ME, YOU HAVE WON A WHOOPING AMOUNT OF',reward,'RS CONGRATULATIONS')
1,1,2,3,5,8,13,21,34,55,89,154,
a='cross lost and {} dog {}'
print(a.format('bark',1))'''

def rec(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return rec(n-1)+rec(n-2)

print(rec(2))


