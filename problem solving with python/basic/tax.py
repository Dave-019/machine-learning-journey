product_price = int (input('enter product price: '))

gsct = 0.09 * product_price
ssct = 0.09 * product_price 

final_price = product_price + gsct + ssct

print("final price =",final_price)