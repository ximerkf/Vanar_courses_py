# Solving the situation when a client wants to pay for service
# - trying to pay by cash
# - trying to pay by cart
# - trying to pay by cryptocurrency

# HW:
# - update the flawchart
# -* maybe convert crypto to cash / card

service_price = 100 # $

client_cash_amount = int(input("Enter cash amount: ")) # $

if client_cash_amount >= service_price:
    print("CASH Payment success!")
else:
    print("CASH Payment failure!")
    client_card_amount = int(input("Enter card amount: ")) #$

    if client_card_amount >= service_price:
        print("CARD Payment success!")
    else:
        print("CARD Payment failure!")
        client_crypto_amount = int(input("Enter crypto amount: ")) # not $ but bitcoin
        bitcoin_to_dollar_coef = 20000
        client_crypto_amount_in_dollar = client_crypto_amount * bitcoin_to_dollar_coef

        if client_crypto_amount_in_dollar >= service_price:
            print("CRYPTO Payment success!")
        else:
            print("CRYPTO Payment failure!")  