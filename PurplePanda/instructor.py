from PurplePanda.parent import Parent


class Instructor(Parent):
    lab_ta = [{}]

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        pass

    def assigning_ta(self, lab_id=None, username=None):
        if self.lab_ta is not None:
            if lab_id is not None:
                if username is not None:
                    for x in self.lab_ta:
                        if self.lab_ta[x] is not None:
                            self.lab_ta[x] = [{lab_id, username}]

    def view_assignments(self, assignments=[]):

        if assignments is not None:
            for x in assignments:
                print(x)


    def get_username(self):
        return self.username

    def set_username(self, username=None):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password=None):
        self.password = password
