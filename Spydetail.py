# spy_name="jyoti"
# spy_age=20
# spy_rating=4.5
# spysalutation='Ms.'
# spy_is_online=True
from datetime import datetime
class Spy:
    def __init__(self,name,salutaion,age,rating):
       self.name = name
       self.salutation = salutaion
       self.age = age
       self.rating = rating
       self.chats =[]
       self.current_status_message=None

class ChatMessage:
      def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)
friend1= Spy('jyoti','ms', '21', '4')
friend2= Spy('sudiksha','ms', '21', '5')
friend3=Spy('komal','ms','20','6')
friends = [friend1,friend2,friend3]




# friends=[
#     {
#         'name':'jyoti',
#         'saluatation':'ms',
#         'rating':32,
#         'age': 21,
#         'chats':[]
#      },
#     {
#         'name':'sudi',
#         'saluatation':'ms',
#         'rating':31,
#         'age': 20,
#         'chats':[]
#     }
# ]
# spy = {
#     'name': 'bond',
#     'salutation': 'Mr.',
#     'age': 24,
#     'rating': 4.7,
#     'is_online': True
#
# }
