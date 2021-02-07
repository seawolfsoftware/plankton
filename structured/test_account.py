import account

client = account.Account('oanda.cfg')
accounts = client.get_accounts()

for account in accounts:

    account_instruments = client.get_instruments(account.id)
    account_details = client.get_account_details(account.id)
    account_summary = client.get_account_summary(account.id)

    print('Account Instruments:', account_instruments)
    # print('Account Details:', account_details)
    # print('Account Summary:', account_summary)

    alias = "primo"
    margin_rate = 0.02
    # for index, instrument in enumerate(account_instruments):
    #     print(index, instrument)
    # print(x.configure_account(account.id, alias=alias, marginRate=str(margin_rate)))

    # print(x.view_changes_since(account.id, sinceTransactionID=1))
    # print('Account Details:', account_details)

