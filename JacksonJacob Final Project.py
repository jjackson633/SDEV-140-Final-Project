"""

Author:  Jacob Jackson
Date written: Pending
Assignment:   Module 8 Final Project
Short Desc:   See attached document

"""
from breezypythongui import EasyFrame
class BankingApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Jackson Trust Mobile")
        self.accountBalance = 5000
        greeting = "Hello! What would you like to do today?"
        self.guessLabel = self.addLabel(text = greeting, row = 0,
                                       column = 0, sticky = "NSEW",
                                       columnspan = 3)
        self.balanceButton = self.addButton(text = "View Balance", row = 1, column = 0,
                                         command = self.displayBalance)
        self.withdrawalButton = self.addButton(text = "Withdrawal", row = 1, column = 1)
        self.depositButton = self.addButton(text = "Deposit", row = 1, column = 2)

    def displayBalance(self):
        self.guessLabel["text"] = "Your account balance is currently $" + str(self.accountBalance)
        
def main():
    BankingApp().mainloop()

if __name__ == "__main__":
    main()
        
