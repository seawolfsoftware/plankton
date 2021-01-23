import current

oanda = current.Current('oanda.cfg')

ins = oanda.get_instruments()

print(ins)