def loggedin():
    print("\nLog in Successfull")

    print("\n(q)uit")
    answer1 = input("")

    if answer1 == "q":
        return True
    else:
        while True:
            break



users = ['sample']
passwords = ['sample']


while True:
    print("Select an option (l)ogin | (s)ign up")
    answer = input("")

    if answer == "s":
        
        global user
        global password 
        
        while True:
            user = input("Create user name: ")
    
            if user in users:
                print("Username already exists")
                continue
        
            else:
                users.append(user)
                break
        
        password = input("Create user password: ")
        passwords.append(password)
        print("\nAccount created successfully!")
        continue
        
        
    
    elif answer == "l":
        
        username = input("Enter user name: ")
    
        while username not in users:
            print("User not found")
            username = input("Enter user name: ")
    
            
    
        user_password = input("Enter user password: ")
    
        while user_password not in passwords:
            print("Password incorrect")
            user_password = input("Enter user password: ")
            
        loggedin()
                   
    
    else:
         print("Error Select either l or s")
         continue




    
