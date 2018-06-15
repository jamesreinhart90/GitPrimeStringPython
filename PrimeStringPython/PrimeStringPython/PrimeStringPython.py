def main():

    def GetPrimeString():
        primeString = ""
        for i in range (2,1994):
            notPrime = 0

            for j in range (2, i):
                if (i % j is 0):
                    notPrime += 1

            if notPrime is 0:
                primeString += str(i)
        return primeString

    def GetInput():
        for k in range(1000):
            userInput = input("Please enter a number between 1 and 1,000: ")

            try:
                userInput = int(userInput)
                if (userInput > 1000 or userInput < 1):
                    print("Invalid input!")
                else:
                    break
            except:
                print("Invalid input!")
        return userInput

    def GetID(userInput, primeString):
        id = primeString[userInput - 1 : userInput + 4]
        return id

    def OutMessage(id):
        print(format("Your id is {0} {1}", [int(id), 3]))

    print("Prime String Finder")
    OutMessage(GetID(GetInput(), GetPrimeString()))

main()