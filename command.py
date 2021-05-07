class command:
    def __init__(self,message,prefix):
        self.message = message
        self.prefix = prefix
        self.messagesplit = str(message.content).split()
        self.command = self.messagesplit[0]
        if self.command[0] == self.prefix:
            self.check = True
        else:
            self.check = False
    def com(self):
        if self.check == True:
            if self.command == '!hi':
                return 'HELLO!!!!!'
            else:
                pass
        pass