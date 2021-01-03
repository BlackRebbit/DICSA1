def menu():
    print("============================================")
    print("Welcome to Electronic Services & Protection:")
    print("============================================\n\n")
    while True:
        print("\t1. Display Our List of Services\n\t2. Search for service\n\t3. Display added services\n\t4. Payment\n\t5. Exit ESP\n\n")

        try:
            value = input("\tPlease input your choice of action (ENTER to exit):")
            val = int(value)
            if val == 1:
                DisplayList()
            elif val == 2:
                Search()
            elif val == 3:
                DisplayAdded()
            elif val == 4:
                Payment()
            elif val == 5:
                break
        except ValueError as e:
            if value == '':
                break
            else:
                print("Invalid input, try again")
        except Exception as e:
            print(e)

def DisplayList():
    #placeholder
    print("1")
    print("Yes, we have the following service(s):")
    ListofService = {"Firewall service":1.2, "Security Ops Center":4.2, "Hot Site":8.5, "Data Protection":10.0}
    AddService(ListofService)

def AddService(ListofService):
    count =0

    for service, price in ListofService.items():
        count= count+1
        print('{}. {:20}:\t${:.1f}k/year'.format(count, service, price))
     
    print("Enter the service 1-4 that you would like to add, or 0 to stop: ")
    #Add the service function

def Search():
    #placeholder
    print("2")

def DisplayAdded():
    #placeholder
    print("3")

def Payment():
    #placeholder
    print("4")

menu()
