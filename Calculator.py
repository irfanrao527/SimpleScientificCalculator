#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:



while(True):
    print("Choose the math operation \n\n0 - Addition\n1 - Substraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n ")

    oper = input("\nChoose the option from the menue: ")
    
    ###-----Addition
    
    if oper == "0":
            val1 = float(input("\nFirst value:"))
            val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(val1 + val2)+ "\n")
    
            back = input('\n Go back to the main menue ? (y/n)')
            
            if back == 'y':
                continue
            else:
                break
    
    ##- Substration 
    elif oper == "1":
            val1 = float(input("\nFirst value:"))
            val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(val1 - val2)+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break
    
    ##- Multiplication 
    elif oper == "2":
            val1 = float(input("\nFirst value:"))
            val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(val1 * val2)+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break
                
    ##- Division 
    elif oper == "3":
            val1 = float(input("\nFirst value:"))
            val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(val1 / val2)+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break 
        
        
    ##- Modulo 
    elif oper == "4":
            val1 = float(input("\nFirst value:"))
            val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(val1 % val2)+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break 
                
                
    ##- Raising to a power 
    elif oper == "5":
            val1 = float(input("\nFirst value:"))
            val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(math.pow(val1,val2))+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break         
                
    
    
    ##- Squar root 
    elif oper == "6":
            val1 = float(input("\nEnter the value for the squar root:"))
            #val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(math.sqrt(val1))+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break  
                
    ##- Log 
    elif oper == "7":
            val1 = float(input("\nEnter the value for the Logarithum (with base 2):"))
            #val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(math.log(val1,2))+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break            
                
                
    ##- Sine 
    elif oper == "8":
            val1 = float(input("\nEnter the value (in degree) to calculate the sine:"))
            #val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(math.sin(math.radians(val1)))+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break     
                  
    ##- Cos 
    elif oper == "9":
            val1 = float(input("\nEnter the value (in degree) to calculate the cosine:"))
            #val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(math.cos(math.radians(val1)))+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break  
                
                    
    ##- Tangent 
    elif oper == "10":
            val1 = float(input("\nEnter the value (in degree) to calculate the tangent:"))
            #val2 = float(input("\nSecond value:"))
        
            print("\n The result is:" + str(math.tan(math.radians(val1)))+ "\n")
    
            back = input("\n Go back to the main menue ? (y/n)")
            
            if back == 'y':
                continue
            else:
                break   
                
    else:
        print("\nInvalid option!\n")
        print("Please enter a valid opetion from 0 to 10\n\n")
        continue
        
                
        
        


# In[4]:





# In[ ]:





# In[ ]:





# In[ ]:




