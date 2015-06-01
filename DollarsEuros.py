#Money Exchange Program
#Takes in a currency and changes it to another

currency = raw_input("What is currency?(dollar/euros)")
money = input("Enter your amount:")

if currency == 'dollar':
    euros = money * 0.92
    print "Your", money, "dollars are", euros, "euros."

elif currency == 'euros':
    dollars = money * 1.09
    print "Your", money, "euros are", dollars, "dollars."
elif currency == 'Won':
    won = money * 0.00090
    print "Your", money, "won are", won, "dollars." 
else:
    print "Sorry your currency is not supported for now." 
