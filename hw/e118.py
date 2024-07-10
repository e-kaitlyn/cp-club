import random
def creatdeck():
    deck =[]
    sv= ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    dv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    hv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    cv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    s=h=d=c=13
    for i in range(52):
        card = ""
        suits = ['s','h','d','c']
        if s ==0:suits.remove("s")
        if h ==0:suits.remove("h")
        if d ==0:suits.remove("d")
        if c ==0:suits.remove("c")

        suit = random.choice(suits)
        if suit == "s":
            value = random.choice(sv)
            card+=value+"s"
            sv.remove(value)
            s-=1
        if suit == "h":
            value = random.choice(hv)
            card+=value+"h"
            hv.remove(value)
            h-=1
        if suit == "d":
            value = random.choice(dv)
            card+=value+"d"
            dv.remove(value)
            d-=1
        if suit == "c":
            value = random.choice(cv)
            card+=value+"c"
            cv.remove(value)
            c-=1
        deck.append(card)
    return(deck)


print(creatdeck())

