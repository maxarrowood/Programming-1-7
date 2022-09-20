from stanfordkarel import *


class ktools:

    def m(self):
        """Shorthand for Move"""
        move()

    def m3(self):
        self.m()
        self.m()
        self.m()

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

    def printm(self):
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.tr()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.m()
        self.tr()
        self.m()
        self.tr()
        self.put5()
        self.tl()
        self.m()
        self.m()

    def a(self):
        self.tl()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.tl()
        self.m()
        self.m()

    def x(self):
        self.tl()
        self.put()
        self.m3()
        self.m()
        self.put()
        self.tr()
        self.m()
        self.tr()
        self.m()
        self.put()
        self.m()
        self.m()
        self.put()
        self.tl()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.m()
        self.tr()
        self.m()
        self.tr()
        self.put()
        self.m()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.m()
        self.tl()
        self.put()
        self.m3()
        self.m()
        self.put()
        self.ta()
        self.m3()
        self.m()
        self.tl()
        self.m()
        self.m()


def main():
    """ Karel code goes here! """
    kt = ktools()

    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tr()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tr()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tr()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()

    pass


if __name__ == "__main__":
    run_karel_program()
