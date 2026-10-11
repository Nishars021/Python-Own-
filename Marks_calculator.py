#MArks in 5 subjects
sub1 = 30
sub2 = 90
sub3 = 20
sub4 = 96
sub5 = 76

#Total & Average
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total/5

#Percentage 
perc = (total/500) * 100

#Display Pass or Fail
if sub1 >= 35 :
    print("Pass in subject 1")
else :
    print("Fail in subject 1")

if sub2 >= 35 :
    print("Pass in subject 2")
else :
    print("Fail in subject 2")

if sub3 >= 35 :
    print("Pass in subject 3")
else :
    print("Fail in subject 3")
    
if sub4 >= 35 :
    print("Pass in subject 4")
else :
    print("Fail in subject 4")

if sub5 >= 35 :
    print("Pass in subject 5")
else :
    print("Fail in subject 5")

#Display grade
if perc >= 90 : 
   print ("Grade : A" )

if perc >= 80 and perc <= 89 : 
   print ("Grade : B")

if perc >= 70 and perc <= 79 : 
   print ("Grade : C")

if perc >= 60 and perc <= 69 : 
   print ("Grade : D")

if perc >= 35 and perc <= 59 : 
   print ("Grade : E")

if perc < 35 : 
   print ("Grade : F")