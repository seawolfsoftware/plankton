import oanda

oanda = oanda.Oanda('oanda.cfg')

ins = oanda.get_instruments()

# print(ins)
print(oanda.get_account_summary())
print('\n------------------------\n')
print(oanda.get_account_details())