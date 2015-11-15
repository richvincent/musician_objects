class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")


class Bassist(Musician):
    # The Musician class is the parent of the Bassist class

    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sponing, splang")


class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["wham", "diddle", "wham", "diddle"])

    def count(self):
        print(
            """\t\t\ta one\n
            and a two\n
            and a three\n
            and a four"""
        )

    def spontaneouslyCombust(self):
        print(
            """\t\t\tYou bloody well need a new guitariest\n
            Because I'm about to catch fire!!!!\n"""
        )

        try:
            raise NameError("I've Combusted")
        except NameError:
            print("I smell combustion!")
            raise


class Band(object):
    def __init__(self):
        # Request that the new band be given a name
        self.members = dict(drummer='', bassist='', guitarist='')
        self.bandName = ''
        while self.bandName == '':
            self.bandName = input('Please select a band name: ')

    def addMember(self, memberName, instrument):
        print(memberName)
        print(instrument)
        instrument.lower()
        while instrument not in list(self.members.keys()):
            instrument = input('This band only needs a drummer[d], guitariest\
                        [g], or a bassist[b] please choose one: ').lower()
            if instrument == 'd':
                instrument = 'drummer'
            if instrument == 'g':
                instrument = 'guitarist'
            if instrument == 'b':
                instrument = 'bassist'

        if instrument == 'drummer':
            self.drummer = Drummer()
            self.drummer.name = memberName
            self.members['drummer'] = self.drummer
        elif instrument == 'guitarist':
            self.guitarist = Guitarist()
            self.guitarist.name = memberName
            self.members['guitarist'] = self.guitarist
        elif instrument == 'bassist':
            self.bassist = Bassist()
            self.bassist.name = memberName
            self.members['bassist'] = self.bassist

    def fireMember(self, memberName):
        if (memberName in [self.drummer.name, self.guitarist.name,
                           self.bassist.name]) == True:
            locator = [self.drummer.name, self.guitarist.name,
                       self.bassist.name].index(memberName)
            if locator == 0:
                self.members["drummer"] = ''
                self.drummer = ''
            elif locator == 1:
                self.members["guitarist"] = ''
                self.guitarist = ''
            elif locator == 2:
                self.members["bassist"] = ''
                self.bassist = ''
        else:
            print("This musician {} does not work here!".format(memberName))
            print("The current band members are {drummer}, {guitarist}, and\
                  {bassist}".format(drummer=self.drummer.name,
                                    guitarist=self.guitarist.name,
                                    bassist=self.bassist.name))
