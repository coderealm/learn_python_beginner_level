# file name: example_528.py

class Team:

    def __init__(self, members):

        self.members = members

    def __len__(self):

        return len(self.members)

team = Team(["Alice", "Bob"])

print(len(team))
