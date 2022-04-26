from PurplePanda.parent import Parent


class Admin(Parent):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def create_class(self, class_id, class_name):
        pass

    def data_view(self):
        pass
