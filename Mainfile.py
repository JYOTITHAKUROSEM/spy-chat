from function import send_message
from function import read_message
from Spydetail import friends,spy
from function import add_status,start_chat
from Addfriend import add_friend
print "Hello! Let\'s get started"
question =( "Do you want to continue with default user (Y/N)? ")
existing = raw_input(question)
if (existing == "Y"):
   start_chat(spy['name'],spy['age'],spy['rating'])
else:
    spy_name = raw_input("welcome to spy chat,tell me your name first")
    if len(spy_name) > 0:
        spysalutation = raw_input("should you call mr.or miss?:")
        spy_age = raw_input("what is your age")
        spy_age = int(spy_age)
        spy_rating = raw_input("what is your rating")
        spy_rating = float(spy_rating)
        spy_is_online = True
        print("you are add correct information")
        if spy_age > 12 and spy_age < 50:
            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
                spy_rating) + " Proud to have you onboard"
    else:
        print("please add valid spy name")
