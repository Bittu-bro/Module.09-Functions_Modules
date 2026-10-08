amount = 0.0
kyc_documents = {}
def current_Balence():
    global amount 
    print(f"We are just fatching your Current Balence\n\tYour Current Balence is ₹{amount}")

    
def deposit_amount():
    global amount
    deposit_amount = float(input("Enter your amout: "))
    if deposit_amount > 0.00:
        amount += deposit_amount   
        print(f"We are just depositing your Amount\n\tNow, your Current Balence is ₹{amount}")
    else:
        print("Your Entered Amount is Negative or Zero !!\n\tPlease Try Again.")


def withdrawal_amount():
    global amount
    withdrawal_amount = float(input("Enter your amout: "))
    if withdrawal_amount > amount:
        print(f"You cannot withdraw the amount because you do not have that much money in your account!!\n Please Try Again with Vaild Amount.")
    elif withdrawal_amount > 0.00:
        amount -= withdrawal_amount
        print(f"we are just Withdrawaling your Amount\nNow, your Current Balence is ₹{amount}")
    else:
        print("Your Entered Amount is Negative or Zero !!\n\tPlease Try Again.")


def cheak_kyc_status():
    if len(kyc_documents) == 0:
        print("KYC not Done")
    else:
        for doc in kyc_documents:       
            print(f"{doc}: {kyc_documents[doc]}")

def update_your_kyc(documents):
    global kyc_documents
    kyc_documents.update(documents)
    




def quit():
    global amount
    print(f"Your current Balence is ₹{amount}")
    print("Thanks for banking with us.\n\t \"Best Regards From KBC Bank\"")


    
def invalid():
    print("You have selected an incorrect choice; please enter the correct choice.")

























if __name__ == "__main__":
    print("==============================")
    print("Welcome to the \'KBC Bank\'")

    while True:
        print("==============================")
        print(f"1. Cheak Your Balence\n2. Deposite An Amount\n3. Withdrawal Amount\n4. Cheak your KYC Status\n5. Update Your KYC Status\n6. Quit")
        print("==============================")
        print("\tChoice shuld be 1 to 6")
        print("==============================")
        choice = input("Enter your choice: ")
        print("==============================")
        if choice == '6':
            quit()
            break
        elif choice == '1':
            current_Balence()
        elif choice == '2':
            deposit_amount()
        elif choice == '3':
            withdrawal_amount()
        elif choice == '4':
            cheak_kyc_status()
        elif choice == '5':
            kyc_docs = {}
            n_document = int(input("Enter How Many Document You Want To Add: "))
            for i in range (n_document):
                key = input("Enter The Document Name: ")
                value = input("Enter The Document Number: ")
                kyc_docs[key] = value
            update_your_kyc(kyc_docs)
            print("KYC Updated")
        else:
            invalid()

