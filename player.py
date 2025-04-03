class Player:

    def __init__(self, client):
        self.client = client  # Interface client, managing the connection
        self.name = None

    def set_name(self, name):
        '''
            Choose a name
        '''
        self.name = name

