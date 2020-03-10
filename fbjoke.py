
#Note: First install fbchat in python. you can sin simply do that by "pip install fbchat".
import fbchat
from fbchat import Client
from time import sleep
class fbchatter:
    __username=""#your fb username inside ""
    getpassfile = open("getpass.txt","rb") #make a new getpass.txt file in your project folder and save your fb password in it 
    __password = getpassfile.read()#Just to ensure you haven't shown your password
    # ses = ""  for the session you can check down below
    client = ""
    friends = ""
    friend = ""
    msg = ""
    sent = ""
    rcvdmsgs = ""
    rcvdmsg = ""
    dmsg = ""
    stime=""
    def __init__(self): 
        # print("Welcome user")
        # sleep(3) 
        # print("Let's login first")
        # sleep(3)
        self.client = fbchat.Client(self.__username,self.__password)
        self.friends = self.client.searchForUsers("")#either you wanna send to one friend or multiple that depends, if you want to sned to one friend insert their usernamee inside""
        self.friend = self.friends[0]#this is to assign the first username because above variable is in list, you can also send to multiple friends by looping

        #Note: I also haven't made any session because you need to check every often, so if you want you can easily make session and don't forget to log out at the end
        # self.ses=client.getSession() this is session


        self.msg = "Hey! how are you?"
        print("Sending Message")
        self.sent = self.client.send(fbchat.models.Message(self.msg), self.friend.uid)
        if self.sent:
            print("Message sent successfully")

        
        self.rcvdmsgs = self.client.fetchThreadMessages(self.friend.uid, 1) #this will check the recieved messages the latest one
        self.rcvdmsgs.reverse()
        self.rcvdmsg = self.rcvdmsgs[0]
        self.dmsg = self.rcvdmsgs[0]
        print(self.rcvdmsg.text)
        print(self.dmsg.text)
        sleep(4)
        while 1: #Note: you can also get fbchat onMessage() function to listen the coming message but I made this because it's simple
            if self.rcvdmsg.author == self.dmsg.author: #here's the main thing to check out the condition, in a conversation there's always a two autor one is you and another your friend
                self.rcvdmsgs = self.client.fetchThreadMessages(self.friend.uid, 1)
                self.rcvdmsgs.reverse()
                self.rcvdmsg = self.rcvdmsgs[0]
            else:
                sleep(15)
                self.msg = "I am little bit bored can you tell me a joke pls"
                print("Sending Message")
                self.sent = self.client.send(fbchat.models.Message(self.msg), self.friend.uid)
                if self.sent:
                    print("Message sent successfully")
                
                self.rcvdmsgs = self.client.fetchThreadMessages(self.friend.uid, 1)
                self.rcvdmsgs.reverse()
                self.rcvdmsg = self.rcvdmsgs[0]
                self.dmsg = self.rcvdmsgs[0]
                print(self.rcvdmsg.text)
                print(self.dmsg.text)
                sleep(4)
                while 1:
                    if self.rcvdmsg.author == self.dmsg.author:
                        self.rcvdmsgs = self.client.fetchThreadMessages(self.friend.uid, 1)
                        self.rcvdmsgs.reverse()
                        self.rcvdmsg = self.rcvdmsgs[0]
                    else:
                        sleep(10)
                        self.stime = 10
                        self.rcvdmsgs = self.client.fetchThreadMessages(self.friend.uid, 1)
                        self.rcvdmsgs.reverse()
                        self.rcvdmsg = self.rcvdmsgs[0]
                        print(self.rcvdmsg.text)
                        print(self.dmsg.text)

                        if len(self.rcvdmsg.text) > 0 and len(self.rcvdmsg.text) < 20:
                            print("Sending Message") 
                            self.sent = self.client.send(fbchat.models.Message("Please :("), self.friend.uid)
                            sleep(self.stime)
                            self.stime = self.stime + 5
                        else:
                            print("Sending picture") 
                            sleep(4)
                            self.client.sendLocalImage(".jpg", fbchat.models.Message(""), self.friend.uid)#this will send the pictures
                            if self.sent:
                                print("picture sent successfully")
                            break
                break
            #Note: theres only two if and else, you can do multiple of them just check there's multiple other break to break down infinte loop
            # client.logout();
        
obj = fbchatter()

