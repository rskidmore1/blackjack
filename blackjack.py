import requests
import json
import time  


deckId = ''
myValue = 0
dealerVal = 0
dealerTotalValue = 0


def deckId():  #Requests deckId for game 
  global deckId

  r = requests.get("http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1") 

  deckRequest = json.loads(r.content)

  deckId =  deckRequest['deck_id']


def playerCards(): #Gets player cards for current deck ID 
  global deckId
  global yourCards 
  Request = "http://deckofcardsapi.com/api/deck/%s/draw/?count=2" % deckId
  
  r2 = requests.get(Request)

  yourCards = {} 

  yourCards = json.loads(r2.content)


def dealerCards(): #Get dealre cards for current deck ID 
  global deckId
  global dealersCards
  dealerRequest = "http://deckofcardsapi.com/api/deck/%s/draw/?count=2" % deckId
  r3 = requests.get(dealerRequest)
  dealersCards = {}
  dealersCards = json.loads(r3.content) 

def playerValue(yourCards): #Determines the value of players cards  
  global myValue 
  for card in yourCards['cards']: 
    #print card['value']
    global totalVal
    global myValue
    if card['value'] in ('2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10'):
      intVal = int(card['value']) 
      myValue = myValue + intVal
      time.sleep(0.5)
      print "My card: %s of %s" % (card['value'],  card['suit'])
    elif card['value'] in ('QUEEN', 'KING', 'JACK'):
      myValue = myValue + 10 
      time.sleep(0.5)
      print "My card: %s of %s" % (card['value'],  card['suit'])
    elif card['value'] == 'ACE': 
      myValue = myValue + 11 
      time.sleep(0.5)
      print "My card: %s of %s" % (card['value'],  card['suit'])
    totalVal = myValue 
    time.sleep(0.5)
    print "TotalVal: %s" % totalVal
    print ''

def dealerValue(dealersCards): #Determines the value of dealers cards
  global dealerVal
  
  for card in dealersCards['cards']: 
    #print card['value']
    global dealerTotalValue 
    global dealerVal 
    
  
    if card['value'] in ('2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10'):
      intVal =  int(card['value'])
      dealerVal = dealerVal + intVal
    elif card['value'] in ('QUEEN', 'KING', 'JACK'):
      dealerVal = dealerVal + 10 
    elif card['value'] == 'ACE': 
      dealerVal = dealerVal + 11 
    dealerTotalValue = dealerVal
  time.sleep(0.5)
  print '' 
  print "Dealers first cards: %s of %s" % (dealersCards['cards'][0]['value'],  dealersCards['cards'][0]['suit'])



def play(myValue, dealerTotalVal, dealersCards): #Takes values of dealer and players cards to play game  
  
  while totalVal < 21: 
    singleCard = "http://deckofcardsapi.com/api/deck/%s/draw/?count=1" % deckId
    singleRequest = requests.get(singleCard)
    singleReqJSON = {}
    singleReqJSON = json.loads(singleRequest.content)
    time.sleep(0.5)
    userInput = raw_input('Hit or Stay: ')
    userInput =  userInput.upper()
    if userInput == 'HIT': 
      time.sleep(0.5)
      print "Hit"
      print ''
      #print singleReqJSON['cards']

      for card in singleReqJSON['cards']:  
        print card['value']
        global totalVal 
        if card['value'] in ('2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10'): 
          myValue = myValue + int(card['value'])
          time.sleep(0.5)
          print "My value: %s" % myValue 
        elif card['value'] in ('QUEEN', 'KING', 'JACK'):
          myValue = myValue + 10 
          time.sleep(0.5) 
          print "My value: %s" % myValue
        elif card['value'] == 'ACE': 
          myValue = myValue + 11 
          time.sleep(0.5)
          print "My value: %s" % myValue 
        totalVal = myValue 
        time.sleep(0.5)
        print "TotalVal: %s" % totalVal 
        print ''
      if totalVal > 21: 
        time.sleep(0.5)
        print "Sir you have exceeded 21"
    
    else: 
      time.sleep(0.5)
      print 'Stay'
      break 
    print "TotalVal: %s" % totalVal


  print "TotalVal: %s" % totalVal

  if totalVal <= 21:  
    if totalVal > dealerTotalValue:
      time.sleep(0.5) 
      print "You win."
    else: 
      time.sleep(0.5)
      print "Dealer wins."
  print ''
  print "Dealers second card: %s of %s" % (dealersCards['cards'][1]['value'],  dealersCards['cards'][1]['suit'])
  print "Dealer Total Value: %s" % dealerTotalValue


deckId()
playerCards()
dealerCards()
playerValue(yourCards) 
dealerValue(dealersCards)
play(myValue, dealerTotalValue, dealersCards)


time.sleep(0.5)
print ''
print "Thanks for playing. Please play again soon -_-"
