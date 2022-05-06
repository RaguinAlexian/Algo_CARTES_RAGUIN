class Mage:
    def __init__(self, nom, pv, manaM):
        self.__name = nom
        self.__health = pv
        self.__manaMax = manaM 
        self.__currentMana = manaM
        self.__hand = [] 
        self.__gameCard = [] 
        self.__discard = []
        self.__deck = []
        self.__availableCase = 0

    def getName(self) :
        return self.__name

    def gainMana(self) :
        self.__currentMana = self.__manaMax

    def changeMana(self, change) :
        self.__currentMana = self.__currentMana + change

    def playCard(self, choose) :
        if(self.__availableCase < 5) :
            self.__gameCard.append(choose)
        else :
            return "Impossible"
        self.__hand.pop(choose)

    def getHealth(self) :
        return self.__health

    def changeHealth(self, change) :
        self.__health = self.__health + change

    def showHand(self) :
        for i in range() :
            return self.__hand[i]

class Carte(Mage):
    def __init__(self, coutMana, nom, desc):
        self.__manaUse = coutMana
        self.__name = nom
        self.__description = desc

    def getMana(self) :
        return self.__manaUse

    def getName(self) :
        return self.__name

    def getDescrition(self) :
        return self.__description

    def goToCimetery(self, choose) :
        self.__discard.append(choose)
        self.__gameCard.pop(choose)

class Blast(Carte):
    def __init__(self, dmg):
        self.__damage = dmg

    def targetBlast(self) :
        return self.__damage

class Creature(Carte):
    def __init__(self, pv, charge):
        self.__lifePoint = pv
        self.__atk = charge
        self.__hasCharged = False

    def targetAtk(self) :
        if(self.__hasCharged == True) :
            return "impossible"
        else :
            self.__hasCharged = True
            return self.__atk

    def pvChange(self, change) :
        self.__lifePoint = self.__lifePoint + change

    def getPv(self) :
        return self.__lifePoint


class Cristal(Carte):
    def __init__(self, manaMaxPlus):
        self.__value = manaMaxPlus

    def changeManaMax(self) :
        self.__manaMax = self.__manaMax + self.__value