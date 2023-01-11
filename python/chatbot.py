import sys
## INTELLIGENT CHATBOT FOR NOBMART

print("HI!!, THIS IS NOBMART CHATBOT\n")
print("HOW MAY WE HELP YOU TODAY??\n")
print("TAP 'Y' TO CONTACT OUR CUSTOMER SERVICE PERSONNELS OR 'W' TO WRITE TO US")
while True:
    userin = input()
    if userin == 'Y':
        print("Hang on as an agent will be available shortly")
        sys.exit()
    elif userin == 'W':
        print("You can contact us @ nobmart@help.com")
        sys.exit()
    else:
        print("Please select a valid input as requested above")
        continue
