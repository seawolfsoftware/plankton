import oanda


class Account(oanda.Oanda):
    """ Account is class for the Oanda v20 API. """

    def __init__(self, conf_file):
        super().__init__(conf_file)

    def get_accounts(self):
        """ Gets the list of Accounts
        the client is authorized to access and their associated properties.

        :returns
        accounts: `list` of accounts with properties
        """
        response = self.ctx.account.list()
        accounts = response.get('accounts')
        return response.get('accounts')

    # /v3/accounts/{accountID}
    def get_account_details(self, account_id):
        """ Gets the full details of a client’s Account.
        This includes full open Trade, open Position and pending Order representation.

        :returns
        account: Account
        """
        response = self.ctx.account.get(account_id)
        account_details = response.get('account')
        return account_details

    # /v3/accounts/{accountID}/summary
    def get_account_summary(self, account_id):
        """ Gets a summary for a single Account that a client has access to.

        :returns
        account_summary: AccountSummary

        A summary representation of a client’s Account.
        The AccountSummary does not provide to full specification of
        pending Orders, open Trades and Positions.
        """
        response = self.ctx.account.summary(account_id)
        account_summary = response.get('account')
        return account_summary

    # /v3/accounts/{accountID}/instruments
    def get_instrument_names(self, account_id):
        """ Gets the list of tradeable instruments for the given Account.

        The list of tradeable instruments is dependent on the regulatory
        division that the Account is located in, thus should be the same
        for all Accounts owned by a single user.

        :returns
        instruments: 'list' of strings

        Each string contains the base currency and quote currency delimited by a “_”.
        """
        resp = self.ctx.account.instruments(account_id)
        instruments = resp.get('instruments')
        instruments = [ins.dict() for ins in instruments]
        instruments = [(ins['displayName'], ins['name'])
                       for ins in instruments]
        return sorted(instruments)

    # /v3/accounts/{accountID}/configuration
    def configure_account(self, account_id, **kwargs):
        """ Sets the client-configurable portions of an Account.

        Args:
        **alias (str): account alias (defaults to "primary")
        **marginRate (float):
        """
        response = self.ctx.account.configure(account_id, **kwargs)

        assert response.status == 200
        print('New alias is:', response.body['clientConfigureTransaction'].alias)
        print('New margin rate is:', response.body['clientConfigureTransaction'].marginRate)
        print('Last Transaction ID', response.body['lastTransactionID'])

        return response.body


x = Account('oanda.cfg')
accounts = x.get_accounts()

for account in accounts:

    account_instruments = x.get_instrument_names(account.id)
    account_details = x.get_account_details(account.id)
    account_summary = x.get_account_summary(account.id)

    # print('Account Instruments:', account_instruments)
    # print('Account Details:', account_details)
    # print('Account Summary:', account_summary)

    alias = "primo"
    margin_rate = 0.02
    print(x.configure_account(account.id, alias=alias, marginRate=str(margin_rate)))
    # print('Account Details:', account_details)

