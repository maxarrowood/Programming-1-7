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
        self.ta()
        self.m3()
        self.m()
        self.m()
        self.tr()
        self.m3()
        self.m()
        self.tr()
        self.ta()
        self.m()

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

    def one(self):
        kt.tl()
        kt.mm(5)
        kt.ta()
        kt.put5()
        kt.tl()
        kt.mm(2)

    def fic(self) -> bool:
        """Front is Clean"""
        return front_is_clear()

    def fib(self) -> bool:
        """Front is Blocked"""
        return not self.fic()

    def ric(self) -> bool:
        """Right is Clear"""
        self.tr()
        if self.fic():
            self.tl()
            return True  #return signals end of function
        self.tl()
        return False

    def rib(self) -> bool:
        return not self.ric()

    def mazemove(self):
        """Maze Move"""
        if self.fib():
            self.tl()
        else:
            self.m()
            if self.ric():
                self.tr()
                self.m()
                if self.ric():
                    self.tr()
                    self.m()
        pass

    def mm(self, num):
        """Move Multiple"""
        for number in range(0, num):
            self.m()

    def putm(self, num):
        """Put Multiple"""
        for i in range(num - 1):
            self.put()
            self.m()
        self.put()

    def pickm(self, num):
        """Pick Multiple"""
        for _ in range(num - 1):
            self.pick()
            self.m()
        self.pick()

    def SOB(self) -> bool:
        """Standing on Beeper"""
        return beepers_present()

    def jump(self):
        """Jump for 510"""
        while self.fic():
            self.m()
        self.tl()
        while self.rib():
            self.m()
        self.tr()
        self.m()
        self.tr()
        while self.fic():
            self.m()
        self.tl()

    def find(self):
        """Find for 515"""
        while not facing_north():
            self.tl()
            self.m()
            self.tl()
            self.m()
        for _ in range(2):
            if not self.SOB():
                self.m()
                self.tl()
                self.m()


def main():
    """ Karel code goes here! """
    kt = ktools()

    kt.m()
    kt.tl()
    kt.mm(3)
    kt.tr()
    kt.mm(3)
    kt.tr()
    kt.mm(3)
    kt.tl()
    kt.mm(2)
    kt.tl()
    kt.mm(8)
    kt.tr()
    kt.mm(2)
    kt.tr()
    kt.mm(8)
    kt.tl()
    kt.m()
    kt.tr()
    kt.mm(5)
    kt.tr()
    kt.mm(7)
    kt.tr()
    kt.mm(5)
    kt.tl()
    kt.m()
    kt.tl()
    kt.mm(7)
    kt.tr()
    kt.m()
    kt.tr()
    kt.mm(7)
    kt.tl()
    kt.m
    kt.tl()
    kt.mm(4)
    kt.tr()
    kt.mm(2)
    kt.tr()
    kt.mm(2)
    kt.tl()
    kt.m()
    kt.pick()

    pass


if __name__ == "__main__":
    run_karel_program()
