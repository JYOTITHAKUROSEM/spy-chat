
current_status_message = []
from Spydetail import spy,Spy,ChatMessage,friends
from steganography.steganography import *
from datetime import datetime
from colorama import Style,Fore,init
import  sys
STATUS_MESSAGES = ['My name is Jyoti,  jyotithakur','Keeping the British end up, Sir']
#from Addfriend import add_friend  #show_menu = False
#from Spydetail import spy
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name
    if spy.age>12 and spy.age<50:
        sys.stdout.write (Fore.BLACK+"Authentication complete. Welcome "+Fore.RED+"%s" %(spy.name))
        print Fore.BLACK+"of age %d and rating of %f "%(spy.age,spy.rating)
    show_menu = True
    while show_menu:
      menu_choices =Fore.BLACK+ "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application " \

      print(Style.RESET_ALL)
      menu_choice = int(raw_input(menu_choices))
      if menu_choice == 1:
         print 'You chose to update the status'
         spy.current_status_message=add_status(current_status_message)
      elif menu_choice == 2:
           number_of_friends= add_friend()
           print "you have %d friends"%(number_of_friends)
      elif menu_choice == 3:
          send_message()
      elif menu_choice==4:
          read_message()
      elif menu_choice==5:
          read_chat_history()
#Add Status
def add_status(current_status_message):

    if spy.current_status_message != None:
        print Fore.BLACK+'Your current status message is %s \n' % (current_status_message)
        print Style.RESET_ALL
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message
#Add Friend
def add_friend():
    new_friend = Spy("","",0,0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.age= int (raw_input("enter your friend age:\n"))
    new_friend.rating=float(raw_input("enter your friends rating:\n"))

    if len(new_friend.name)>0 and 12 < new_friend.age<50 and spy.rating<=new_friend.rating<=5.0:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)
def select_a_friend():
    item_number = 1

    for friend in friends:
        print ('%d. %s %s age %d is rated %.2f' %( item_number, friend.name,friend.salutation, int(friend.age), float(friend.rating)))
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#Send message
def send_message():

    friend_choice = select_a_friend()
    original_image=raw_input("what is the name of the image")
    output_path = raw_input("enter output path")
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print Fore.BLUE+"Your secret message image is ready!"
#Read message
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)
    new_chat=ChatMessage(secret_text ,False)
    friends[sender].chats.append(new_chat)

    print (secret_text)
#Read chat history
def read_chat_history():
    read_for=select_a_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print(Fore.BLUE+ "[%s]%s:%s"%(chat.time.strftime("%d,%B,%Y"),"You said:",chat.message))
        else:
           print(Fore.CYAN+"[%s]%s:%s"%(chat.time.strftime("%d,%B,%Y"),friends[read_for].name,chat.message))







