
############################################################
# This program will derive and intergrate BASIC polynomials#
############################################################

#By: Linus Wright and Joe Conrad


#Declare all arrays
c=[]
n=[]
c1=[]
n1=[]
c2=[]
n2=[]
c3=[]
n3=[]
a=[]
a1=[]
a2=[]

#Declare global variables
answer=0				#Final answer
answer1=float(0)		#Answer, used in intergration
answer2=float(0)		#Also used in intergration
x=0						#Used in derivatives




#Define function for finding First Derivative

def derivative():
    for i in range(0,terms):
        c1.append(int(c[i])*int(n[i]))
        n1.append(int(n[i])-1)
    print('First Derivative:')
    for i in range(0,terms):
        print(int(c1[i]),'x^',int(n1[i]),end=' '),
        if i+1<terms:
            print('+',end=' ')
    print('')


	
#Define function for finding Second Derivative
	
def derivative2():
    for i in range(0,terms):
        c2.append(int(c1[i])*int(n1[i]))
        n2.append(int(n1[i])-1)
    print('Second Derivative:')
    for i in range(0,terms):
        print(int(c2[i]),'x^',int(n2[i]),end=' '),
        if i+1<terms:
            print('+',end=' ')
    print('')

	
#Define function for finding Intergral
def integrate():
    for i in range(0,terms):
        c3.append(float(c[i])/(float(n[i])+1))
        n3.append(int(n[i])+1)
    print('Integral:')
    for i in range(0,terms):
            print(float(c3[i]),'x^',int(n3[i]),end=' ')
            if i+1<terms:
                print('+',end=' ')
    print('')


	
#########################################################	

	
#Inputs

print('Enter number of terms.')
terms = int(input())

for i in range(0,terms):
    print('Enter coefficient of term '+ str(i+1)+'.')
    c.append(input())
    print('Enter power of term '+ str(i+1)+'.')
    n.append(input())
print('Enter derivative number (1,2) or integral (3).')
D = int(input())
if D == 3:
    print('Enter 2 values of x. If none, press enter.')
    global x1,x2
    x1 = input()
    x2 = input()
else:
    print('Enter value of x. If none, press enter.')
    global x
    x = input()



#Calls functions
    
if D==1:
    derivative()
if D==2:
    derivative()
    derivative2()
if D==3:
    integrate()

	
	
	
#Derivative at a point

if D != 3:
    if x != None:
        for i in range(0,terms):

            if D == 1:
                a.append(int(c1[i]) * float(x) ** int(n1[i]))
                answer=a[i]+answer
            elif D==2:
                a.append(int(c2[i]) * float(x) ** int(n2[i]))                    
                answer=a[i]+answer
        print(answer)

		
		
#Intergral at a point
		
if D == 3:
    for i in range(0,terms):
        a1.append(float(c3[i]) * float(x1) ** int(n3[i]))
        a2.append(float(c3[i]) * float(x2) ** int(n3[i]))
    for i in range(0,terms):
        answer1=float(a1[i])+answer1
        answer2=float(a2[i])+answer2
    answer= answer1-answer2
        
    
    print(answer)


