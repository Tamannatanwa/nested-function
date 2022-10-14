print("WELCOME TO KBC")
name=input("enter your name:")
question=["1.who is the founder of facebook"," 2.what is the  capital of india?","3.ng mei koaun se course padhaya jaata hai?"]
option=[["1.mark zuckerberg","2.bill gates","3.steve jobs","4.larry page"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software engineering","2.counseling","3.torium","4.agriculture"]]
price=[" YOU ARE WON 1000RUPEES, CONGREATULATION","WOW!,NICE,GREAT ANSWER","AWESOME ,YOU ARE WINNER KBC GAME"]
solu=[1,4,1]
life_line=[["1.mark zuckerberg","2.stev jobs"],["1.bhopal","2.delhi"],["1.softeware engineering","2.counseling"]]
life_solution=[1,2,1]
i=0
count=0
def hint(i):
    global count
    if count==0:
        count+=1
        k=0
        while k<len(life_line[i]):
            print(life_line[i][k])
            k=k+1
        choice=int(input("enter the choice"))
        if choice==life_solution[i]:
            return True
        else:
            return False
                
    else:
        print("already used lifeline")
        choice=int(input("enter your choice...."))
        if choice==solu[i]:
            return True
        else:
            return False
def solution(i):
    print("1.with lifeline")
    print("2.without lifeline")
    choice=int(input("enter your choose..."))
    if choice==1:
        return hint(i)
    else:
        option[i]
        choose=int(input("enter your choice..."))
        if choose==solu[i]:
            return True
        else:
            return False
def ques():
    i=0
    while i<len(question):
        print(question[i])
        j=0
        while j<len(option[i]):
            print(option[i][j])
            j=j+1
        a=solution(i)
        if a==False:
            print("wrong answer")
            break
        elif a==True:
            print("congrats",price[i])
            
        i=i+1
ques()
