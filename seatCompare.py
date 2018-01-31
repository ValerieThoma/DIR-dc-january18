yesterday_seat_assignments = [
    "Moses",
    "Ken",
    "Terry",
    "David",
    "Nick",
    "Itzik",
    "Jaehee",
    "Illia"
];


today_seat_assignments = [
    "Nick",
    "Ashely",
    "Ken",
    "Joel",
    "Aaron",
    "Jaehee",
    "Moses",
    "Chris"
];

if today_seat_assignments[0] == yesterday_seat_assignments[0]:
    print "Hey, %s can't sit here!" % today_seat_assignments[0];
else: 
    print "Cool, you can sit there!";

i = 0
seat_count = len(today_seat_assignments)
while i < seat_count:
    print today_seat_assignments[i]
    i += 1
print "We're done!";    
#    OR write it like this
# indicies = [0,1,2,3,4,5,6,7]
# indicies = range(0,8);
# for i in range(0, len(today_seat_assignments)):
#     if today_seat_assignments[i] == yesterday_seat_assignments[i]
#         print "Hey, %s can't sit there!" % today_seat_assignments[i]
#     else:
#         print "Cool, you can sit there";    
    
