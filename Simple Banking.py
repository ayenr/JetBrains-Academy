from random import seed, choices, choice
import sqlite3
from sys import exit


def validate_number(card_number):
    number = list(map(int, card_number[:-1]))

    numbers_sum = 0

    for i in range(len(number)):

        val = number[i]

        if i % 2 == 0:
            val *= 2

        numbers_sum += val if val < 10 else val - 9

    checksum = ((numbers_sum // 10 + 1) * 10 - numbers_sum) % 10

    return True if checksum == int(card_number[-1]) else False


class Card:

    def __init__(self, account_number='', pin=''):
        self.account_number = account_number
        self.pin = pin
        self.balance = 0

    @staticmethod
    def new_account_number():
        inn = '400000'
        seed()
        can = (choices(range(10), k=9))
        can1 = str("".join(map(str, can)))
        accountno = list(map(int, inn + can1))

        number_sum = 0

        for i in range(len(accountno)):
            val = accountno[i]

            if i % 2 == 0:
                val *= 2

            number_sum += val if val < 10 else val - 9

        checksum = ((((number_sum // 10) + 1) * 10 - number_sum) % 10)
        accountno.append(checksum)
        accountno = map(str, accountno)
        accountno = "".join(accountno)

        return accountno

    @staticmethod
    def new_pin():
        seed()
        pin_number = "".join([str(choice(range(9))) for _ in range(4)])

        return pin_number

    def new_account(self):
        self.account_number = self.new_account_number()
        self.pin = self.new_pin()

        print('Your card number:', self.account_number, 'Your card PIN:', self.pin, sep='\n', end='\n \n')


class BankDB:

    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
        )""")
        self.conn.commit()

    def card_entry(self, card: Card()):
        self.cur.execute(f'INSERT INTO card (number, pin) VALUES ({str(card.account_number)},{str(card.pin)});')
        self.conn.commit()

    def balance(self, number):
        return self.cur.execute(f"""SELECT balance
        FROM card
        WHERE number = {str(number)}""").fetchone()[0]

    def add_balance(self, number):
        money = int(input('Enter income: \n'))
        self.cur.execute(f"""
            UPDATE card
            SET 
                balance = balance + {money}
            WHERE 
                number = {number};
        """)
        self.conn.commit()

    def update_balance(self, number, money):
        self.cur.execute(f'''
                    UPDATE card
                    SET 
                        balance = balance + '{money}'
                    WHERE 
                        number = '{number}'
                ''')
        self.conn.commit()

    def delete_account(self, number):
        self.cur.execute(f"DELETE FROM card WHERE number = {number}")
        self.conn.commit()

    def close(self):
        self.conn.close()


class BankMenu:
    def __init__(self):
        self.card = Card()
        self.db = BankDB()
        self.logincard = ''
        self.loginpin = ''

    def login(self):

        while True:
            self.logincard = (input("Enter your card number: \n"))
            self.loginpin = (input("Enter your PIN: \n"))

            self.db.cur.execute(f"""SELECT number
            FROM card
            WHERE number = {self.logincard} AND
            pin = {self.loginpin}""")

            if self.db.cur.fetchone():
                print('You have successfully logged in! \n')
                self.submenu()

            else:
                print('Wrong card number or PIN! \n')
                break

    def transfer(self, number):
        transferacc = input('Enter transfer account \n')

        if transferacc == self.logincard:
            print("You can't transfer money into your own account!\n")

        elif validate_number(transferacc):
            card_details = self.db.cur.execute(f"""SELECT number
                    FROM 
                        card
                    WHERE 
                    number = {str(transferacc)}
                    """).fetchone()

            try:

                if transferacc in card_details:
                    amount = int(input("Enter how much money you want to transfer:\n"))
                    if amount > self.db.balance(number):
                        print("Not enough money! \n")
                    else:
                        self.db.update_balance(transferacc, amount)
                        self.db.update_balance(number, -amount)
                        print('Success! \n')

            except TypeError:
                print('Such a card does not exist.\n')

        else:
            print('Probably you made mistake in card number. Please try again! \n')

    def close(self):
        print('Bye!')
        self.db.close()
        exit(0)

    def submenu(self):

        while True:
            choice2 = input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")

            if choice2 == "1":
                print(f'Balance: {self.db.balance(self.logincard)} \n')
            elif choice2 == "2":
                self.db.add_balance(self.logincard)
            elif choice2 == "3":
                self.transfer(self.logincard)

            elif choice2 == "4":
                self.db.delete_account(self.logincard)
                print('The account has been closed!')
            elif choice2 == "5":
                self.db.delete_account(self.logincard)
            elif choice2 == "0":
                self.close()

    def starter_menu(self):
        while True:
            choice1 = input("""1. Create an account
2. Log into account
0. Exit
""")

            if choice1 == '1':
                self.card.new_account()
                self.db.card_entry(self.card)
            elif choice1 == '2':
                self.login()

            elif choice1 == '0':
                self.close()


if __name__ == "__main__":
    menu = BankMenu()
    menu.starter_menu()