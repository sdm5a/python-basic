# #  write a proagram to print the following pattern
# n=int(input("Enter number of rows: "))
# for i in range(1,n+1):               #*
#     for j in range(1,i+1):           #**
#         print("* ", end="")          #***
#     print()                          #****
    
# '''*****
#    ****
#    ***
#    **
#    *'''
# m=int(input("Enter number of rows: "))
# for i in range(n):
#     for j in range(m-i):
#         print("* ", end="")
#     print()    
    
# '''*
#    **
#    ***
#    ****
#    *****
#    ****
#    ***
#    **
#    *'''    
# k=int(input("Enter the number of rows : "))
# for i in range(1,k+1):               
#     for j in range(1,i+1):           
#         print("* ", end="")          
#     print()                          
# for i in range(k):
#     for j in range(k-i):
#         print("* ", end="")
#     print()        
    
# '''****
#    ****
#    ****
#    ****'''  
# l=int(input("Enter the number of rows : "))            
# for i in range(1,l+1):
#     for j in range(1,l+1):
#         print("* ", end="")
#     print()    
    
'''
* * * * *
*       *
*       *
*       *
* * * * *'''    
# a=int(input("Enter the number of rows :"))    
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if i==1 or j==1 or i==a or j==a:
#             print("* ", end="")
#         else:
#             print("  ", end="")    
#     print()    
 
'''
* * * * *
* *     *
*   *   *
*     * *
* * * * *'''        
        
# b=int(input("Enter the number of rows :"))    
# for i in range(1,b+1):
#     for j in range(1,b+1):
#         if i==1 or j==1 or i==b or j==b or i==j:
#             print("* ", end="")
#         else:
#             print("  ", end="")    
#     print()    
            
'''            
* 
* * 
*   * 
*     * 
* * * * * '''            
# c=int(input("Enter number of rows: "))
# for i in range(1,c+1):               
#     for j in range(1,i+1):           
#         if i==1 or j==i or j==1 or i==c :
#            print("* ", end="") 
#         else:
#             print("  ",end="")          
#     print()                

'''
* * * * *
*     *
*   *
* *
* '''
# d=int(input("Enter number of rows: "))
# for i in range(d):
#     for j in range(d-i):
#         if i==0 or j==0  or j==d-(1+i): 
#             print("* ", end="")
#         else:
#             print("  ",end="")
#     print()   
 
     
e=int(input("Enter the number of rows: "))    
            