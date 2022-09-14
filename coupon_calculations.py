'''
Program: coupon_calculations.py
Author: Joshua M. McGinley
Last date modified: 09/14/2022

You are online shopping at SuperAwesomeCouponDealsAndStuff.com. They offer two types of discounts, cash-off
coupons and percent discount coupons. You must add tax after applying coupons. If you have cash-off coupons,
those must be applied first, then apply the percent discount coupons on the pre-tax amount.
The following is the order of calculations:

    The first is cash-off coupons, that you earn by shoppings. You may apply one $5 or $10 cash off per order.
    The second is percent discount coupons for 10%, 15%, or 20% off.
    The third is tax
    The fourth is shipping according to the the following guidelines:

        up to $10 dollars, shipping is $5.95
        $10 and up to $30 dollars, shipping is $7.95
        $30 and up to $50 dollars, shipping is $11.95
        Shipping is free for $50 and over

In this program, prompt the user for the the amount of the purchase, the cash coupon, the percent coupon.
Then calculate and return the total order item.
For instance, you have $5 off and 30% coupons and your item is $15.99, you will first take

    $15.99 - $5.00 = $10.99.
    30% off $10.99 to get $7.69
    Add tax at 6% to get $8.15
    Add shipping cost before tax $5.95 to get $14.10

Do not forget to use variables and constants where appropriate. Using varialabes, the first line might look
like the following:

    cash_off_subtotal = price - cash_off

Name your file coupon_calculations.py.
'''
import constant

amount_of_purchase = float(input('Enter the amount of purchase: '))  #Get the amount_ofPurchase
coupon_amount = input('Enter cash-off coupon amount (either: $0, $5, or $10): ')  #Get cash-off coupon amount

#If then elif statements to set value of cash_off
if(coupon_amount == '0'):
    cash_off = 0
elif(coupon_amount == '5'):
    cash_off = 5
elif(coupon_amount == '10'):
    cash_off = 10
#cash_off_subtotal calculated by subtracting cash_off from amount_ofpurchase
cash_off_subtotal = amount_of_purchase - cash_off

#Print Total after cash off 'cash_off_subtotal' to the screen
print('Total after cash off ', end=' $')
print(f'{cash_off_subtotal: 5.2f}')


percent_discount = input('Enter percent discount coupon (either: none, 10%, 15%, or 20%): ') #Get percent_discount
                                                                                            #from user
#Set percent equal to %10, %15, %20, or none based on percent_discount
if(percent_discount == 'none'):
    percent = 1
elif(percent_discount == '10'):
    percent = .9
elif(percent_discount == '15'):
    percent = .85
elif(percent_discount == '20'):
    percent = .80

#Calculate discount_subtotal by multiplying cash_off_subtotal by percent
discount_subtotal = (cash_off_subtotal * percent)

#Print Total after coupon 'discount_subtotal'
print('Total after coupon', end=" $")
print(f'{discount_subtotal: 5.2f}')

#Determine shipping by comparing discount_subtotal
if(discount_subtotal <= 10):
    shipping = 5.95
elif(10 < discount_subtotal <= 30):
    shipping = 7.95
elif(30 < discount_subtotal <= 50):
    shipping = 11.95
elif(discount_subtotal > 50):
    shipping = 0.00

#Print shipping
#print('Shipping cost', end=' $')
print(f'Shipping cost ${shipping: 5.2f}')

#Calculate subtotal by multiplying discount_subtotal * constant.TAX
subtotal = discount_subtotal * constant.TAX

#Print The subtotal is 'subtotal'
print('The subtotal is', end=' $')
print(f'{subtotal: 5.2f}')

#Calculate total by adding subtotal and shipping
total = subtotal + shipping

#Print The total whis shipping is 'total'
print('The total with shipping is', end=' $')
print(f'{total: 5.2f}')

