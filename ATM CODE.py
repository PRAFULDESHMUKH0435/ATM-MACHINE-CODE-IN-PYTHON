import  time
balance=10000
print("Please Enter Your Name:")
name=input()
pin=int(input("Enter Your ATM Pin: \n"
              "pin=1234\n"))
print(f"Welcome Mr. {name.upper()}, We Are Fetching Your Account Details, Please Wait")
time.sleep(3)
if pin==1234:
    while True:
                print(f"""
                    Choose Following Operations\n
                    Enter 1 For Balance Check
                    Enter 2 To Deposit Money
                    Enter 3 To Withdraw Money
                    Enter 4 To Exit """)


                try:
                    option=int(input())

                except:
                    print("Invalid Operation Chosen")






                if option==1:
                    print(f"Your Current Balance Is Rs. {balance}")

                elif option==2:
                    print("How Much Money You Want To Deposit")
                    deposit=int(input())
                    updated_balance=balance+deposit
                    if (deposit<=0):
                        print("Please Enter Valid Amount")


                    else:
                        print(f"Rs. {deposit} Has Been Deposited In Your Account\n"
                              f"Your Current Balance Is Rs. {updated_balance}")

                elif option==3:
                    print("How Much Money You Want To Withdraw")
                    withdraw=int(input())
                    withdraw_balance=balance-withdraw
                    if (withdraw>balance):
                        print("Your Account Does Not Have This Amount Of Balance\n"
                              "Please Enter Less Amount To Proceed")


                    else:
                        print(f"Rs. {withdraw} Has Been Withdrawn From  Your Account\n"
                              f"Your Current Balance Is Rs. {withdraw_balance}")


                elif option==4:
                    print("Exited Sucessfully")
                    exit()

                else:
                    print("Invalid Operation Chosen, Please Choose Correct Operation To Proceed")






else:
    print(" Sorry Invalid Pin, Try Again")


