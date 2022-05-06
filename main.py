import random

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

    def getHealth(self) :
        return self.__health

    def getManaMax(self) :
        return self.__manaMax

    def getCurrentMana(self) :
        return self.__currentMana

    def getCard(self) :
        self.__hand.append(self.__deck.pop())

    def gainMana(self) :
        self.__currentMana = self.__manaMax

    def changeMana(self, change) :
        self.__currentMana = self.__currentMana + change

    def changeHealth(self, change) :
        self.__health = self.__health + change

    def playCard(self, choose) :
        if(self.__availableCase < 5) :
            self.__gameCard.append(choose)
            self.__availableCase = self.__availableCase + 1
            self.__hand.pop(choose)
        else :
            return "Impossible"

    def showHand(self) :
        for i in range(len(self.__hand)) :
            return self.__hand[i]

    def showCimetery(self) :
        for i in range(len(self.__discard)) :
            return self.__discard[i]

    def showPlayed(self) :
        for i in range(len(self.__gameCard)) :
            return self.__gameCard[i]

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
        self.__availableCase = self.__availableCase - 1

class Blast(Carte):
    def __init__(self, dmg):
        self.__damage = dmg

    def damageBlast(self) :
        return self.__damage

class Creature(Carte):
    def __init__(self, pv, charge):
        self.__lifePoint = pv
        self.__atk = charge
        self.__hasCharged = False

    def getAtk(self) :
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

    def getValue(self) :
        return self.__value

class Shuffle(Carte):

    def deckShuffle(self):        
        random.shuffle(self.__deck)