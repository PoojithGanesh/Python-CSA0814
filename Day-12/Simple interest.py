'''Write a python program using functions to calculate the simple interest, suppose the customer is aa senior citizen. He is being offered
12 peercentage rate of interest; for all other cusstomers, the ROI is 10 percentage'''
def main():
    principal = float(input("Enter the principal amount: "))
    time = float(input("Enter the time period (in years): "))
    is_senior_citizen = input("Are you a senior citizen? (yes/no): ")

    if is_senior_citizen.lower() == "yes":
        rate = 12
    else:
        rate = 10

    interest = (principal * rate * time) / 100
    print("The simple interest is: ", interest)

main()
