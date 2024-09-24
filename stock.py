'''
1) u have to ask which type of user is using the machine 
 1) user/ emp (type 1)  2) admin (type 2)
================================================   for  1) user/ emp =======
stock = [] -> 12 items / products 

srno  product      qty     price     gst      tax  brand 

user input : details : 
stock =: 
features L: 2 ) 
 u needs 
 3) bill calculate 
 to fetch the stock updation based on the types of user
 ========================================  for admin =======================
 stock display : 
 use => (modular programming )
stock-qty-userqty



 
 
'''
print()
print("****************************************** :) WELCOME TO THE ARMY GARMENTS :) **************************************")

stock=[1,   'Shirts',       'Adidas',         100,    3000,   12 ,  
       2,   'Sweatshirts',  'H&M',            100,    4000,   12 ,    
       3,   'Pants',        'Nike',           100,    3500,   12 ,    
       4,   'Shirts',       'Adidas',         100,    3000,   12 ,    
       5,   'Pants',        'Nike',           100,    3500,   12 ,    
       6,   'Sweatshirts',  'H&M',            100,    4000,   12 ,    
       7,   'Jeans',        'Calvin Klein',   100,    5000,   12 ,    
       8,   'Sweatshirts',  'H&M',            100,    4000,   12 ,    
       9,   'Pants',        'Nike',           100,    3500,   12 ,    
       10,  'Jeans',        'Calvin Klein',   100,    5000,   12 ,    
       11,  'Jeans',        'Calvin Klein',   100,    5000,   12 ,   
       12,  'Shirts',       'Adidas',         100,    3000,   12 ,      ]



def updation(qty_value1, qty_value2 , qty_value3, qty_value4, user_input1, user_input2 ,user_input3 ,user_input4):
    qty_value1['qty'] -= user_input1['qty']
    qty_value2['qty'] -= user_input2['qty']
    qty_value3['qty'] -= user_input3['qty']
    qty_value4['qty'] -= user_input4['qty']
        #   print(qty_value)
        # qty_value=stock
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ USER FUNCTIONS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Payment method  
def payment_method(choose):
    if choose == 'yes':
        print("You chose to pay with Card")
        
    else:
        print("You chose to pay with Cash") 
         
# Bill Calculation
def bill_calculate(total_price):
    gst=total*12/100
    total_price=total+gst
    print(f"Total bill: {total_price}")  
    
 
    
    
###################################################### Driver code#############################################################################

print()
print("First we have to identify who you are ?")
print()
print("Please Enter 1 for user and 2 for admin")
print()
role=int(input("Please Enter your answer : "))
if role == 1:
        print("Access granted User")
        print()
        print("****************************************** :) WELCOME USER  :) ********************************************** ")  
        print()      
        print("-----------------------------------------------------------------------")
        print("Sr No. |   Product       |       Brand       |  Qty |  Price  | GST    ")
        print("-----------------------------------------------------------------------")
        print("  1    |   'Shirts'      |  'Adidas'         | 100  |  3000   |  12    ")
        print("  2    |   'Sweatshirts' |  'H&M'            | 100  |  4000   |  12    ")
        print("  3    |   'Pants'       |  'Nike'           | 100  |  3500   |  12    ")
        print("  4    |   'Shirts'      |  'Adidas'         | 100  |  3000   |  12    ")
        print("  5    |   'Pants'       |  'Nike'           | 100  |  3500   |  12    ")
        print("  6    |   'Sweatshirts' |  'H&M'            | 100  |  4000   |  12    ")
        print("  7    |   'Jeans'       |  'Calvin Klein'   | 100  |  5000   |  12    ")
        print("  8    |   'Sweatshirts  |  'H&M'            | 100  |  4000   |  12    ")
        print("  9    |   'Pants'       |  'Nike'           | 100  |  3500   |  12    ")
        print("  10   |   'Jeans'       |  'Calvin Klein'   | 100  |  5000   |  12    ")
        print("  11   |   'Jeans'       |  'Calvin Klein'   | 100  |  3000   |  12    ")
        print("  12   |   'Shirts'      |  'Adidas'         | 100  |  3000   |  12    ")
        print("-----------------------------------------------------------------------")
        print()
        key_value={'shirts':3000,
           'sweatshirts':4000,
           'pants':3500,
           'jeans':5000}

        user_input = input("Would you like to buy something ? (Yes or No) ")
        print() 
        while(user_input=='yes'): 
            customer_input=input("So what would you like buy ? ")
            if (customer_input in key_value):
                user_qty=int(input("What quantity you would like to purchase : "))
                print()
                total=user_qty*key_value[customer_input]   
            else:
                print("Invalid input")
            user_input=input("Would you like to continue shopping (Yes or No) ? ")    
                        
        print()
        bill_calculate(total_price=0) 
        print() 
          
        choose=input("Would you like to pay with Card (Yes or No) : ")
        print()
        
        payment_method(choose)    
        print()
        print("Thank You . Please visit again .")
        
        
        
        
#--------------------------------------------------- for admin---------------------------------------------------------------- 
elif role == 2:
        password='admin89'
        print()
        cpassword=input("Please confirm your Password : ")
        print()
        if password == cpassword:
            print("Access granted Admin ")
            print()
            print("****************************************** :) WELCOME ADMIN  :) ********************************************** ")
            print()
            print("-----------------------------------------------------------------------")
            print("Sr No. |   Product       |       Brand       |  Qty |  Price  | GST    ")
            print("-----------------------------------------------------------------------")
            print("  1    |   'Shirts'      |  'Adidas'         | 100  |  3000   |  12    ")
            print("  2    |   'Sweatshirts' |  'H&M'            | 100  |  4000   |  12    ")
            print("  3    |   'Pants'       |  'Nike'           | 100  |  3500   |  12    ")
            print("  4    |   'Shirts'      |  'Adidas'         | 100  |  3000   |  12    ")
            print("  5    |   'Pants'       |  'Nike'           | 100  |  3500   |  12    ")
            print("  6    |   'Sweatshirts' |  'H&M'            | 100  |  4000   |  12    ")
            print("  7    |   'Jeans'       |  'Calvin Klein'   | 100  |  5000   |  12    ")
            print("  8    |   'Sweatshirts  |  'H&M'            | 100  |  4000   |  12    ")
            print("  9    |   'Pants'       |  'Nike'           | 100  |  3500   |  12    ")
            print("  10   |   'Jeans'       |  'Calvin Klein'   | 100  |  5000   |  12    ")
            print("  11   |   'Jeans'       |  'Calvin Klein'   | 100  |  3000   |  12    ")
            print("  12   |   'Shirts'      |  'Adidas'         | 100  |  3000   |  12    ")
            print("-----------------------------------------------------------------------")
            print()
            
            qty_value1 = {'product': 'shirts',            'qty': 100}  
            qty_value2 = {'product': 'pants',             'qty': 100} 
            qty_value3 = {'product': 'sweatshirts',       'qty': 100} 
            qty_value4 = {'product': 'jeans',             'qty': 100} 
            
            user_input1 = {'product': 'shirts',       'qty': 10 }          
            user_input2 = {'product': 'pants',        'qty': 40 }  
            user_input3 = {'product': 'sweatshirts',  'qty': 20 }  
            user_input4 = {'product': 'jeans',        'qty': 60 }  
            
            updation(qty_value1 ,qty_value2 ,qty_value3 ,qty_value4 ,user_input1 ,user_input2 ,user_input3 ,user_input4)
            print("Updated stock ")
            print(qty_value1)
            print(qty_value2)
            print(qty_value3)
            print(qty_value4)
            # for qty_value in stock:
            # qty_value=stock
            # print(stock) 
                      
        else:
            print("Sorry! Wrong passowrd  ")
            
else:
    print("Invalid User ")
print()


         

# stock1={'srno.':1,  'product':'Shirts',       'brand':'Adidas',         'qty':100,    'price':3000,   'gst':12 ,  
#        'srno.':2,   'product':'Sweatshirts',  'brand':'H&M',            'qty':100,    'price':4000,   'gst':12 ,    
#        'srno.':3,   'product':'Pants',        'brand':'Nike',           'qty':100,    'price':3500,   'gst':12 ,    
#        'srno.':4,   'product':'Shirts',       'brand':'Adidas',         'qty':100,    'price':3000,   'gst':12 ,    
#        'srno.':5,   'product':'Pants',        'brand':'Nike',           'qty':100,    'price':3500,   'gst':12 ,    
#        'srno.':6,   'product':'Sweatshirts',  'brand':'H&M',            'qty':100,    'price':4000,   'gst':12 ,    
#        'srno.':7,   'product':'Jeans',        'brand':'Calvin Klein',   'qty':100,    'price':5000,   'gst':12 ,    
#        'srno.':8,   'product':'Sweatshirts',  'brand':'H&M',            'qty':100,    'price':4000,   'gst':12 ,    
#        'srno.':9,   'product':'Pants',        'brand':'Nike',           'qty':100,    'price':3500,   'gst':12 ,    
#        'srno.':10,  'product':'Jeans',        'brand':'Calvin Klein',   'qty':100,    'price':5000,   'gst':12 ,    
#        'srno.':11,  'product':'Jeans',        'brand':'Calvin Klein',   'qty':100,    'price':5000,   'gst':12 ,   
#        'srno.':12,  'product':'Shirts',       'brand':'Adidas',         'qty':100,    'price':3000,   'gst':12 ,      }

# qty_value = {
            #              'shirts': 100,
            #              'sweatshirts': 100,
            #              'jeans': 100,
            #              'pants': 100
            #                                   }