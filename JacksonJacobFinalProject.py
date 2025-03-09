"""

Author:  Jacob Jackson
Date written: 3/9/2025
Assignment:   Module 8 Final Project
Short Desc:   See included read me documentation for more information.

"""
from tkinter import PhotoImage
from breezypythongui import EasyFrame
class BankingApp(EasyFrame):
    def __init__(self):
        """General window skeleton is set up here, includes labels for username and password
            and input boxes for both, a label for prompting the user, log in and out buttons,
            and finally balance,withdraw, and deposit buttons"""
        EasyFrame.__init__(self, title = "Jackson Credit Union Mobile")
        self.jacobBalance = 5000 #this and next two lines sets initial balances for the three accounts
        self.saraBalance = 7500
        self.coleBalance = 500
        self.usernameLabel = self.addLabel(text = "Username:", row = 0,
                                               column = 0, sticky = "NSEW")
        self.usernameInput = self.addTextField(text = "",row = 0, column = 1, columnspan = 2)
        self.passwordLabel = self.addLabel(text = "Password:", row = 1,
                                               column = 0, sticky = "NSEW")
        self.passwordInput = self.addTextField(text = "",row = 1, column = 1, columnspan = 2)
        self.loginButton = self.addButton(text = "Log in", row = 2, column = 0,
                                                command = self.loginVerification)
        self.logoutButton = self.addButton(text = "Log Out", row = 2, column = 2,
                                                 command = self.logoutUser, state = "disabled")
        greeting = "Please enter username and password" #initial greeting upon launch
        self.greetingLabel = self.addLabel(text = greeting, row = 3,
                                       column = 0, sticky = "NSEW",
                                       columnspan = 3)
        self.balanceButton = self.addButton(text = "View Balance", row = 4, column = 0,
                                                command = self.displayBalance, state = "disabled")
        self.withdrawButton = self.addButton(text = "Withdraw", row = 4, column = 1,
                                                command = self.withdrawFunds,state = "disabled")
        self.depositButton = self.addButton(text = "Deposit", row = 4, column = 2,
                                                command = self.depositFunds,state = "disabled")

    def loginVerification(self):
        """Three example users are created for this program, username and password combination is required for
            successful login. If incorrect a prompt telling the user that something was incorrect will be given."""
        if self.usernameInput.getText() == "jjackson633" and self.passwordInput.getText() == "password1234":
            self.accountBalance = self.jacobBalance # saved user balance is loaded
            self.greetingLabel["text"] = "Hello! What would you like to do today?"
            self.logoutButton["state"] = "normal" #most buttons are disabled by default, passing the login will enable them
            self.balanceButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.loginButton["state"] = "disabled" #login button gets disabled to prevent issues
            self.usernameInput["state"] = "readonly"
            self.passwordInput["state"] = "readonly"
        elif self.usernameInput.getText() == "sajane22" and self.passwordInput.getText() == "321cba":
            self.accountBalance = self.saraBalance #given how i coded logging in, identical code is needed for each user
            self.greetingLabel["text"] = "Hello! What would you like to do today?"
            self.logoutButton["state"] = "normal" 
            self.balanceButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.loginButton["state"] = "disabled"
            self.usernameInput["state"] = "readonly"
            self.passwordInput["state"] = "readonly"
        elif self.usernameInput.getText() == "coletaamox" and self.passwordInput.getText() == "discord467":
            self.accountBalance = self.coleBalance
            self.greetingLabel["text"] = "Hello! What would you like to do today?"
            self.logoutButton["state"] = "normal"
            self.balanceButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.loginButton["state"] = "disabled"
            self.usernameInput["state"] = "readonly"
            self.passwordInput["state"] = "readonly"       
        else:
            self.greetingLabel["text"] = "Username or Password is incorrect"

    def logoutUser(self):
        """Buttons other than log in will be redisabled and the program will return to how it was before logging in,
            the users will also have their balances saved from past action if they need to log in again."""
        self.logoutButton["state"] = "disabled"
        self.balanceButton["state"] = "disabled"
        self.withdrawButton["state"] = "disabled"
        self.depositButton["state"] = "disabled"
        self.loginButton["state"] = "normal"
        self.usernameInput["state"] = "normal"
        self.passwordInput["state"] = "normal"
        self.greetingLabel["text"] = "Please enter username and password"
        if self.usernameInput.getText() == "jjackson633": #else statement to determine what user needs to have their balance changes
            self.jacobBalance = self.accountBalance
        elif self.usernameInput.getText() == "sajane22":
            self.saraBalance = self.accountBalance
        else:
            self.coleBalance = self.accountBalance
            
    def displayBalance(self):
        """Shows current user balance"""
        self.greetingLabel["text"] = "Your account balance is currently $" + str(self.accountBalance)

    def withdrawFunds(self):
        """Removes funds from balance, non numbers and negative numbers are automatically rejected, withdraw cannot exceed balance"""
        withdrawAmount = self.prompterBox(title = "Withdraw Funds", promptString = "Enter amount to withdraw") #opens a new prompt box
        if withdrawAmount.isnumeric() == False: #checks to ensure only positive numbers are entered
            self.greetingLabel["text"] = "Please enter only positive numbers"
        elif int(withdrawAmount) > self.accountBalance: #checks to ensure withdraw does not exceed the balance
            self.greetingLabel["text"] = "Not enough funds to complete transaction."
        else:
            self.accountBalance -= int(withdrawAmount)
            self.greetingLabel["text"] = "Your account balance is now $" + str(self.accountBalance) #informs the user of their balance after successful withdraw
        
    def depositFunds(self):
        """Removes funds from balance, non numbers and negative numbers are automatically rejected"""
        depositAmount = self.prompterBox(title = "Deposit Funds", promptString = "Enter amount to deposit")
        if depositAmount.isnumeric() == False: #checks to ensure only positive numbers are entered
            self.greetingLabel["text"] = "Please enter only positive numbers"
        else:
            self.accountBalance += int(depositAmount)
            self.greetingLabel["text"] = "Your account balance is now $" + str(self.accountBalance)
        
def main():
    BankingApp().mainloop()

if __name__ == "__main__":
    main()
        
