import sys
## INTELLIGENT CHATBOT FOR NOBMART

print("HI!!, THIS IS NOBMART CHATBOT\n")
print("SELECT ONE OPTION OR IF YOU WISH TO QUIT 'Q'")

# Taking inputing from user
#while True:
reply = input()
if reply == 'q':
    sys.exit()
    print("Missing goods?")
#        reply1 = input()
if reply == 'N' or "NO":
    sys.exit()
elif reply == 'y' or "yes":
    print("Please contact our agents @ nobmart@help.com")
