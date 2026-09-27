import json;
import random;
import string;
from pathlib import Path;

class Bank:
    database = "Data.json"
    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, "r") as fs:
                return json.load(fs)
        return []

    @classmethod
    def save_data(cls, Data):
        with open(cls.database, "w") as fs:
            json.dump(Data, fs, indent=4)

    @classmethod
    def generate_account_number(cls):
        chars = (
            random.choices(string.ascii_letters, k=3)
            + random.choices(string.digits, k=3)
            + random.choices("!@#$%^&*", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    @classmethod
    def create_account(cls, name, age, email, pin):
        Data = cls.load_data()
        if age < 18 or len(str(pin)) != 4:
            return None, "Age must be 18+ and PIN should be 4 Digits."
        acc_no = cls.generate_account_number()
        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": acc_no,
            "balance": 0,
        }
        Data.append(user)
        cls.save_data(Data)
        return user, "Account Created Successfully."

    @classmethod
    def find_user(cls, acc_no, pin):
        Data = cls.load_data()
        for user in Data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                return user
        return None

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        Data = cls.load_data()
        for user in Data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                if 0 < amount <= 10000:
                    user["balance"] += amount
                    cls.save_data(Data)
                    return True, "Deposit Successful."
                return False, "Amount must be Between 1 and 10000."
        return False, "Invalid Account or PIN."

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        Data = cls.load_data()
        for user in Data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                if user["balance"] >= amount:
                    user["balance"] -= amount
                    cls.save_data(Data)
                    return True, "Withdrawal Successful."
                return False, "Insufficient Balance."
        return False, "Invalid Account or PIN."

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
        Data = cls.load_data()
        for user in Data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                user["name"] = name or user["name"]
                user["email"] = email or user["email"]
                user["pin"] = int(new_pin) if new_pin else user["pin"]
                cls.save_data(Data)
                return True, "User Details Updated."
        return False, "User not Found."

    @classmethod
    def delete_user(cls, acc_no, pin):
        Data = cls.load_data()
        for i, user in enumerate(Data):
            if user["accountNo."] == acc_no and user["pin"] == pin:
                Data.pop(i)
                cls.save_data(Data)
                return True, "Account Deleted Successfully."
        return False, "Account not Found."