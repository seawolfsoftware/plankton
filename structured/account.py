# import oanda
from structured import oanda


class Account(oanda.Oanda):
    """ Account is a Python wrapper class for accounts.py in Oanda v20 REST API. """

    def __init__(self, conf_file):
        super().__init__(conf_file)

    def get_accounts(self):
        """ Gets the list of Accounts the client is authorized to access
        and their associated properties.

        :returns
        accounts : (Array[AccountProperties])

        endpoint: /v3/accounts
        """
        response = self.ctx.account.list()
        accounts = response.get('accounts')
        return accounts

    def get_account_details(self, account_id):
        """ Gets the full details of a client’s Account.
        This includes full open Trade, open Position and pending Order representation.

        :returns
        account : (Account),
        lastTransactionID : (TransactionID)

        endpoint: /v3/accounts/{accountID}
        """
        response = self.ctx.account.get(account_id)
        account = response.get('account')
        last_transaction_id = response.get('lastTransactionID')
        return account, last_transaction_id

    def get_account_summary(self, account_id):
        """ Gets a summary for a single Account that a client has access to.

        :returns
        account : (AccountSummary),
        lastTransactionID : (TransactionID)

        A summary representation of a client’s Account.
        The AccountSummary does not provide to full specification of
        pending Orders, open Trades and Positions.

        endpoint: /v3/accounts/{accountID}/summary
        """
        response = self.ctx.account.summary(account_id)
        account_summary = response.get('account')
        last_transaction_id = response.get('lastTransactionID')
        return account_summary, last_transaction_id

    def get_instruments(self, account_id):
        """ Gets the list of tradeable instruments for the given Account.

        The list of tradeable instruments is dependent on the regulatory
        division that the Account is located in, thus should be the same
        for all Accounts owned by a single user.

        :returns
        instruments : (Array[Instrument]),
        lastTransactionID : (TransactionID)

        Modified instruments to return each instrument as a string which
        contains the base currency and quote currency delimited by a “_”.

        endpoint: /v3/accounts/{accountID}/instruments
        """
        response = self.ctx.account.instruments(account_id)
        instruments = response.get('instruments')
        instruments = [ins.dict() for ins in instruments]
        instruments = [(ins['displayName'], ins['name'])
                       for ins in instruments]
        last_transaction_id = response.get('lastTransactionID')
        return instruments, last_transaction_id

    def configure_account(self, account_id, **kwargs):
        """ Sets the client-configurable portions of an Account.

        **kwargs:
        alias : (string),
        marginRate : (DecimalNumber)

        endpoint: /v3/accounts/{accountID}/configuration
        """
        response = self.ctx.account.configure(account_id, **kwargs)
        assert response.status == 200

        # TODO  implement error handling for:
        #  HTTP 400 – The configuration specification was invalid.
        #  HTTP 403 – The configuration operation was forbidden on the Account.
        print('New alias is:', response.body['clientConfigureTransaction'].alias)
        print('New margin rate is:', response.body['clientConfigureTransaction'].marginRate)
        print('Last Transaction ID', response.body['lastTransactionID'])

    # /v3/accounts/{accountID}/changes
    def view_changes_since(self, account_id, **kwargs):
        """ Polls an Account for its current state and changes
        since a specific TransactionID.

        Args:
        **alias (str): account alias (defaults to "primary")
        """
        response = self.ctx.account.changes(account_id, **kwargs)
        print(response)
