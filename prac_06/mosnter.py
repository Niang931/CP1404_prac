TEETH_THRESHOLD = 16
SCARY_COLOUR = 'red'

class Monster:
    """"Monster class knows everything about monster"""
    def __init__(self, name='Mike', number_of_teeth=0, colour='blue'):
        """"Initialize the monster attributes"""
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def is_scary(self):
        """Determine if a monster is scary based on number of teeth and colour"""
        return self.number_of_teeth > TEETH_THRESHOLD or self.colour == SCARY_COLOUR

    def __str__(self):
        """Convert object to string"""
        return f"{self.name} {self.number_of_teeth} {self.colour} {self.is_scary()}"

    def __repr__(self):
        """Developing and debugging purpose"""
        return f"({self.name} {self.is_scary()})"

m1 = Monster("Lucas",2, 'red')
m2 = Monster('Lea',20,'blue')
m3 = Monster('Poew', 15, 'green')
m4 = Monster('Osss', 13, 'red')
m5 = Monster('Ara', 12, 'black')

monsters = [m1,m2,m3,m4,m5]
scary_monsters = [monster.name for monster in monsters if monster.is_scary()]
# print(scary_monsters)


class User:
    """Represent user with all characteristics"""
    def __init__(self, name):
        """Initialize user attributes"""
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def give_taco(self, other_user):
        """Give taco to another user and gain point"""
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other_user.score += 1
        else:
            print("No more tacos left")

    def __str__(self):
        """Convert object to string"""
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"



