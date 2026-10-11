#Price & Quantity of items
price_pen = 10
quan_pen = 5
total_pen = price_pen*quan_pen

price_ball = 60
quan_ball = 3
total_ball = price_ball*quan_ball

price_book = 55
quan_book = 12
total_book = price_book*quan*book

#Calculate subtotal
subtotal = total_pen + total_ball + total_book

#Apply 10% discount if subtotal is 1000rs or more
if subtotal >= 1000 :
    disc_price = subtotal * (10/100)
    print("Discount Price : ",disc_price)

#Display final bill


