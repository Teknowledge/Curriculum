# my first floor is your second floor

hotelGuests = [
  ["Rob", "Lars", "-"],
  ["Sam", "-", "Yak"]
]

prices = [
  [95, 0, 85],
  [115, 190, 125]
]

def lookUpGuestFromRoom(floorNumber, roomNumber):
  return hotelGuests[floorNumber][roomNumber]

def lookUpRoomFromGuest(guestName):
  for floorNumber in range(len(hotelGuests)):
    for roomNumber in range(len(hotelGuests[0])):
      print("Checking floor:", floorNumber)
      print("and room:", roomNumber)
      print("The guest here is:", "your code here")


print(lookUpGuestFromRoom(0, 0))
print(lookUpGuestFromRoom(0, 1))

# Challenge 1.0 - Right now we print out "Rob" and "Sam". Add two more prints
#    using the function lookUpGuestFromRoom() to also print "Lars" and "Yak".

# Challenge 1.1 - Replace "your code here" in lookUpRoomFromGuest() to actually
#    print what guest is at that floorNumber and roomNumber.

# Challenge 1.2 - Make lookUpRoomFromGuest return a list that is the correct
#    [floorNumber, roomNumber] corresponding to the guestName. Check it with:
#      print(lookUpRoomFromGuest("Yak"))
#    If no guest exists, return None.  You can delete the prints also.

# Challenge 1.3 - Write a new function getPriceForGuest(guestName) that takes a
#    string of a guest's name who is in the hotel and returns the corresponding
#    price from the prices list.
#    Hint: feel free to use your function lookUpRoomFromGuest!

# BONUS Challenge 1.4 - Write a function getTotalProfit(hotelGuests, prices)
#    that returns the total money made from all the guests in the hotel.
#    (Empty rooms, marked with "-", don't make any profit.)
#    Try testing the function with new lists of lists for the hotelGuests and
#    the prices, but with three floors!
