# import account
import pytest

from structured import account


class TestAccount:

    def setup_method(self):
        self.client = account.Account('oanda.cfg')

    @pytest.fixture
    def account_id(self):
        return '101-001-17666413-001'

    def test_get_accounts(self, account_id):
        accounts = self.client.get_accounts()
        for account in accounts:
            assert account.id == account_id

    def test_get_account_details(self, account_id):
        account, last_transaction_id = self.client.get_account_details(account_id)
        print(account)

    def test_get_account_summary(self, account_id):
        account, last_transaction_id = self.client.get_account_summary(account_id)
        print(account.alias)

    def test_get_instruments(self, account_id):
        instruments = self.client.get_instruments(account_id)
        for index, instrument in enumerate(instruments):
            print(index, instrument)

    def test_configure_account(self, account_id):
        alias = "primo"
        margin_rate = 0.02

        print(self.client.configure_account(account_id, alias=alias, marginRate=str(margin_rate)))

    def test_view_changes_since(self, account_id):
        print(self.client.view_changes_since(account_id, sinceTransactionID=31))
