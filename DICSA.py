import sys

def main(UserCart):
    ListofService = {"Firewall Service":1.2, "Security Ops Center":4.2, "Hot Site":8.5, "Data Protection":10.0} #Declare List of Service
    print("============================================")
    print("Welcome to Electronic Services & Protection:")
    print("============================================\n")
    while True:
        print("\n\t1. Display Our List of Services\n\t2. Search for service\n\t3. Display added services\n\t4. Payment\n\t5. Exit ESP\n\n")

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
            elif val == 5:#Exit
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
            
            if val == 1:
                while True:
                    value = input("\nWhich service could you like to remove(Enter the index number), or 0 to stop:")
                    val = int(value)
                    if val == 0:
                        break
                        main(UserCart)
                    elif ((val <=0) or (val > count)):
                        print("Invalid input, please try again.\n")
                    else:
                        value = input("Are you sure you want to remove {}?".format(UserCart[val-1][0]))
                        if value.lower() == 'y':
                            print("{} has successfully removed from cart\n".format(UserCart[val-1][0]))
                            UserCart.pop(val-1)
                            DisplayAdded(UserCart)
            elif val == 2:
                print("Back to menu..")
                main(UserCart)
            else:
                print("Invalid inpuit, please try again. \n")

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