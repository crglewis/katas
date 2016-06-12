#Change to Accept Input

# 1, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A
# C, D, H, S
inputBlack = "2H 3D 5S 9C KD"
inputWhite = "2C 3H 4S KC AH"

def pokerHands(inputBlack, inputWhite):

    whiteCards = getCards(inputBlack)
    blackCards = getCards(inputWhite)

    scoreCards(blackCards, whiteCards)
    

def getCards (input):
    
    card1 = convertToInt(input[0:2])
    card2 = convertToInt(input[3:5])
    card3 = convertToInt(input[6:8])
    card4 = convertToInt(input[9:11])
    card5 = convertToInt(input[12:14])
    
    hand = []
    hand.append(card1)
    hand.append(card2)
    hand.append(card3)
    hand.append(card4)
    hand.append(card5)
       
    return sorted(hand)

def convertToInt(inputString):

        card = []

        if (inputString[0] == "T"):
            card.append(10)
            card.append(inputString[1])
        elif (inputString[0] == "J"):
            card.append(11)
            card.append(inputString[1])
        elif (inputString[0] == "Q"):
            card.append(12)
            card.append(inputString[1])
        elif (inputString[0] == "K"):
            card.append(13)
            card.append(inputString[1])
        elif (inputString[0] == "A"):
           card.append(14)
           card.append(inputString[1])

        print (card)
        return card

def scoreCards(blackCards, whiteCards):

    ## Use ASCII math????
    ## Score Black Cards

    pair1 = pair(blackCards)
    pair2 = pair(whiteCards)
    
    if(pair1 > pair2):
        print("Black Hand Wins")
    elif(pair1 < pair2):
        print("White Hand Wins")
    """ Finish Tie breaker"""
        

    ## Score White Cards

'''
  2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked by the value of the cards forming the pair.
  If these values are the same, the hands are ranked by the values of the cards not forming the pair, in decreasing order.
'''
def pair(cards):

    clubs = 0
    diamonds = 0
    hearts = 0
    spades = 0

    pairCards = []
    score = 0
    
    for card in cards:
        if (card[1] == "C"):
            clubs += 1
            pairCards.append(card)
        elif (card[1] == "D"):
            diamonds += 1
            pairCards.append(card)
        elif (card[1] == "H"):
            hearts += 1
            pairCards.append(card)
        elif (card[1] == "S"):
            spades += 1
            pairCards.append(card)

    if (clubs > 1):
        card1 = pairCards[0]
        card2 = pairCards[1]

        score = card1[0] + card2[0]
        
    return score
           
'''
  The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the value of their highest pair.
  Hands with the same highest pair are ranked by the value of their other pair. If these values are the same the hands are ranked by the value of the remaining
  card.
'''
##def twoPair(cards):

'''
  Three of the cards in the hand have the same value. Hands which both contain three of a kind are ranked by the value of the 3 cards.
'''
##def threeOfKind(cards):

'''
  Hand contains 5 cards with consecutive values. Hands which both contain a straight are ranked by their highest card.
'''
##def straight(cards):

'''
  Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the rules for High Card.
'''
##def flush(cards):

'''
  3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the value of the 3 cards.
'''
##def fullHouse(cards):

'''
  4 cards with the same value. Ranked by the value of the 4 cards.
'''
##def fourOfKind(cards):

'''
5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.
'''
##def straightFlush(cards):

pokerHands(inputBlack, inputWhite)













