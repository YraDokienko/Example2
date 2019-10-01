class Player():

    def __init__(self, name, power, skill, health):
        self.name = name
        self.power = power
        self.skill = skill
        self.health = health

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def get_skill(self):
        return self.skill

    def set_health(self, new_health):
        self.health = new_health

    def show_player(self):
        print("Герой - {}\n HP: = {}\n".format(self.name, self.health))
