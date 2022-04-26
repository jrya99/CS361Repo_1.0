from PurplePanda.parent import Parent


class TA(Parent):
    def __init__(self, username=None, password=None):
        pass

    def view_assignments(self,assignments=None):
       # Precondition: assignment is existing
       # Postcondition: TA can now see the assignments
       # of theirs and other TA’s
       # Side - effects: none
       if assignments is not None:
           for x in assignments:
               print(x)


    def obtain_contact_info(self, username=None):
        # Precondition: information is available to read
        # Postcondition: software is displaying the information to
        # screen
        # Side - effects: none
        if username is not None:
            self.print_contact_info(username)


    def get_username(self):
        return self.username

    def set_username(self, username=None):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password=None):
        self.password = password