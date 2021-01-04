import sys
def main():
    
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
                DisplayList()
                sys.exit()
            elif val == 2: #Search for Service
                Search()
            elif val == 3: #Display added services
                DisplayAdded()
            elif val == 4: #Payment
                Payment()
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

def DisplayList():
    #placeholder
    print("1")
    print("Yes, we have the following service(s):")
    print("1. Firewall service    :          $1.2k/year")
    print("2. Security Ops Center :          $4.2k/year")
    print("3. Hot Site            :          $8.5k/year")
    print("4. Data Protection     :          $10.0k/year")
    print("Enter the service 1-4 that you would like to add, or 0 to stop: ")


def Search():
    #placeholder
    print("2")

def DisplayAdded():
    #placeholder
    print("3")

def Payment():
    #placeholder
    print("4")

main()
