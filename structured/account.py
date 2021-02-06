import oanda


class Account(oanda.Oanda):
    """ Account is class for the Oanda v20 API. """

    def __init__(self, conf_file):
        super().__init__(conf_file)

    def get_accounts(self):
        """ Get the list of Accounts the client is authorized
        to access and their associated properties.

        :returns
        accounts: `list` of accounts with properties
        """
        response = self.ctx.account.list()
        accounts = response.get('accounts')
        return accounts

    # /v3/accounts/{accountID}
    def get_account_details(self, account_id):
        """ Returns full details for Account, including trades, positions, orders"""
        response = self.ctx.account.get(account_id)
        raw = response.get('account')
        return raw.dict()

    # /v3/accounts/{accountID}/summary
    def get_account_summary(self, account_id):
        """ Returns summary for Account"""
        response = self.ctx.account.summary(account_id)
        raw = response.get('account')
        return raw.dict()

    # /v3/accounts/{accountID}/instruments
    def get_instruments(self, account_id):
        """ Get the list of tradeable instruments for the given Account.
        The list of tradeable instruments is dependent on the regulatory
        division that the Account is located in, thus should be the same
        for all Accounts owned by a single user. """
        resp = self.ctx.account.instruments(account_id)
        instruments = resp.get('instruments')
        instruments = [ins.dict() for ins in instruments]
        instruments = [(ins['displayName'], ins['name'])
                       for ins in instruments]
        return sorted(instruments)


x = Account('oanda.cfg')
accounts = x.get_accounts()

for account in accounts:

    account_instruments = x.get_instruments(account.id)
    account_details = x.get_account_details(account.id)
    account_summary = x.get_account_summary(account.id)

    print('Account Instruments:', account_instruments)
    print('Account Details:', account_details)
    print('Account Summary:', account_summary)
