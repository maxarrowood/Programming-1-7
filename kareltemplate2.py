from stanfordkarel import *


class ktools:

    def m(self):
        """Shorthand for Move"""
        move()

    def tl(self):
        """Turn Left"""
        turn_left()

    def tr(self):
        """Turn Right"""
        self.tl()
        self.tl()
        self.tl()

    def ta(self):
        """Turn Around"""
        self.tl()
        self.tl()

    def pick(self):
        """Pick Beeper"""
        pick_beeper()

    def put(self):
        """Put Beeper"""
        put_beeper()

    def put2(self):
        """Put 2 Beepers"""
        self.put()
        self.m()
        self.put()

    def put5(self):
        """Put 5 Beepers"""
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()

    def h(self):
        """Print H w/ Beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def e(self):
        """Print E w/ Beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.tr()
        self.m()
        self.m()
        self.tr()
        self.put2()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.m()

    def l(self):
        self.tl()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.m()

    def o(self):
        self.l()
        self.ta()
        self.m()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.l()


def main():
    """ Karel code goes here! """
    kt = ktools()

    pass


if __name__ == "__main__":
    run_karel_program()
