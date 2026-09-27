import json;
import random;
import string;
from pathlib import Path;

class Bank:
    database = "Data.json"
    Data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                Data = json.loads(fs.read())
        else:
            print("No Such File Exist.")
    except Exception as err:
        print(f"An Exception Occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.Data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name": input("Tell Your Name :- "),
            "age": int(input("Tell Your Age :- ")),
            "email": input("Tell Your Email :- "),
            "pin": int(input("Tell Your 4 Number Pin :- ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0,
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry you cannot Create your Account.")
        else:
            print("Account has been Created Successfully.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please Note Down your Account Number.")
            Bank.Data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please tell your Account Number")
        pin = int(input("Please tell your PIN as Well"))
        userdata = [
            i for i in Bank.Data if i["accountNo."] == accnumber and i["pin"] == pin
        ]
        if userdata == False:
            print("Soory no Data Found.")
        else:
            amount = int(input("How Much you Want to Depoit"))
            if amount > 10000 or amount < 0:
                print(
                    "Sorry the Amount is too much you can Deposit Below 10000 and Above 0."
                )
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print("Amount Deposited Successfully.")

    def withdrawmoney(self):
        accnumber = input("please tell your Account Number")
        pin = int(input("please tell your PIN as Well"))
        userdata = [
            i for i in Bank.Data if i["accountNo."] == accnumber and i["pin"] == pin
        ]
        if userdata == False:
            print("Soory no Data Found.")
        else:
            amount = int(input("How Much you Want to Withdraw"))
            if userdata[0]["balance"] < amount:
                print("Soory you don't have that much Money.")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("Amount withdrew successfully.")

    def showdetails(self):
        accnumber = input("Please tell your Account Number")
        pin = int(input("Please tell your PIN as Well"))
        userdata = [
            i for i in Bank.Data if i["accountNo."] == accnumber and i["pin"] == pin
        ]
        print("Your Information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Please tell your Account Number")
        pin = int(input("Please tell your PIN as Well"))
        userdata = [
            i for i in Bank.Data if i["accountNo."] == accnumber and i["pin"] == pin
        ]
        if userdata == False:
            print("No Such User Found.")
        else:
            print("You cannot Change the Age, Account Number, Balance.")
            print("Fill the Details for Change or Leave it Empty if no Change.")
            newdata = {
                "name": input("Please tell New Name or Press Enter : "),
                "email": input("Please tell your New Email or Press Enter to Skip : "),
                "pin": input("Enter New Pin or press enter to skip : "),
            }
            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            newdata["age"] = userdata[0]["age"]
            newdata["accountNo."] = userdata[0]["accountNo."]
            newdata["balance"] = userdata[0]["balance"]
            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            Bank.__update()
            print("Details Updated Successfully.")

    def Delete(self):
        accnumber = input("Please tell your Account Number ")
        pin = int(input("Please tell your PIN as Well"))
        userdata = [
            i for i in Bank.Data if i["accountNo."] == accnumber and i["pin"] == pin
        ]
        if userdata == False:
            print("Sorry No Such Data Exist.")
        else:
            check = input(
                "Press Y if you Actually Want to Delete the Account or Press N"
            )
            if check == "n" or check == "N":
                print("bypassed")
            else:
                index = Bank.Data.index(userdata[0])
                Bank.Data.pop(index)
                print("Account Deleted Successfully.")
                Bank.__update()
user = Bank()
print("press 1 for creating an Account.")
print("press 2 for Deposititing the Money in the Bank.")
print("press 3 for Withdrawing the Money.")
print("press 4 for Show Details.")
print("press 5 for Updating the Details.")
print("press 6 for Deleting your Account.")
check = int(input("Tell your Response :- "))
if check == 1:
    user.Createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.Delete()