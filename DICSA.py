def menu():
    UserCart = []
    print("============================================")
    print("Welcome to Electronic Services & Protection:")
    print("============================================\n")
    while True:
        print("\n\t1. Display Our List of Services\n\t2. Search for service\n\t3. Display added services\n\t4. Payment\n\t5. Exit ESP\n\n")

        try:
            value = input("\tPlease input your choice of action (ENTER to exit):")
            val = int(value)
            if val == 1:
                DisplayList(UserCart)
            elif val == 2:
                Search(UserCart)
            elif val == 3:
                DisplayAdded(UserCart)
            elif val == 4:
                Payment(UserCart)
            elif val == 5:
                break
        except ValueError as e:
            if value == '':
                break
            else:
                print("Invalid input, try again")
        except Exception as e:
            print(e)

def DisplayList(UserCart):
    print("Yes, we have the following service(s):")
    ListofService = {"Firewall service":1.2, "Security Ops Center":4.2, "Hot Site":8.5, "Data Protection":10.0}
    AddService(ListofService, UserCart)

def AddService(ListofService, UserCart):
    
    DataList = list(ListofService.items())

    while True:
        count =0
        for service, price in ListofService.items():
            count= count+1
            print('{}. {:20}:\t${:.1f}k/year'.format(count, service, price))
        try:
            value = input("Enter the service 1-4 that you would like to add, or 0 to stop: ")
            val = int(value)

            if ((val > len(DataList)) or (val < 0)):
                print("Invalid input, try again\n")
            elif val == 0:
                break
            else:
                print("You have added \"{}\" to the cart.\n".format(DataList[val-1][0]))
                UserCart.append(DataList[val-1])
                print(UserCart)
        except Exception as e:
                print(e)
        
    #Add the service function

def Search():
    #placeholder
    print("2")

def DisplayAdded(UserCart):
    if len(UserCart) <=0:
        print("You have not add any service.")
    else:
        print("Services you have added today:")
        print("Service{:13}|\tPrice".format(""))
        for items in UserCart:
            print("{:20}|\t${:.1f}/year".format(items[0],items[1]))

def Payment(UserCart):
    #placeholder
    print("4")

menu()
