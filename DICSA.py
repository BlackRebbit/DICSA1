import sys
import getpass
import hashlib
import base64
ListofService = {"Firewall Service":1.2, "Security Ops Center":4.2, "Hot Site":8.5, "Data Protection":10.0} #Declare List of Service

def main(UserCart):
    
    print("============================================")
    print("Welcome to Electronic Services & Protection:")
    print("============================================\n")
    while True:
        print("\n\t1. Display Our List of Services\n\t2. Search for service\n\t3. Display added services\n\t4. Payment\n\t5. Admin Menu\n\t6. Exit ESP\n\n")

        try:
            value = input("\tPlease input your choice of action (ENTER to exit):")
            val = int(value)

            #using if else statement to select function
            if val == 1: #Display List of Services
                AddService(ListofService,UserCart)
            elif val == 2: #Search for Service
                Search(ListofService, UserCart)
            elif val == 3: #Display added services
                DisplayAdded(UserCart)
            elif val == 4: #Payment
                Payment(UserCart)
            elif val == 5: #admin menu
                AdminLogin()
            elif val == 6:#Exit
                print("Thank you for using ESP.")
                sys.exit()

        except ValueError as e:
            if value == '': #check for ENTER
                print("Thank you for using ESP.")
                sys.exit()
            else: #any other input are invalid
                print("Invalid input, try again")
        except Exception as e:
            print(e)

def AdminLogin():
    #username - admin
    #password - 12345
    username = "YWRtaW4=".encode() #encode to byte form
    passwd1 = "8342d2719fa5821c254d6484cfc0716fc1e01b8e290ea575187762fc" #hardcoded admin password
    passwd2 = "428d14bd293db60510a7d17e09a714d8aec70c6f5e430a966c499e3d1ad3dede7feb2e32"
    name = input("Username: ")
    
    key = getpass.getpass("Password: ") #get password
    hash=hashlib.sha512(b'key') #hash with sha512
    hash.update(b'salt') #hash with salt
    finalkey = hash.hexdigest()

    if ((finalkey == passwd1+passwd2) and base64.b64encode(name.encode()) == username): #Base64 is used to hide the username
        AdminMain()
    else:
        print("invalid username or password")

def AdminMain():

    while True:
        print("1. Add New Service")
        print("2. Modify Service")
        print("3. Remove Service")
        print("4. Back to Main Menu")
        try:
            value = input("\tPlease input your choice of action:")
            val = int(value)
            if val == 1:
                AddNewService(ListofService)
            elif val == 2:
                ModifyService(ListofService)
            elif val == 3:
                RemoveService(ListofService)
            elif val == 4:
                break

        except ValueError as e:
                print("Invalid input, try again")
        except Exception as e:
            print(e)


def AddNewService(ListofService):
    while True:
        try:
            service = input("Service name: ")
            price = input("Price per year: ")
            price_float = float(price)
            print("Service name: {}\n Price: ${:.1f}k/year".format(service,price_float))
            value = input("Are you sure you want to add this service to the list? (Y/N) ")
            if value.lower() == 'y':
                print("Service \"{}\" added to the list.".format(service))
                ListofService.update({service:price_float})
                break
            elif value.lower() =='n':
                print("The service is not added to the list.")
                break
            else:
                print("Invalid input, try again.")
        except ValueError as e:
            print("Invalid input, try again")
        except Exception as e:
            print(e)           

def ModifyService(ListofService):
    while True:
        count=0
        for service, price in ListofService.items():
            count=count+1 #count for each service in the list
            print('{}. {:20}:\t${:.1f}k/year'.format(count, service, price))
        InputService = input("Which service could you like to modify? (Enter the service name, type \"Cancel\" to exit to menu) ")
        if InputService.lower() == "cancel":
                    break
        else:
            Find = False
            
            for service,price in ListofService.items():
                if InputService in service:
                    Find = True
                    ServiceName = service
                    ServicePrice = price

            if Find == True:
                while True:
                    value = input("Are you sure you want to modify {}? (Y/N) ".format(ServiceName))
                    if value.lower() == "y":
                        print("1. Edit Service Name")
                        print("2. Edit Price")
                        print("3. Cancel")
                        value = input("What could you like to modify? (Enter the index number) ")
                        val = int(value)

                        if val == 1:
                            while True:
                                value = input("What is the new service name? ")
                                confirm = input("Are you sure you want to change the service name from {} to {}? (Y/N) ".format(ServiceName,value))
                                if confirm.lower() == "y":
                                    ListofService[value] = ListofService[ServiceName]
                                    ListofService.pop(ServiceName)
                                    print("The new service name is {}.\n".format(value))
                                    break
                                elif confirm.lower() == "n":
                                    print("The service name has not change.\n")
                                    break
                                else:
                                    print("Invalid Input, try again.")

                        elif val == 2:
                            while True:
                                try:
                                    value = input("What is the new price? ")
                                    val = float(value)
                                    confirm = input("Are you sure you want to change the service price from {} to {}? (Y/N) ".format(ServicePrice,value))
                                    if confirm.lower() == "y":
                                        ListofService.update({ServiceName:val})
                                        print("The new price has changed to {}".format(value))
                                        break
                                    elif confirm.lower() == "n":
                                        print("The service price has not change.\n")
                                        break
                                    else:
                                        print("Invalid Input, try again.")

                                except ValueError as e:
                                    print("Invalid input, try again")
                                except Exception as e:
                                    print(e)   
                                    
                        elif val == 3:
                            print("Back to Admin Menu..")
                            break
                        else:
                            print("Invalid input, try again.")
                    elif value.lower() == "n":
                        break
                    else: 
                        print("Invalid input, try again.")
            else:
                print("Invalid input, try again.")
def RemoveService(ListofService):
    while True:
        count=0
        for service, price in ListofService.items():
            count=count+1 #count for each service in the list
            print('{}. {:20}:\t${:.1f}k/year'.format(count, service, price))
        value = input("Which service could you like to remove? (Enter the service name, type \"Cancel\" to exit to menu) ")
        if value.lower() == "cancel":
            break
        else:
            Find = False
            for service in ListofService:
                if value in service:
                    Find = True

            if Find == True:
                val = input("Are you sure you want to remove {}? (Y/N)".format(value))
                if val.lower() == 'y':
                    ListofService.pop(value) #Remove from list
                    print("{} has been removed.".format(value))
                    break
            else:
                print("Service not found. Please enter the exact match")
       

def AddService(ListofService, UserCart):
    DataList = list(ListofService.items()) 
  
    print("Yes, we have the following service(s):")
    while True:
        count=0
        for service, price in ListofService.items():
            count=count+1 #count for each service in the list
            print('{}. {:20}:\t${:.1f}k/year'.format(count, service, price))
        try:
            value = input("Enter the service 1-{} that you would like to add, or 0 to stop: ".format(count)) #Ask user which service they want to add
            val = int(value) #convert to int

            if ((val > len(DataList)) or (val < 0)):
                print("Invalid input, try again\n")
            elif val == 0:
                break
            else:
                while True:
                    value = input("Are you sure that you want to add {} to your cart? (Y/N)".format(DataList[val-1][0])) #Confirm with user if they want to add service to cart
                    if value.lower() == "y":
                        print("You have added \"{}\" to the cart.\n".format(DataList[val-1][0])) 
                        UserCart.append(DataList[val-1]) #Add to User Cart
                        break
                    elif value.lower() =="n":
                        print("You have NOT add \"{}\" to the cart.\n".format(DataList[val-1][0]))
                        break
                    else:
                        print("Invalid input, please try again.\n")
        except ValueError as e:
            print("Invalid input, try again\n")
        except Exception as e:
            print(e)
        
def Search(ListofService, UserCart):
    while True:
        value = input("Please input service to search: ")
        count=0
        newlist= {}

        for service,price in ListofService.items(): #retrieve the list of services and price from the list of service
            if value.lower() in service.lower(): #check the user's input if service contain the substring, used lower() to ensure that it is not case sensitive
                count=count+1 
                newlist.update({service:price})

        if len(newlist) <=0: #if length of the new list is 0, then ask user to try again.
            print("No service found, try again.")
        else: #if length is more than 1, then run addService with the newlist and break from while loop
            AddService(newlist, UserCart)
            break
    
def DisplayAdded(UserCart):
    if len(UserCart) <=0: #Check if User cart is empty
        print("You have not add any service.")

    else: #else display the added services from the user cart
        while True:
            count=0
            print("Services you have added today:")
            print("Index\t|\tService{:13}|\tPrice".format(""))
            for items in UserCart:
                count=count+1
                print("{}\t|\t{:20}|\t${:.1f}/year".format(count,items[0],items[1]))
            print("\n1. Remove added service from cart")
            print("2. Back to menu")
        
            try:
                value = input("Please input your choice of action: ")
                val = int(value)

                if val == 1: #Ask user which service they would like to remove

                    value = input("\nWhich service would you like to remove(Enter the index number), or 0 to stop:")
                    val = int(value)

                    if val == 0: #break back to menu
                        break
                    elif ((val <=0) or (val > count)): #invalid input
                        print("Invalid input, please try again.\n")
                    else: #Ask user if confirm to remove that service, if yes then remove from cart else break back to menu
                        value = input("Are you sure you want to remove {}(Y/N)?".format(UserCart[val-1][0]))
                        if value.lower() == 'y':
                            print("{} has successfully removed from cart".format(UserCart[val-1][0]))
                            UserCart.pop(val-1)
                            
                        elif value.lower() == 'n':
                            break
                        else:
                            print("Invalid input, please try again. \n")
                elif val == 2:
                    print("Back to menu..")
                    break
                else:
                    print("Invalid input, please try again. \n")

            except ValueError as e:
                print("Invalid input, try again\n")
            except Exception as e:
                print(e)

def Payment(UserCart):
    if len(UserCart) <=0: #Check if User cart is empty
        print("You have not add any service.")

    else: #else display the added services from the user cart
        count=0
        total=0
        print("Pls check your services added:")
        for items in UserCart:
            count=count+1
            total+=items[1]
            print("{}. {:20}:\t${:.1f}/year".format(count, items[0],items[1]))
        print("Your subscription will be a total of : ${}/year.\n".format(total))
        while True:
            value = input("Confirm payment? (Y/N)")
            if value.lower() == "y":
                print("Thank you for using ESP.")
                sys.exit() #exit
            elif value.lower() =="n":
                print("Back to Menu..")
                break #break out of loop to menu
            else:
                print("Invalid input, try again.")

if __name__ == "__main__":
    UserCart = [] #Declare User Cart
    main(UserCart)