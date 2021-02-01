class CoffeeMachine:

    def __init__(self):
        self.m_water = 400
        self.m_milk = 540
        self.m_coffee = 120
        self.m_cups = 9
        self.m_money = 550

    def __str__(self):
        print(f'''The coffee machine has:
              {self.m_water} of water
              {self.m_milk} of milk
              {self.m_coffee} of coffee beans
              {self.m_cups} of disposable cups
              {self.m_money} of money
    ''')

    def buy(self):
        drink = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')

        if drink == '1':
            resources = min([(self.m_water // 250), (self.m_coffee // 16), self.m_cups])
            if resources >= 1:
                self.m_water -= 250
                self.m_coffee -= 16
                self.m_cups -= 1
                self.m_money += 4
                print('I have enough resources, making you a coffee!')
            else:
                ingredients = ['water', 'coffee', 'cups']
                limiting = [(self.m_water // 250), (self.m_coffee // 16), self.m_cups]
                for i in limiting:
                    if i == 0:
                        print(f'Sorry I don\'t have enough {ingredients[i]}')

        elif drink == '2':
            resources = min([(self.m_water // 350), (self.m_milk // 75), (self.m_coffee // 20), self.m_cups])
            if resources >= 1:
                self.m_water -= 350
                self.m_milk -= 75
                self.m_coffee -= 20
                self.m_cups -= 1
                self.m_money += 7
                print('I have enough resources, making you a coffee!')
            else:
                ingredients = ['water', 'milk', 'coffee', 'cups']
                limiting = [(self.m_water // 350), (self.m_milk // 75), (self.m_coffee // 20), self.m_cups]
                for i in limiting:
                    if i == 0:
                        print(f'Sorry I don\'t have enough {ingredients[i]}')
        elif drink == '3':
            resources = min([(self.m_water // 200), (self.m_milk // 100), (self.m_coffee // 12), self.m_cups])
            if resources >= 1:
                self.m_water -= 200
                self.m_milk -= 100
                self.m_coffee -= 12
                self.m_cups -= 1
                self.m_money += 6
                print('I have enough resources, making you a coffee!')
            else:
                ingredients = ['water', 'milk', 'coffee', 'cups']
                limiting = [(self.m_water // 200), (self.m_milk // 100), (self.m_coffee // 12), self.m_cups]
                for i in limiting:
                    if i == 0:
                        print(f'Sorry I don\'t have enough {ingredients[i]}')

    def fill(self):

        r_water = int(input('Write how many ml of water do you want to add:\n'))
        r_milk = int(input('Write how many ml of milk do you want to add:\n'))
        r_coffee = int(input('Write how many grams of coffee beans do you want to add:\n'))
        r_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))

        self.m_water += r_water
        self.m_milk += r_milk
        self.m_coffee += r_coffee
        self.m_cups += r_cups

    def take(self):

        while True:
            print(f'I gave you ${self.m_money}')
            self.m_money -= self.m_money
            break

    def actions(self):
        while True:
            task = input('Write action (buy, fill, take, remaining, exit):\n')
            if task == 'buy':
                self.buy()
            elif task == 'fill':
                self.fill()
            elif task == 'take':
                self.take()
            elif task == 'remaining':
                self.__str__()
            else:
                break


coffee_machine = CoffeeMachine()
coffee_machine.actions()

