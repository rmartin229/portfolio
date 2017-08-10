import turtle
import math


class User:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.name = ""
        self.connections = []

    def addConnectionUser (self, friend):
        self.connections.append(friend)

    def deleteConnection (self, friend):
        self.connections.pop(friend)
        return(connections)

    def makeAccount (self):
        self.name=input("What is your name?")

class Network:
    # Define the fields and methods for your object here.
    def __init__ (self):
        self.userList = []

    def numberOfUsers (self):
        return (len(userList))

    def addConnectionNetwork (self, User1, User2):
        if User1 not in User2.connections:
            User1.addConnectionUser(User2)
            User2.addConnectionUser(User1)
            print("You are now friends.")
        # if friend not in userList:
        #     self.userList.append(friend)
        # else:
        #     print("User is already in your list of friends")

    def getUsers (self):
        return (userList)

    def getConnections (self):
        return (connections)

def main():
    myNetwork = Network()
    userName = User()
    userName.makeAccount()
    User1 = User()
    userName.makeAccount()
    User2 = User()
    print("Do you want to add friends?")
    user_input = input()
    if user_input == "Yes":
        myNetwork.addConnectionNetwork(User1,User2)

#Runs your program.
if __name__ == '__main__':
    main()
