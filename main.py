import random

class Mage:
    def __init__(self, nom, pv, manaM):
        self.__name = nom
        self.__health = pv
        self.__manaMax = manaM 
        self.__currentMana = manaM
        self.__hand = [] 
        self.__gameCard = [] 
        self.__gameCardSize = 0
        self.__discard = []
        self.__discardSize = 0
        self.__deck = []
        self.__deckSize = 0
        self.__availableCase = 0

    def getName(self) :
        return self.__name

    def getHealth(self) :
        return self.__health

    def getManaMax(self) :
        return self.__manaMax

    def getCurrentMana(self) :
        return self.__currentMana

    def gainMana(self) :
        self.__currentMana = self.__manaMax

    def changeMana(self, change) :
        self.__currentMana = self.__currentMana + change

    def changeHealth(self, change) :
        self.__health = self.__health + change

    def drawCard(self) :
        self.__hand.append(self.__deck.pop())

    def playCard(self, choose) :
        if(self.__availableCase < 5) :
            self.__gameCard.append(choose)
            self.__availableCase = self.__availableCase + 1
            self.__hand.pop(choose)
        else :
            return "Impossible"

    def showHand(self, choose) :
        return self.__hand[choose]

    def showCimetery(self, choose) :
        return self.__discard[choose]

    def showPlayed(self, choose) :
        return self.__gameCard[choose]

    def deckMaking(self, card) :
        self.__deck.append(card)

    def deckShuffle(self):        
        random.shuffle(self.__deck)

class Carte(Mage):
    def __init__(self, coutMana, nom, desc):
        self.__manaUse = coutMana
        self.__name = nom
        self.__description = desc

    def getMana(self) :
        return self.__manaUse

    def getName(self) :
        return self.__name

    def getDescription(self) :
        return self.__description

    def goToCimetery(self, choose) :
        self.__discard.append(choose)
        self.__gameCard.pop(choose)
        self.__availableCase = self.__availableCase - 1

class Blast(Carte):
    def __init__(self, cost, name, desc, dmg):
        Carte.__init__(self, cost, name, desc)
        self.__damage = dmg

    def damageBlast(self) :
        return self.__damage

class Creature(Carte):
    def __init__(self, valeur, name, desc, pv, charge):
        Carte.__init__(self, valeur, name, desc)
        self.__lifePoint = pv
        self.__atk = charge
        self.__hasCharged = False        

    def getAtk(self) :
        if(self.__hasCharged == True) :
            return "impossible"
        else :
            return self.__atk

    def hasPlayed(self) :
        if(self.__hasCharged == False) :
            self.__hasCharged = True
        else :
            self.__hasCharged = False

    def pvChange(self, change) :
        self.__lifePoint = self.__lifePoint + change

    def getPv(self) :
        return self.__lifePoint


class Cristal(Carte):
    def __init__(self, manaCost, name, desc, manaMaxPlus):
        Carte.__init__(self, manaCost, name, desc)
        self.__value = manaMaxPlus

    def changeManaMax(self) :
        self.__manaMax = self.__manaMax + self.__value

    def getValue(self) :
        return self.__value

joueur1 = Mage("Benoit",25,10)
joueur2 = Mage("Albert",25,10)

card1 = Cristal(6, "Cristal de terre", "Ce cristal se plante dans la terre avant de redistribuer son énergie, il rapporte 3 mana supplémentaire", 3)
card2 = Blast(2, "Vague de glace", "Une explosion de glace vient frapper l'adversaire", 4)
card3 = Creature(1, "Slime nul", "Ce n'est qu'un pauvre slime", 1, 1)

for i in range(3) :
    joueur1.deckMaking(card1)
    joueur1.deckMaking(card2)
    joueur1.deckMaking(card3)

joueur1.deckShuffle()
joueur1.drawCard()
print(joueur1.showHand(0).getName())
print("La carte coûte",joueur1.showHand(0).getMana())
print("Description :",joueur1.showHand(0).getDescription())
if(isinstance(joueur1.showHand(0),Creature)) :
    print("Attaque", joueur1.showHand(0).getAtk())
    print("Pv", joueur1.showHand(0).getPv())
if(isinstance(joueur1.showHand(0),Blast)) :
    print("Inflige",joueur1.showHand(0).damageBlast())

