import time
print ("Hello, solve your quadratic equation here.")

import cmath
print ("Select what to solve--")
print ("1. Quadratic equation with real coeff.")
print ("2. Quadratic equation with Compex coeff.")
choice= input('Enter your choice:')

if choice =='1':
 a= float(input('Enter leading coeff.='))
 if a==0:
     print("\033[1;31;40,m Error: Leading coeff. cannot be zero. \033[0")
 else:
     b= float(input('Enter coeff. of x='))
     c= float(input('Enter constant ='))
     def quadratic_eqn (a, b, c):
      """
      Args:
      a: coefficient of x^2 term.
      b: coefficient of x term.
      c: constant term.
    """
      start= time.time()
      D = b**2 - 4*a*c
      root1 = (-b+cmath.sqrt(D))/(2*a)
      root2 = (-b-cmath.sqrt(D))/(2*a)
      print("The discriminant is:", round(D, 3))
      print('The equation is:')
      print (f" {a}x^2 + {b}x +{c}=0")
      print("The roots are:",root1,root2)
      elapsed= (time.time()-start)*1000
      print("Executed in:", elapsed, "ms")
 print(quadratic_eqn(a,b,c))

elif choice== "2":
   a= float(input('Entyer real part of the leading coeff.:'))
   b= float(input('Enter imaginary part of the leading coeff.:'))
   A= complex(a,b)

   if A==0:
      print("Error: Leading coeff. cannot be zero.")
   
   else:
      c= float(input('enter real part of coeff. of x:'))
      d= float(input('Enter im. part of the coeff. of x:'))
      B= complex (c,d)

      e= float(input('Enter re. part of constant term:'))
      f= float(input('Enter im. part of constant term:'))
      C= complex(e,f)
      
      def quadratic_eqn(A,B,C):
       """
      Args:
      A: coefficient of x^2 term.
      B: coefficient of x term.
      C: constant term.
    """
      start= time.time()
      D= B**2-4*A*C

      root1= -B+ cmath.sqrt(D)
      root2= -B+ cmath.sqrt(D)

      print("The discriminant is:",D)     
      print('The equation is:')
      print (f" {A}x^2 + {B}x +{C}=0")
      print("The roots are:", root1, root2)
      elapsed= (time.time()-start)*1000
      print("Executed in:", elapsed, "ms")
      print(quadratic_eqn(A,B,C))

else:
   print("Invalid input, please try again.")

            
   
     
 
