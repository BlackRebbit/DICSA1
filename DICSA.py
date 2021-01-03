
def menu():
    print("============================================")
    print("Welcome to Electronic Services & Protection:")
    print("============================================\n\n")

    print("\t1. Display Our List of Services\n\t2. Search for service\n\t3. Display added services\n\t4. Payment\n\t5. Exit ESP\n\n")

    while True:
        val = 0
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