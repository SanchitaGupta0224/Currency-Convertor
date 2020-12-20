from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

def my_func(answersinputeasy):
	if answersinputeasy==1:
		val=input("Enter currency code:")
		test=CurrencyCodes()
		cur_symbol = test.get_symbol(val)
		cur_name = test.get_currency_name(val)
		print("Currency symbol : " + cur_symbol+"\nCurrency name : "+cur_name)
		print("\n\n")
	elif answersinputeasy==2:
		val=input("Enter currency code:")
		x = CurrencyRates()
		print("Latest currency rates :\n")
		print(x.get_rates(val))
		print("\n\n")
	elif answersinputeasy==3:
		print("\nRate conversion from currency-1 to currency-2 :\n")
		val=input("Enter currency code (1) : ")
		val1=input("Enter currency code(2) : ")
		x = CurrencyRates()
		print(x.get_rate(val, val1))
		print("\n\n")
	elif answersinputeasy==4:
		print('\nLatest price of 1 bitcoin in required currency: ')
		val=input("Enter currency code:")
		b = BtcConverter()   
		print(b.get_latest_price(val))
		print("\n\n")
	elif answersinputeasy==5:
		print('Converting specific amount to bitcoins from required currency\n')
		val=input("Enter currency code : ")
		val1=int(input("Enter amount : "))
		b = BtcConverter()
		print(b.convert_to_btc(val1, val))
		print("\n\n")
	elif answersinputeasy==6:
		print('Coverting bitcoin to currency : \n')
		val=input("Enter currency code : ")
		val1=int(input("Enter amount : "))
		b = BtcConverter()
		print(b.convert_btc_to_cur(val1, val))
		print("\n\n")
	else:
		print('Invalid Input')




new_name=1
while new_name != 7:
	new_name = int(input("Enter\n1-Get symbol, and currency name using currency code \n2-List all latest currency rates for any currency\n3-Get rate conversion from one currency to another\n4-Latest price of 1 bitcoin in specific currency\n5-Convert amount to bitcoins of specific currency\n6-Convert Bitcoins to valid currency amount based on latest price\n7-Quit\n\nINPUT : "))
	if new_name != 7:
		my_func(new_name)