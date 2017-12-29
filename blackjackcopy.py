import requests
import json 

   
#r = requests.get("http://deckofcardsapi.com/api/deck/new/draw/shuffle/?count=52")


r = requests.get("http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1") 

deckRequest = json.loads(r.content)

#print r.content 

print ""

deckId =  deckRequest['deck_id']
 

totalVal = 0

#decId = "ixlam6j2sycp"

Request = "http://deckofcardsapi.com/api/deck/%s/draw/?count=2" % deckId

#r2 = requests.get(deckRequest)

r2 = requests.get(Request)



print ''
#print r2.content

yourCards = {} 

yourCards = json.loads(r2.content)
myValue = 0

newCard = 0

for card in yourCards['cards']: 
  print card['value']
  global totalVal 
  if card['value'] in ('2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10'): 
    myValue = myValue + int(card['value'])
    print "My value: %s" % myValue 
  elif card['value'] in ('QUEEN', 'KING', 'JACK'):
    myValue = myValue + 10 
    print "My value: %s" % myValue
  elif card['value'] == 'ACE': 
    myValue = myValue + 11 
    print "My value: %s" % myValue 
  totalVal = myValue 
  print "TotalVal: %s" % totalVal

print '' 


#Dealers cards 
dealerRequest = "http://deckofcardsapi.com/api/deck/%s/draw/?count=2" % deckId
r3 = requests.get(dealerRequest)
dealerCards = {}
dealerCards = json.loads(r3.content)
newDealerCards = 0
dealerTotalValue = 0
dealerValue = 0 

print "Dealers first cards: %s of %s" % (dealerCards['cards'][0]['value'],  dealerCards['cards'][0]['suit'])

print ''

for card in dealerCards['cards']: 
  #print card['value']
  global dealerTotalVal 
  global dealerValue 
  if card['value'] in ('2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10'): 
    dealerValue = dealerValue + int(card['value'])
    #print "Dealer value: %s" % dealerValue 
  elif card['value'] in ('QUEEN', 'KING', 'JACK'):
    dealerValue = dealerValue + 10 
    #print "Dealer value: %s" % dealerValue
  elif card['value'] == 'ACE': 
    dealerValue = dealerValue + 11 
    #print "Dealer value: %s" % dealerValue 
  dealerTotalVal = dealerValue 
  #print "Dealer Total Val: %s" % totalVal 

print dealerCards
print dealerValue 


while totalVal < 21: 
  singleCard = "http://deckofcardsapi.com/api/deck/%s/draw/?count=1" % deckId
  singleRequest = requests.get(singleCard)
  singleReqJSON = {}
  singleReqJSON = json.loads(singleRequest.content)
  userInput = raw_input('Hit or Stay: ')
  userInput =  userInput.upper()
  if userInput == 'HIT': 
    print "Hit"
    
    print singleReqJSON['cards']

    for card in singleReqJSON['cards']:  
      print card['value']
      global totalVal 
      if card['value'] in ('2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10'): 
        myValue = myValue + int(card['value'])
        print "My value: %s" % myValue 
      elif card['value'] in ('QUEEN', 'KING', 'JACK'):
        myValue = myValue + 10 
        print "My value: %s" % myValue
      elif card['value'] == 'ACE': 
        myValue = myValue + 11 
        print "My value: %s" % myValue 
      totalVal = myValue 
      print "TotalVal: %s" % totalVal 
    if totalVal > 21: 
      print "Sir you have exceeded 21"
    
  else: 
    print 'Stay'
    break 
  print "TotalVal: %s" % totalVal

print "TotalVal: %s" % totalVal

if totalVal <= 21:  
  if totalVal > dealerTotalVal: 
    print "You win."
  else: 
    print "Dealer wins."

print ''
print 'Your value: %s' % totalVal

print ''
print 'Dealer value: %s' % dealerTotalVal 
print 'Dealers first card: %s of %s' % (dealerCards['cards'][0]['value'], dealerCards['cards'][0]['suit'])
print 'Dealers second card: %s of %s' % (dealerCards['cards'][1]['value'], dealerCards['cards'][1]['suit'])





'''

dealtCards = {}

counter = 0 
length =  len(cards['cards'])

while counter < length: 
  
  cardName = "card " + str(counter)
  code = cards['cards'][counter]['code']
  dealtCards[cardName] = [code]
  #print cardName
  #print code
  counter += 1 

print dealtCards
'''

