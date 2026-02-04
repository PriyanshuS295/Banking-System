# project and we are creating a banking system

import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]

    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())

        else:
            print("No such file exists")
    except Exception as err:
        print(f"an eception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)


    def Createaccount(self):
            info = {
                "name":input("Tell your name: "),
                "age":int(input("tell your age: ")),
                "email":input("tell your email: "),
                "pin": int(input("Tell your pin: ")),
                "accountNo. ": Bank.__accountgenerate(),
                "balance ": 0
            }

            if info['age']<18 or len(str(info['pin'])) !=4:
                print("Sorry you can not create you account")

            else:
                print("Account has been created successfully")
                for i in info:
                    print(f"{i} : {info[i]}")
                print("Please note down your account number")

                Bank.data.append(info)
                Bank.__update()

    def depositmoney(self):
        accnumber=input("please tell your account number: ")
        pin=int(input("Please tell your pin: "))

        userdata= [i for i in Bank.data if i['accountNo. ']== accnumber and i['pin']==pin]
        if userdata==False:
            print("Sorry No Data Found")
        else:
            amount=int(input("How much you want to deposit: "))
            if amount > 10000 or amount<0:
                print("Sorry the amount is too much, deposit amount below 10000")
            else:
                userdata[0]['balance '] += amount
                Bank.__update()
                print("Amount deposited successfully")
            
    def withdrawmoney(self):
        accnumber=input("please tell your account number: ")
        pin=int(input("Please tell your pin: "))

        userdata= [i for i in Bank.data if i['accountNo. ']== accnumber and i['pin']==pin]
        if userdata==False:
            print("Sorry No Data Found")
        else:
            amount=int(input("How much you want to withdraw: "))
            if userdata[0]['balance ']<amount:
                print("Sorry you don't have that much money")
            else:
                userdata[0]['balance '] -= amount
                Bank.__update()
                print("Amount withdrew successfully")

    def showdetails(self):
        accnumber=input("please tell your account number: ")
        pin=int(input("Please tell your pin: "))
        userdata= [i for i in Bank.data if i['accountNo. ']== accnumber and i['pin']==pin]
        print("Your details are: ")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber=input("please tell your account number: ")
        pin=int(input("Please tell your pin: "))
        userdata= [i for i in Bank.data if i['accountNo. ']== accnumber and i['pin']==pin]

        if userdata== False:
            print("No such user found")

        else:
            print("You cannot change the age, account number, balance")
            print("Fill the details for change or leave it empty if no change")

            newdata={
                "name": input("Please tell new name or press enter:"),
                "email": input("please tell your new emailor press enter"),
                "pin": input("Enter new pin or press enter to skip")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']

            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']

            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['accountNo. '] = userdata[0]['accountNo. ']

            newdata['balance '] = userdata[0]['balance ']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue

                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print("details update successfully")

    def delete(self):
        accnumber=input("please tell your account number: ")
        pin=int(input("Please tell your pin: "))
        userdata= [i for i in Bank.data if i['accountNo. ']== accnumber and i['pin']==pin]
        
        if userdata== False:
            print("No such user found")

        else:
            index=Bank.data.index(userdata[0])
            Bank.data.pop(index)
            print("Bank Account Deleted Successfully")
            Bank.__update()

            
user = Bank()

print("Press 1 for creating an Account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating details")
print("Press 6 for Deletion of account")

check=int(input("Tell you response: "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check ==3:
    user.withdrawmoney()

if check==4:
    user.showdetails()

if check==5:
    user.updatedetails()

if check==6:
    user.delete()